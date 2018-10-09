# Ion Flux Relabeling
# ===================
# Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired 
# spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong 
# and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position 
# labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much 
# more quickly - quickly enough, perhaps, to earn a promotion!
# Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, 
# she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter 
# in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:
#    7                     
#  3   6                  
# 1 2 4 5               
# Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers 
# representing different flux converters - which returns a list of integers p where each element in p is the label of the 
# converter that sits on top of the respective converter in q, or -1 if there is no such converter.  For example, 
# answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of 
# height 3, which is [3, 6, -1].
# The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 
# represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, 
# two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p contain at least one but 
# no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.
# Languages
# =========
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
# Test cases
# ==========
# Inputs:
#     (int) h = 3
#     (int list) q = [7, 3, 5, 1]
# Output:
#     (int list) [-1, 7, 6, 3]
# Inputs:
#     (int) h = 5
#     (int list) q = [19, 14, 28]
# Output:
#     (int list) [21, 15, 29]
# Use verify [file] to test your solution and see how it does. When you are finished editing your code, 
# use submit [file] to submit your answer.
# If your solution passes the test cases, it will be removed from your home folder.

# class dfs:
#     time = 0
#     @staticmethod
#     def construct_tree(level):
#         returning_tree = ((2**level)-1) * [-1]
#         return returning_tree

#     @staticmethod
#     def dfs_aux(tree_array, index):
#         if index*2+2 > len(tree_array):
#             dfs.time = dfs.time+1
#             tree_array[index] = dfs.time
#             return dfs.time

#         if tree_array[index] == -1:
#             tree_array[index*2+1] = dfs.dfs_aux(tree_array, index*2+1)
#             tree_array[index*2+2] = dfs.dfs_aux(tree_array, index*2+2)
#             dfs.time = dfs.time+1
#             tree_array[index] = dfs.time

#         return dfs.time

#     @staticmethod
#     def post_order_dfs(tree_array):
#         for index in range(len(tree_array)):
#             if tree_array[index] == -1:
#                 dfs.dfs_aux(tree_array, index)
        
# def answer(h, q):
#     # your code here
#     if h > 30 or h < 1:
#         return -1

#     class dfs:
#         time = 0
#         @staticmethod
#         def construct_tree(level):
#             returning_tree = []
#             if level < 30 and level > 0:
#                 returning_tree = ((2**level)-1) * [-1]
#             return returning_tree

#         @staticmethod
#         def dfs_aux(tree_array, index):
#             if index*2+2 > len(tree_array):
#                 dfs.time = dfs.time+1
#                 tree_array[index] = dfs.time
#                 return dfs.time

#             if tree_array[index] == -1:
#                 tree_array[index*2+1] = dfs.dfs_aux(tree_array, index*2+1)
#                 tree_array[index*2+2] = dfs.dfs_aux(tree_array, index*2+2)
#                 dfs.time = dfs.time+1
#                 tree_array[index] = dfs.time

#             return dfs.time

#         @staticmethod
#         def post_order_dfs(tree_array):
#             for index in range(len(tree_array)):
#                 if tree_array[index] == -1:
#                     dfs.dfs_aux(tree_array, index)

#     tmp_tree = dfs.construct_tree(h)
#     dfs.post_order_dfs(tmp_tree)
#     search_array = len(tmp_tree) * [0]
#     for idx in reversed(range(1, len(tmp_tree))):
#         if idx % 2 == 0:
#             search_array[tmp_tree[idx]] = tmp_tree[(idx-2)//2]
#         else: 
#             search_array[tmp_tree[idx]] = tmp_tree[(idx-1)//2]
#     search_array.append(-1)

#     answers = []
#     for elem in q:
#         answers.append(search_array[elem])

#     return answers

def find_number(target, current, rec):
    right = current - 1
    left = right - (rec//2)

    if right == target or left == target:
        return current
    else:
        if target <= left:
            return find_number(target, left, rec//2)
        else:
            return find_number(target, right, rec//2)

def answer(h, q):
    # if(h > 30 or h < 1):
    #     raise ValueError('Height is outside of bounds')
    # if(len(q) > 10000 or len(q) < 1):
    #     raise ValueError('Flux converters list is outside of bounds')

    items=(2**h)-1

    array=[]
    for i in range(len(q)):
        if (q[i]<items and q[i]>0):
            array.append(find_number(q[i],items,items-1))
        else:
            array.append(-1)
    return array 
    
def main():
    ans1 = answer(6, [19, 14, 28])
    print(ans1)
    ans2 = answer(3, [7, 3, 5, 1])
    print(ans2)
    ans3 = answer(20, [2589, 3, 5, 1])
    print(ans3)

if __name__ == '__main__':
    main()