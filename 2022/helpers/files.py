from io import TextIOWrapper
import os
def readAdventInput(year: str, day: str) -> str:
    with open(os.path.join(os.getcwd(), f"{year}\day {day}\input.txt"), "r") as f:
        return f.read()