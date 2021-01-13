# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:44:32 2021

@author: guill
"""

import sys

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

    def levelOrder(self,root):
        #Write your code here
        
        myQueue = [root]
        treeString = ""
        
        while myQueue != []:
            
            if myQueue[0] == None:
                
                myQueue.pop(0)
            
            else:

                pathLeft = myQueue[0].left
                pathRight = myQueue[0].right 
                
                treeString += str(myQueue[0].data) + " "
                #print(treeString)
                
                myQueue.pop(0)
                
                # improve by not adding if value is None (quicker)
                myQueue.append(pathLeft)
                myQueue.append(pathRight)
        
        print(treeString)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)