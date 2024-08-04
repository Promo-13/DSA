from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.left = leftChild
newBT.right = rightChild

def preOrderTraversal(root):
    if not root:
        return None
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    
def inOrderTraversal(root):
    if not root:
        return None
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)

def postOrderTraversal(root):
    if not root:
        return None
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)
    
def levelOrderTraversal(root):
    if not root:
        return None
    
    res = []
    q = deque()
    q.append(root)
    
    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.data)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    
    print(res)
    
def searchBT(root, target):
    if not root:
        return None
    if root.data == target:
        return root
    left = searchBT(root.left, target)
    right = searchBT(root.right, target)
    return left or right

def insertBT(root, data):
    if not root:
        root = TreeNode(data)
    else:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node.left:
                node.left = TreeNode(data)
                return "Succesfully inserted"
            else:
                q.append(node.left)
            if not node.right:
                node.right = TreeNode(data)
                return "Succesfully inserted"
            else:
                q.append(node.right)
                
def getDeepestNode(root):
    """ Function to get the deepest node in the binary tree """
    if not root:
        return None
    
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return node

def deleteDeepestNode(root, d_node):
    """ Function to delete the deepest node """
    if not root:
        return
    
    q = deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        
        if node is d_node:
            node = None
            return
        
        if node.right:
            if node.right is d_node:
                node.right = None
                return
            else:
                q.append(node.right)
        
        if node.left:
            if node.left is d_node:
                node.left = None
                return
            else:
                q.append(node.left)

def deleteNodeBT(root, key):
    """ Function to delete a node with given key """
    if not root:
        return None
    
    # If the tree is empty
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    
    # Find the node to delete
    key_node = None
    q = deque()
    q.append(root)
    
    while q:
        temp = q.popleft()
        
        if temp.data == key:
            key_node = temp
        
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    
    if key_node:
        # Get the deepest node
        deepest_node = getDeepestNode(root)
        
        # Replace key_node with deepest_node's value
        key_node.data = deepest_node.data
        
        # Delete the deepest node
        deleteDeepestNode(root, deepest_node)
    
    return root

def deleteBT(root):
    """ Function to delete the binary tree """
    root.data = None
    root.left = None
    root.right = None

newBT = TreeNode("Drinks")
leftchild = TreeNode("Cold")
rightchild = TreeNode("Hot")
newBT.left = leftchild
newBT.right = rightchild
res = insertBT(newBT,"Milkshake")
deleteNodeBT(newBT, "Cold")
levelOrderTraversal(newBT)
deleteBT(newBT)
levelOrderTraversal(newBT)
