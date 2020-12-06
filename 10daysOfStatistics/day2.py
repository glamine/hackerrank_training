# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:10:53 2020

@author: guill
"""


# Set data
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1) * len(dice2)
total_possibilities = 0

# Verify possibilities
for i in range(len(dice1)):
    for j in range(len(dice2)):
        if (dice2[j] + dice1[i]) <= 9:
            total_possibilities = total_possibilities + 1
            print("{0} + {1} = {2}".format(dice1[i], dice2[j], (dice2[j] + dice1[i])))

# Get probability
probability = total_possibilities / total
print("Probability: {0}/{1} = {2}".format(total_possibilities,total,probability))


########################
#%%

# Set data
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1) * len(dice2)
total_possibilities = 0

# Verify possibilities
for i in range(len(dice1)):
    for j in range(len(dice2)):
        if (dice1[i] + dice2[j]) == 6 and (dice1[i] != dice2[j]):
            total_possibilities = total_possibilities + 1
            print("{0} + {1} = {2}".format(dice1[i], dice2[j], (dice1[i] + dice2[j])))

# Get probability
probability = total_possibilities / total
print("Probability: {0}/{1} = {2}".format(total_possibilities,total,probability))


#%% Set data
x = {"Red":4/7, "Black":3/7}
y = {"Red":5/9, "Black":4/9}
z = {"Red":4/8, "Black":4/8}

# Get possibilities
first_possibility = x["Red"] * y["Red"] * z["Black"]
second_possibility = x["Red"] * y["Black"] * z["Red"]
third_possibility = x["Black"] * y["Red"] * z["Red"]

# Get probability
print(first_possibility + second_possibility + third_possibility)