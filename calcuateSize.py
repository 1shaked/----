class BinaryTreeNode:
    left = None
    right = None
    size = -1
    data = None
    maxDepth = -1
    minDepth = -1
    def __init__(self, data: int, parent=None):
        self.parent = parent 
        self.data = data

node  = BinaryTreeNode(0)
node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)
node9 = BinaryTreeNode(9)
node10 = BinaryTreeNode(10)
node11 = BinaryTreeNode(11)
node12 = BinaryTreeNode(12)

node.right  = node1
node1.right = node3
node1.left  = node5

node.left   = node2
node2.right = node4
node2.left  = node6
node5.right = node7
node5.left = node9
node6.left = node8
node4.right = node10
node7.left = node11
node10.left = node12


def addParent(T: BinaryTreeNode):
    if T.left:
        T.left.parent = T
        addParent(T.left)
    if T.right:
        T.right.parent = T
        addParent(T.right)
    

def updateMaxDepth(T: BinaryTreeNode):
    if T.maxDepth != -1:
        return T.maxDepth
    if T.left == None and T.right == None:
        T.maxDepth = 0
    elif T.left == None:
        T.maxDepth = 1 + updateMaxDepth(T.right)
    elif T.right == None:
        T.maxDepth = 1 + updateMaxDepth(T.left)
    else:
        T.maxDepth = max(updateMaxDepth(T.right) , updateMaxDepth(T.left)) + 1
    return T.maxDepth


def updateMinDepth(T: BinaryTreeNode):
    if T.minDepth != -1:
        return T.minDepth
    if T.left == None and T.right == None:
        T.minDepth = 0
    elif T.left == None:
        T.minDepth = 1 + updateMinDepth(T.right)
    elif T.right == None:
        T.minDepth = 1 + updateMinDepth(T.left)
    else:
        T.minDepth = min(updateMinDepth(T.right) , updateMinDepth(T.left)) + 1
    return T.minDepth



def updateSize(T: BinaryTreeNode):
    if T.size != -1:
        return T.size
    if T.left == None and T.right == None:
        T.size = 1
    elif T.left == None:
        T.size = 1 + updateSize(T.right)
    elif T.right == None:
        T.size = 1 + updateSize(T.left)
    else:
        T.size = updateSize(T.left) + updateSize(T.right) + 1
    return T.size


def printMinDepth(T: BinaryTreeNode):
    if T.minDepth == 0:
        return T
    elif T.right == None and T.left != None:
        return printMinDepth(T.left)
    elif T.left == None and T.right != None:
        return printMinDepth(T.right)
    elif  T.left.minDepth <= T.right.minDepth:
        return printMinDepth(T.left)
    else:
        return printMinDepth(T.right)


def printInorder(T: BinaryTreeNode):
    if T:
        printInorder(T.left)
        print(T.data)
        printInorder(T.right)



def findPrintOrder(T: BinaryTreeNode, node: BinaryTreeNode):
    count = 0
    if node.left:
        count += node.left.size
    if node.parent.left == T:
        return 0
    if node.parent.right == T:
        return 1 + T.left.size
    elif node.parent.right == node:
        count += 0
        


def findPrintOrder2(T: BinaryTreeNode, node: BinaryTreeNode):
    count = 1
    current = node
    if current.left:
        count += current.left.size
    
    while current != T:
        if current.parent.right == current:
            count += 1 
            if current.parent.left:
                count += current.parent.left.size 
        current = current.parent
        
    return count
        

addParent(node)

updateSize(node)
updateMinDepth(node)
printInorder(node)

order = findPrintOrder2(node, node10)
print(order)
minNode = printMinDepth(node)

# print(minNode.data)

print(node)