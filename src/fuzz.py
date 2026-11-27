import os
import sys
import random

allowedLetters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
edge=[0,2,-2,3,10,100,1000,-1000]

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
        file=open(os.path.join(seedsPath,name)):
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
    return int(word)

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
        rand.choice(edge)
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
            string =string[:index]+randChar(rand)+ string[index:]
    if choice==2:
        index=rand.randint(0, len(string))
        string = string[:index] + randChar(rand)+ string[index:]
    if choice ==3:
         index=rand.randint(0, len(string)-2)
         string = string[:index] + string[index+1:]
    return string

def mutateList(rand,nums):
    choice=rand.randint(1,4)
    if choice==1:
    elif choice==2:
    elif choice ==3:
    elif choice==4:

    return nums
    


def mutate(rand,words,inputType):
    choice=rand.randint(1,3)
    if choice==1:
    if choice==2:
    if choice ==3:
    
    return []]

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
        elif args[i]=="--random":
        elif target is None:
            target=args[i]
            i+=1
        else:
            seedPath=args[i]
            i+=1
    target=os.path.abspath(target)
    inputType=detectType(target)
    seeds=getSeeds(seeedPath)
    rand=random.Random(randomSeed)

    file=open(target)
    code=compile(file.read(), target, "exec")
    file.close()

    sys.path.insert(0,os.patj.dirname(target))
    tracker+coverage.Coverage(data_file=None, include= [target])
    tracker.start()

    corpus=[]
    coveredLines=set()
    seenErrors=set()
    runCount=0
    totalRuns=len(seeds)+budget
    while runCOunt<totalRuns:
        if runCount<len(seeds):
        elif useRandom or len(corpus)==0:
        else:



