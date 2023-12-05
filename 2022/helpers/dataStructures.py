class StackNoNode:
    def __init__(self, items: list = []):
        self.items = items

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
    
    def __str__(self):
        return f"{self.items}"
    
    def __repr__(self):
        return self.__str__()

class NodeTree:
    def __init__(self, name: str, weight: int, children: list = []):
        self.name = name
        self.weight = weight
        self.children = children

    def __str__(self):
      
        return f"Name: {self.name} Weight: ({self.weight}) -> \n {self.children}"

    def __repr__(self):
        return self.__str__()

class Tree:
    def __init__(self, root: NodeTree = None):
        self.root = root

    def __str__(self):
        return f"{self.root} \n"

    def __repr__(self):
        return self.__str__()
    
    def searchNodeByName(self, aux: NodeTree, name: str):
        if aux.name == name:
            return aux
        for child in aux.children:
            node = self.searchNodeByName(child, name)
            if node != None:
                return node
        return None

    def addNode(self, node: NodeTree, parent: NodeTree):
        if self.root == None:
            self.root = node
        else:
            parent.children.append(node)

    def addNodeByName(self, node: NodeTree, parentName: str):
        if self.root == None:
            self.root = node
        else:
            parentNode = self.searchNodeByName(self.root, parentName)
            if parentNode != None:
                parentNode.children.append(node)
            else:
                raise Exception("Parent not found")