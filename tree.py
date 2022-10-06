class BST:
    left = None
    right = None
    value: int = None
    parent= None
    def __init__(self, left, right, parent ,value: int) -> None:
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent
    
    def addTheParentPropToNodes (self):
        if self.right:
            self.right.parent = self
            self.right.addTheParentPropToNodes()
        if self.left:
            self.left.parent = self
            self.left.addTheParentPropToNodes()
        
    def succor(self):
        if self.right:
            node = self.right
            while (node.parent is not None):
                if not node.left:
                    return node
                node = node.left
        node = self.parent
        while True:
            if node.parent.left == node:
                return node
            node = node.parent

    def predecessors (self):
        
        pass
                
        





leftChildOfLeft = BST(None, None, None ,15)
rightChildOfLeft = BST(None, None, None ,5)

leftChildOfRight = BST(None, None, None ,-5)
rightChildOfRight = BST(None, None, None ,-15)

leftChild = BST(leftChildOfLeft, rightChildOfLeft,None ,10)
rightChild = BST(leftChildOfRight, rightChildOfRight, None ,-10)

root = BST(leftChild, rightChild, None, 0)

root.addTheParentPropToNodes()

suc = root.succor()
print(suc , root)

