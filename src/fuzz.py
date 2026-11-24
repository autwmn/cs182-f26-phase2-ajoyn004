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

def mutate(rand,num):

def mutateStr(rand,string):
def mutateList(rand,nums):


def mutate(rand,words,inputType):

def main():

