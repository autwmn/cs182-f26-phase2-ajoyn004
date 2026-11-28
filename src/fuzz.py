import os
import sys
import random
import contextlib
import traceback
import io
import coverage


allowedLetters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
edge=[0,1,-1,2,10,100,1000,-1000]

def detectType(target):
    file=open(target)
    firstLine=file.readline().strip()
    file.close()
    if firstLine == "# input: int":
        return "int"
    if firstLine == "# input: str":
        return "str"
    if firstLine == "# input: ints":
        return "ints"
    return "other"

def getSeeds(seedPath):
    seeds=[]
    for name in sorted(os.listdir(seedPath)):
        if name.endswith(".txt"):
            file=open(os.path.join(seedPath,name))
            seeds.append(file.read().split())
            file.close()
    return seeds


def randInt(rand):
    return rand.randint(-10000,10000)


def randChar(rand):
    return rand.choice(allowedLetters)

    

def randomInput(rand, inputType):
    if inputType=="int":
        return[str(randInt(rand))]
    if inputType=="str":
        size=rand.randint(1,10)
        string=""
        for i in range(size):
            string+= randChar(rand)
        return [string]
                
    if inputType=="ints":
        size=rand.randint(1,10)
        nums=[]
        for i in range(size):
            nums.append(str(randInt(rand)))
        return nums
    return []
    
        


def toInt(word):
    try:
        return int(word)
    except ValueError:
        return 0

def mutateInt(rand,num):
    choice=rand.randint(1,5)
    if choice==1:
        step=0
        while step==0:
            step=rand.randint(-16,16)
        return num+step
    if choice==2:
        return -num
    if choice==3:
        return rand.choice(edge)
        
    if choice==4:
        digits=list(str(abs(num)))
        index= rand.randint(0,len(digits)-1)
        digits[index]=str(rand.randint(0,9))
        num2 = int("".join(digits))
        if num<0:
            num2=-num2
        return num2

    return randInt(rand)
        

def mutateStr(rand,string):
    choice=rand.randint(1,3)
    if choice==1:
        if len(string)>0:
            index=rand.randint(0,len(string)-1)
            string =string[:index]+randChar(rand)+ string[index+1:]
    if choice==2:
        index=rand.randint(0, len(string))
        string = string[:index] + randChar(rand)+ string[index:]
    if choice ==3:
         if len(string)>0:
             index=rand.randint(0, len(string)-1)
             string = string[:index] + string[index+1:]
    return string

def mutateList(rand,nums):
    choice=rand.randint(1,4)
    if choice==1:
        if len(nums)>0:
            index=rand.randint(0,len(nums-1))
            nums[index]=mutateInt(rand,nums[index])
    elif choice==2:
        index=rand.randint(0,len(nums)-1)
        nums.insert(index,randInt(rand))
    elif choice ==3:
        if len(nums)>0:
            index=rand.randint(0,len(nums))
            del nums[index]
    elif choice==4:
        if len(nums)>=2:
            a=rand.randint(0,len(nums)-1)
            b=rand.randint(0,len(nums)-1)
            nums[a],nums[b]=nums[b],nums[a]
    return nums
    


def mutate(rand,words,inputType):
    times=rand.randint(1,3)
    if inputType=="int":
        num=0
        if len(words)>0:
            num=toInt(words[0])
        for i in range(times):
            num=mutateInt(rand,num)
        return [str(num)]
    if inputType=="str":
        string =" ".join(words)
        for i in range(times):
            string=mutateStr(rand,string)
        return string.split()
    if inputType=="ints":
        nums=[]
        for word in words:
            nums.append(toInt(word))
        for i in range(times):
            nums=mutateList(rand,nums)
        result=[]
        for num in nums:
            result.append(str(num))
        return result
    
    return []
def runTarget(tracker, code, target, words):
    savedArgv=sys.argv
    sys.argv=[target]+words
    error=None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            with contextlib.redirect_stderr(io.StringIO()) :
                exec(code, {"__name__": "__main__","__file__": target})
    except SystemExit:
        pass
    except Exception as err:
        crashLine=0
        for entry in traceback.extract_tb(err.__traceback__):
            if entry.filename==target:
                crashLine=entry.lineno
        error=type(err).__name__+ " at line " + str(crashLine)
    sys.argv=savedArgv



    hitLines=set()
    covData=tracker.get_data()
    for file in covData.measured_files():
        hitLines.update(covData.lines(file))
    return hitLines,error





def main():
    args=sys.argv[1:]
    target=None
    seedPath=None
    budget =15000
    randomSeed=0
    useRandom =False
    i=0
    while i<len(args):
        if args[i]=="--budget":
            budget=int(args[i+1])
            i+=2
        elif args[i]=="--seed":
            randomSeed=int(args[i+1])
            i+=2
        elif args[i]=="--random":
            useRandom=True
            i+=1
        elif target is None:
            target=args[i]
            i+=1
        else:
            seedPath=args[i]
            i+=1
    target=os.path.abspath(target)
    inputType=detectType(target)
    seeds=getSeeds(seedPath)
    rand=random.Random(randomSeed)

    file=open(target)
    code=compile(file.read(), target, "exec")
    file.close()

    sys.path.insert(0,os.path.dirname(target))
    tracker=coverage.Coverage(data_file=None, include= [target])
    tracker.start()

    corpus=[]
    coveredLines=set()
    seenErrors=set()
    runCount=0
    totalRuns=len(seeds)+budget
    while runCount<totalRuns:
        if runCount<len(seeds):
            words=seeds[runCount]
        elif useRandom or len(corpus)==0:
            words =randomInput(rand,inputType)
        else:
            base=rand.choice(corpus)
            words = mutate(rand,base,inputType)
        runCount+=1

        hitLines,error= runTarget(tracker, code, target, words)
        isNew=len(hitLines)>len(coveredLines)
        coveredLines=hitLines
        shown=" ".join(words)

        if error is not None:
            if error not in seenErrors:
                seenErrors.add(error)
                print("Execution " + str(runCount) + ": EXCEPTION " + error + " input="+ shown)
        elif isNew:
            corpus.append(words)
            print("Execution " + str(runCount) + ": NEW #lines=" + str(len(coveredLines)) + " input="+ shown)
    tracker.stop()
    print("DONE #executions=" +str(runCount) + " #corpus_inputs=" +str(len(corpus))+" #lines=" + str(len(coveredLines))+ " #exceptions=" +str(len(seenErrors)))

if __name__=="__main__":
     main()
        



