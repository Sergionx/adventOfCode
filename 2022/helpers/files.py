import os

def readAdventInput(year: str, day: str) -> str:
    with open(os.path.join(os.getcwd(), f"{year}\day {day}\input.txt"), "r") as f:
        return f.read()

def readAdventTestInput(year: str, day: str) -> str:
    with open(os.path.join(os.getcwd(), f"{year}\day {day}\input-test.txt"), "r") as f:
        return f.read()