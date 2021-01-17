# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:54:37 2021

@author: guill
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    # MY VERSION does not seem to work : does not work with data all the same
    # oui, first check if none, then only check data
    def removeDuplicatesBis(self,head):
        #Write your code here
        
        if head == None:
            return head
        elif head.next == None:
            return head
        else:
            currentNode = head
            while currentNode != None and currentNode.next != None:
                
                while currentNode.next != None and currentNode.data == currentNode.next.data:
                    
                    currentNode.next = currentNode.next.next
                    
                    # version with if does not work with more doublons
# =============================================================================
#                 if currentNode.data == currentNode.next.data:
#                 
#                     currentNode.next = currentNode.next.next
# =============================================================================
                    
                currentNode = currentNode.next
                
            return head
        
    def removeDuplicates(self,head):
        #Write your code here
        curr = head
        while curr is not None and curr.next is not None:
            while curr.next is not None and curr.data is curr.next.data:
                curr.next = curr.next.next
            curr = curr.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicatesBis(head)
mylist.display(head); 