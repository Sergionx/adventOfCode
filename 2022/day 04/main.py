import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput

def main():
    txt = readAdventInput("2022", "04")
    lines = txt.splitlines()

    fullOverlaps = 0
    semiOverlaps = 0
    for line in lines:
        firstPair, secondPair = line.split(",")

        firstRange = [int(i) for i in firstPair.split("-")]
        secondRange = [int(i) for i in secondPair.split("-")]

        print(firstRange, secondRange)

        if firstRange[0] <= secondRange[0] and firstRange[1] >= secondRange[1]:
            print("Full Overlap")
            fullOverlaps += 1
        elif secondRange[0] <= firstRange[0] and secondRange[1] >= firstRange[1]:
            print("Full Overlap")
            fullOverlaps += 1
        #Calculating no overlap is more easy than calculating any overlap,
        #so if we calculater that, then the rest is semi overlap
        elif firstRange[1] < secondRange[0] or secondRange[1] < firstRange[0]:
            print("No Overlap")
        else:
            print("Semi Overlap")
            semiOverlaps += 1


    print(f"Full Overlaps: {fullOverlaps}")
    print(f"Semi Overlaps: {semiOverlaps}")
    print(f"Total Overlaps: {fullOverlaps + semiOverlaps}")
main()