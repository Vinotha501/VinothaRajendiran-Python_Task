# Implement a Binary Search Tree (BST)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert
# Time Complexity : O(log n), Each insertion traverse at most log(n) levels of the tree.
def Insert(Node, data):
    if Node is None:
        return TreeNode(data)
    else:
        if data < Node.data:
            Node.left = Insert (Node.left, data)

        elif data > Node.data:
            Node.right = Insert (Node.right, data)
           
    return Node    

# Inorder_traversal
def Inorder(Node):
    if Node is None:
        return 
    Inorder(Node.left)
    print(Node.data, end=", ")
    Inorder(Node.right)

# Preorder_traversal
def Preorder(Node):
     if Node is None:
          return
     print (Node.data, end=", ")
     Preorder (Node.left)
     Preorder (Node.right)

# Postorder_traversal
def Postorder(Node):
     if Node is None:
          return
     Postorder (Node.left)
     Postorder (Node.right)
     print (Node.data, end=", ")

# Minvalue
def Minvalue(Node):
    current = Node
    while current.left is not None:
        current = current.left
    return current

# Delete
# Time Complexity : O(log n), Find node & adjust pointers.
def Delete (Node, data):
    if not Node:
        return None
    
    if data < Node.data:
            Node.left = Delete (Node.left, data)

    elif data > Node.data:
            Node.right = Delete (Node.right, data)

    else:
        if not Node.left:
              temp = Node.right
              Node = None
              return temp
         
        elif not Node.right:
              temp = Node.left
              Node = None
              return temp
             
        Node.data = Minvalue (Node.right).data
        Node.right = Delete (Node.right, Node.data) 

    return Node

# Search
# Time Complexity : O(log n), Searching node from root to leaf.
def Search(Node, target):
    if Node is None:
          return None
    elif Node.data == target:
         return Node
    elif target < Node.data:
         return Search(Node.left, target)
    else:
         return Search(Node.right, target)

# Height    
def Height(Node):
    if Node is None:
        return 0
    else:
         left_height = Height(Node.left)
         right_height = Height(Node.right)
         return 1+max(left_height,right_height)
    
# IsBalanced
def IsBalanced(Node):
    if Node is None:
        return True
    
    lh = Height(Node.left)
    rh = Height(Node.right)

    return (abs(lh - rh) <= 1) and IsBalanced(Node.left) and IsBalanced(Node.right)

# print nodes at the given depth
def NodesAtDepth(Node, depth):
    if Node is None:
        return
    if depth == 0:
        print(Node.data, end=" ")
    else:
        NodesAtDepth(Node.left, depth-1)
        NodesAtDepth(Node.right, depth-1)

# print the structure of the tree
def print_tree(node, level=0, label=","):
     if node is not None:
       print_tree(node.right, level + 1)
       print(" " * 4 * level + str(node.data))
       print_tree(node.left, level + 1)

# Tree constrution
root = TreeNode(12)

Node6 = TreeNode(6)
Node7 = TreeNode(7)
Node2 = TreeNode(2)
Node17 = TreeNode(17)
Node13 = TreeNode(13)
Node18 = TreeNode(18)

root.left = Node6
root.right = Node17

Node6.left = Node2
Node6.right = Node7

Node17.left = Node13
Node17.right = Node18


# Inorder
print("Inorder_traversal:")
Inorder (root)

# Insert
print("\nInsert:")
Insert(root, 20)
Insert(root, 16)
Inorder (root)

#Preorder
print("\nPreorder_traversal:")
Preorder (root)

#Postorder
print("\nPostorder_traversal:")
Postorder (root)

# Delete
print("\nDelete:")
Delete(root,14)

#Traverse
Inorder (root)

# Search
result = Search(root,6)
if result:
     print(f"\nValue found is : {result.data}")
else:
     print("\nValue not found")

# Height of the Binary search tree
print(f"Height of the tree : {Height(root)}")

# Isbalanced
if IsBalanced(root):
     print("Tree is balanced")
else:
     print("Tree is not balanced")

# print the structure of the tree
print("\nBinary Tree Structure:")
print_tree(root)

# print nodes at the given depth
depth = 1
print(f"\nNodes at depth {depth:}:")
NodesAtDepth(root, depth)

     
     