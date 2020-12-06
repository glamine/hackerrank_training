# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:19:08 2020

@author: guill
"""

# =============================================================================
# Objective 
# In this challenge, we get started with conditional probability. Check out the Tutorial tab for learning materials! 
# 
# 
# Task 
# Suppose a family has  children, one of which is a boy. What is the probability that both children are boys?
# 
# 1 / 3
# 1 / 2
# 2 / 3
# 1 / 9
# 
# Ans : 1/3
# explanation: The conditional probablity of A when B has occured already is denoted as P(A|B) = P(A∩B)/P(B)
# Conditional Probability: P(A|B) = P(A AND B)/P(A)
# 
# P(Both are Boys | One is a Boy) = P(Both are Boys AND One is a Boy)/P(One is a Boy)
# 
# P(One is a Boy)= 1 
# 
# P(Both are Boys AND One is a Boy) = 1/3 (if one is a boy then BB, BG, or GB)
# 
# P(Both are Boys | One is a Boy) = (1/3)/1 = 1/3
# =============================================================================


#%%

# Initially there is the possibility of 13/52, however after removing a card,
# the probability of the card being of the same suit falls to 12/51

print (12/51)

# OR 

# =============================================================================
# Objective 
# In this challenge, we're getting started with combinations and permutations. Check out the Tutorial tab for learning materials! 
# 
# 
# Task 
# You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?
# 
# 1 / 156
# 1 / 39
# 12 / 39
# 12 / 51
# 
# ans: 12/51
# 
# explanation: Initially you have 52 cards, 13*4 (4 suites). There are 13 ways to select a color card out of 52.
# again if you pick one more card, there are 12 remaining of the same color, out of total 51 remainig cards.
# No. of ways to select 2 cards = (1) * (2) = (13/52) * (12/51) = 3/51.
# This is for 1 color, as there are 4 colors, total = (4 * 3)/51 = 12/51.
# =============================================================================

#%%

# =============================================================================
# Task 
# A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. If the first marble drawn is red, what is the probability that the second marble is blue?
# 
# 1 / 12
# 7 / 12
# 1 / 6
# 2 / 3
# 
# A: 2/3
# explanation: After 1 red marble is drawn, there will be 2 red marbles and 4 blue marbles in the bag.So, in the bag's current state, 
# there is a 2/6 probability of drawing a red marble and  a 4/6 probability of drawing a blue marble.Because our goal is to find the 
# probability of drawing a blue marble, our answer is 4/6 (which reduces to 2/3 ).
# =============================================================================
