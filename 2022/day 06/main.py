import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput, readAdventTestInput

def main():
    txt = readAdventInput("2022", "06").strip()
    packetMarker = findPacketMarker(txt)
    
    print(f"The start of the packet is at index: {packetMarker}")

def findPacketMarker(txt: str) -> int:
    for i in range(0, len(txt) - 3):
        char1, char2, char3, char4 = txt[i], txt[i+1], txt[i+2], txt[i+3]
        if checkAllDifferent(char1, char2, char3, char4):
            return i + 4 

def checkAllDifferent(char1: str, char2: str, char3: str, char4: str) -> bool:
    if char1 != char2 and char1 != char3 and char1 != char4:
        if char2 != char3 and char2 != char4:
                if char3 != char4:
                    print("all different")
                    return True
    return False



main()