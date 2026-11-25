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
def mutateList(rand,nums):


def mutate(rand,words,inputType):

def main():

