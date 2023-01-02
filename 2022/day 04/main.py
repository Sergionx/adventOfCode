import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput

def main():
    txt = readAdventInput("2022", "04")
    lines = txt.splitlines()

    totalOverlaps = 0
    for line in lines:
        firstPair, secondPair = line.split(",")

        firstRange = [int(i) for i in firstPair.split("-")]
        secondRange = [int(i) for i in secondPair.split("-")]

        print(firstRange, secondRange)

        if firstRange[0] <= secondRange[0] and firstRange[1] >= secondRange[1]:
            print("Overlap")
            totalOverlaps += 1
        elif secondRange[0] <= firstRange[0] and secondRange[1] >= firstRange[1]:
            print("Overlap")
            totalOverlaps += 1

    print(f"Total Overlaps: {totalOverlaps}")
main()