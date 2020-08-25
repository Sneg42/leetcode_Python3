#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # =====================================================================================
    # Function to insert nodes in level order  
    def insertLevelOrder(arr, root, i, n): 
        # Base case for recursion. n - len root
        if i < n: 
            temp = Treenode(arr[i])  
            root = temp  

            # insert left child  
            root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)  

            # insert right child  
            root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
        return root

    # Function to print tree nodes in  
    # InOrder fashion  
    def inOrder(root): 
        if root != None: 
            inOrder(root.left)  
            print(root.data,end=" ")  
            inOrder(root.right) 

