import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput

def main():
    txt = readAdventInput("2022", "03")
    findCommonItemInHalves(txt)
    findCommonItemIn3Groups(txt)
    turbofindCommonItemIn3Groups(txt)

#efficient version
def turbofindCommonItemIn3Groups(txt: str):
    lines = txt.splitlines()  
    total = 0
    count3Groups = 0

    encountered = {}
    for line in lines:
        count3Groups += 1

        if count3Groups == 1:
            encountered = {item: 1 for item in line}
        
        elif count3Groups == 2:
            used = set()
            for item in line:
                if (encountered.get(item) is not None and item not in used):
                  encountered[item] += 1
                  used.add(item)              
            
        elif count3Groups == 3:
            for item in line:
                if encountered.get(item) == 2:
                    total += getPriority(item)
                    break

            count3Groups = 0
  
    print(f"The turbo total priority by 3 groups is {total}")

def findCommonItemIn3Groups(txt: str):
    lines = txt.splitlines()  
    total = 0
    count3Groups = 0

    #I could just use the priority or the ord of the item as a key, but this is more readable
    encountered = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    encountered.update({chr(i): 0 for i in range(ord('A'), ord('Z') + 1)})
    for line in lines:
        
        count3Groups += 1
        item = getItemsInLine(line, encountered)
        # print(encountered)

        priority = 0
        if count3Groups == 3:
            for item in encountered:
                if encountered[item] == 3:
                    print(f"Found {item} in all 3 groups")
                    priority = getPriority(item)
                    break

            #reset encountered
            encountered = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
            encountered.update({chr(i): 0 for i in range(ord('A'), ord('Z') + 1)})

            count3Groups = 0
            total += priority
  
    print(f"The total priority by 3 groups is {total}")

def getItemsInLine(line: str, encountered: dict):
    used = set()
    for item in line:
        if item not in used:
          encountered[item] += 1
          used.add(item)

def findCommonItemInHalves(txt: str):
    lines = [ [line[:len(line)//2], line[len(line)//2:]] for line in txt.splitlines()]   
    total = 0

    for halves in lines:
        item = findItemInCommon(halves[0], halves[1])

        priority = getPriority(item)
        total += priority
  
    print(f"The total priority by halve is {total}")

def findItemInCommon(firstHalf: str, secondHalf: str) -> str:
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