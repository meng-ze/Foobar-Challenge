#
# The Grandest Staircase Of Them All
# ==================================
# With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order 
# to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how 
# to build the best staircase EVER. 
# Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the 
# different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know 
# how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options.
# Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step 
# must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total 
# amount of bricks that make up that step.
# For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and 
# the second step having a height of 1: (# indicates a brick)
# #
# ##
# 21
# When N = 4, you still only have 1 staircase choice:
# #
# #
# ##
# 31
 
# But when N = 5, there are two ways you can build a staircase from the given bricks. 
# The two staircases can have heights (4, 1) or (3, 2), as shown below:
# #
# #
# #
# ##
# 41
# #
# ##
# ##
# 32
# Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can 
# be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, 
# because Commander Lambda's not made of money!
# Languages
# =========
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
# Test cases
# ==========
# Inputs:
#     (int) n = 3
# Output:
#     (int) 1
# Inputs:
#     (int) n = 200
# Output:
#     (int) 487067745
# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
# */
from math import sqrt

def find_all_combination_for(brick_number, below_number, memoized_table):
    if brick_number < 3 or below_number < 2:
        if brick_number < 0:
            return 0
        return 1

    if memoized_table[brick_number][below_number] != 0:
        return memoized_table[brick_number][below_number]

    if memoized_table[brick_number][0] == 0:
       memoized_table[brick_number][0] = find_smallest_level(brick_number)
    range_begin = memoized_table[brick_number][0]

    tmp_sum = 0
    for i in range(range_begin, below_number):
        tmp_sum += find_all_combination_for(brick_number-i, i, memoized_table)
    memoized_table[brick_number][below_number] = tmp_sum
    return tmp_sum

def find_smallest_level(brick_number):
    based_number = brick_number*2 + 0.25
    result = sqrt(based_number)-0.5
    if result - int(result) > 0:
        result = result + 1
    result = int(result)
    return result

def answer(n):
    memoized_table = [[0 for i in range(n+1)] for j in range(n+1)]
    result = find_all_combination_for(n, n, memoized_table)
    return result

# def other_answer(n):
#     combinations = [[0 for rows in range(n)] for cols in range(n + 1)]

#     # If n < 3, there are no possibilities for building the stairwell.
#     for first_three in range(3):
#         for num in range(first_three, n):
#             combinations[first_three][num] = 1

#     # For the rest of them, the formula is incremental.
#     for num in range(3, n + 1):
#         for bot in range(2, n):
#             combinations[num][bot] = combinations[num][bot - 1]
#             if bot <= num:
#                 combinations[num][bot] += combinations[num - bot][bot - 1]

#     # This index on the matrix should contain our solution to the number of distinct combinations.
#     return combinations[n][n - 1]

if __name__ == '__main__':
    print(answer(200))
