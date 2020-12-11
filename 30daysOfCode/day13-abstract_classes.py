# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:21:51 2020

@author: guill
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class

class MyBook(Book):
    
    def __init__(self, title, author, price):
        
        #super(myBook, self).__init__(title, author)
        #super().__init__(title, author)
        Book.__init__(self,title, author)
        self.price = price
        
    def display(self):
        
        print("Title: {0}\nAuthor: {1}\nPrice: {2}".format( \
                    self.title,self.author,self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()