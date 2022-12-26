import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput

def main():
    txt = readAdventInput("2022", "01")
    #separate the lines of the txt file
    lines = txt.splitlines()
    maxCalories = {
        1: 0,
        2: 0,
        3: 0,
    }
    currentCalories = 0

    for line in lines:
        if line == '':
            if maxCalories[1] == 0:
                maxCalories[1] = currentCalories
            
            elif currentCalories > maxCalories[1]:
                maxCalories[1], maxCalories[2], maxCalories[3] = currentCalories, maxCalories[1], maxCalories[2]

            elif currentCalories > maxCalories[2]:
                maxCalories[2], maxCalories[3] = currentCalories, maxCalories[2]
            
            elif currentCalories > maxCalories[3]:
                maxCalories[3] = currentCalories

            print(maxCalories)
            currentCalories = 0
            continue
        
        currentCalories += int(line)
        # print(currentCalories)

    print(sum(list(maxCalories.values())))
main()




