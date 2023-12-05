import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput, readAdventTestInput
from helpers.dataStructures import StackNoNode as Stack

def main():
    txt = readAdventInput("2022", "05")
    lines = txt.splitlines()

    crateList = []
    stacks, startInstructions = createStackList(lines, crateList)
    populateStacks(stacks, crateList)

    for i in range(startInstructions + 1, len(lines)):
        readInstruction9001(lines[i], stacks)
    
    for stack in stacks:
        print(stack.peek())

def createStackList(lines: list[str], crateList: list[str]) -> list[Stack]:
    stacks = []
    startInstrucionts = 0
    for line in lines:
        startInstrucionts += 1
        if line[1].isdigit():
            stacks = [Stack() for _ in range(int(line[-2]))]
            break
        else:
            crateList.append(line)
        
    return stacks, startInstrucionts

def populateStacks(stacks: list[Stack], crateList: list[str]):
    #Read from bottom to top the list of crates
    for line in reversed(crateList):
        characters = [char for char in line]

        #Every 4th character is a  crate
        for i in range(1, len(characters), 4):
            if characters[i] != " ":
                stacks[i // 4].push(characters[i])

def readInstruction9000(instructionLine: str, stacks: list[Stack]):
    instruction = instructionLine.split(" ")
    numberCrates = int(instruction[1])
    fromStack = int(instruction[3])
    toStack = int(instruction[5])

    for _ in range(numberCrates):
        stacks[toStack - 1].push(stacks[fromStack - 1].pop())

def readInstruction9001(instructionLine: str, stacks: list[Stack]):
    instruction = instructionLine.split(" ")
    numberCrates = int(instruction[1])
    fromStack = int(instruction[3])
    toStack = int(instruction[5])

    if numberCrates == 1:
        stacks[toStack - 1].push(stacks[fromStack - 1].pop())
        return

    auxList = []
    for _ in range(numberCrates):
        auxList.append(stacks[fromStack - 1].pop())
    
    for i in range(len(auxList) -1,-1, -1):
        stacks[toStack - 1].push(auxList.pop(i))

main()