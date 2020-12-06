# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:39:09 2020

@author: guill
"""



if __name__ == '__main__':
    
    n = int(input())
    
    myDic = {}
    
    for i in range(n):

        arr = list(input().rstrip().split())
        
        myDic[arr[0]] = int(arr[1])

    while True:
        try:
            q = input()
            if q in myDic:
                print(q + "=" + str(myDic[q]))
            else:
                print("Not found")
        except:
            
            break
        
    ##############♦ OR 
        
    while True:
        query = input()
        if query != "":
    
            if query in myDic.keys():
                print(query + "=" + str(myDic[query]))
            else:
                print("Not found")
        else:
            break
