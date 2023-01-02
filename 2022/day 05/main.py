import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput, readAdventTestInput

class Stack:
    def __init__(self):
        self.items = []

    def show(self):
        print(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def main():
    txt = readAdventInput("2022", "05")
    lines = txt.splitlines()

    crateList = []
    stacks, startInstructions = createStackList(lines, crateList)
    populateStacks(stacks, crateList)

    for i in range(startInstructions + 1, len(lines)):
        readInstruction(lines[i], stacks)
    
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

def readInstruction(instructionLine: str, stacks: list[Stack]):
    instruction = instructionLine.split(" ")
    numberCrates = int(instruction[1])
    fromStack = int(instruction[3])
    toStack = int(instruction[5])

    for _ in range(numberCrates):
        stacks[toStack - 1].push(stacks[fromStack - 1].pop())

main()