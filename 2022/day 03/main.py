import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput

def main():
    txt = readAdventInput("2022", "03")
    lines = [ [line[:len(line)//2], line[len(line)//2:]] for line in txt.splitlines()]
    total = 0

    for halves in lines:
        item = findIteminCommon(halves[0], halves[1])
        priority = getPriority(item)
        total += priority
  
    print(f"The total priority is {total}")

def findIteminCommon(firstHalf: str, secondHalf: str) -> str:
    for item in firstHalf:
        for item2 in secondHalf:
            if item == item2:
                return item

def getPriority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1

main()