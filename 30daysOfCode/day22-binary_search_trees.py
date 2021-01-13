# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:10:06 2021

@author: guill
"""

class Node:
    
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        
        return self.getHeight1(root) - 1
    
    def getHeight1(self,root):
    
        if root == None:
            return 0
        else:
            heightLeft = self.getHeight1(root.left)
            heightRight = self.getHeight1(root.right)
            
            height = max(heightLeft,heightRight) + 1
        
            return height

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height) 