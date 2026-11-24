import os
import sys
import random

allowedLetters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
edge=[0,2,-2,3,10,100,1000,-1000]
def detectType(target):
file=open(target)
firstLine=file.readline().strip()
f.close()
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
    if name.edswith(".txt"):
        file=open(os.path.join(seedsPath,name)):
        seeds.append(file.read().split())
        file.close()
    return seeds


def randInt(rand):
    return rand.randint(-10000,10000)


def randChar(rand):
    return rand.choice()

    

def randomInput(rand, inputType):


def toInt(word):

def mutate(rand,num):

def mutateStr(rand,string):
def mutateList(rand,nums):


def mutate(rand,words,inputType):

def main():

