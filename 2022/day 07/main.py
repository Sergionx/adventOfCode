import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput, readAdventTestInput
from helpers.dataStructures import StackNoNode as Stack, NodeTree, Tree


def main():
    txt = readAdventTestInput("2022", "07")
    lines = txt.splitlines()

    tree = Tree(NodeTree("/", 0, [])) #Responsible to construct the whole directory of the disk

    cdPath = Stack() #Responsible for keeping track of the current directory
    for line in lines:
        instructionParts = line.split(" ")
        
        # print(instructionParts)
        if instructionParts[0] == "$": 
            command(instructionParts, cdPath)
        else: 
            fileOrDirectory(instructionParts, cdPath, tree)
    print(tree)

    sum = calculateDirSum(tree.root)
    print(f"Sum of all directories with a total size at most 100000: {sum}")


def command(instructionParts: list, cdPath: Stack):
    match instructionParts[1]:
        case "cd":
            if instructionParts[2] == "..":
                return cdPath.pop()

            return cdPath.push(instructionParts[2])
        case "ls":
            pass

def fileOrDirectory(instructionParts: list, cdPath: Stack, tree: Tree):
    if instructionParts[0] == "dir": 
        node = NodeTree(instructionParts[1], 0, [])
        tree.addNodeByName(node, cdPath.peek())
    else: # File
        node = NodeTree(instructionParts[1], int(instructionParts[0]), [])
        tree.addNodeByName(node, cdPath.peek())

def calculateDirSum(node: NodeTree) -> int:
    sum = 0
    if node.weight == 0:
        for child in node.children:
            node.weight += calculateDirSum(child)
        if node.weight <= 100000:
            return node.weight
    return node.weight
    
main()