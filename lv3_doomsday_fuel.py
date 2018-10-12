# Doomsday Fuel

# =============
# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter
# involved. It starts as raw ore, then during processing, begins randomly changing between forms,
# eventually reaching a stable form. There may be multiple stable forms that a sample could
# ultimately reach, not all of which are useful as fuel.
# Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by
# predicting the end state of a given ore sample. You have carefully studied the different
# random, the probability of each structure transforming is fixed. That is, each time the ore is in 1
# state, it has the same probabilities of entering the next state (which might be the same state).
# You have recorded the observed transitions in a matrix. The others in the lab have hypothesized
# more exotic forms that the ore can become, but you haven't seen all of them.
# Write a function answer(m) that takes an array of array of nonnegative ints representing how
# many times that state has gone to the next state and return an array of ints for each terminal
# state giving the exact probabilities of each terminal state, represented as the numerator for each
# state, then the denominator for all of them at the end and in simplest form. The matrix is at most
# 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state
# to a terminal state. That is, the processing will always eventually end in a stable state. The ore
# starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as
# long as the fraction is simplified regularly.
# For example, consider the matrix m:
# [
# [0,1,0,0,0,1], # s0, the initial state, goes to s1 and s5 with equal probability
# [4,0,0,3,2,0], # s1 can become s0, s3, or s4, but with different probabilities
# [0,0,0,0,0,0], # s2 is terminal, and unreachable (never observed in practice)
# [0,0,0,0,0,0], # s3 is terminal
# [0,0,0,0,0,0], # s4 is terminal
# [0,0,0,0,0,0], # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].

# Test cases
# ==========
# Inputs:
# (int) m = [
# [0, 2, 1, 0, 0], 
# [0, 0, 0, 3, 4], 
# [0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0]]
# Output:
# (int list) [7, 6, 8, 21]

# Inputs:
# (int) m = [
# [0, 1, 0, 0, 0, 1], 
# [4, 0, 0, 3, 2, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0]]
# Output:
# (int list) [0, 3, 2, 9, 14]

def construct_tree(input_matrix):
        queue = [[0, 1, 1]]
        terminal_queue = []
        non_terminal_nodes_set = set()

        while len(queue) != 0:
                tmp_node = queue.pop(0)
                if tmp_node[0] in non_terminal_nodes_set:
                        continue

                tmp_queue = []
                denominator = 0
                for idx in range(len(input_matrix[tmp_node[0]])):
                        if input_matrix[tmp_node[0]][idx] != 0:
                                denominator += input_matrix[tmp_node[0]][idx]
                                tmp_queue.append([idx, input_matrix[tmp_node[0]][idx], 0])
                if denominator == 0:
                        terminal_queue.append(tmp_node)
                else:
                        non_terminal_nodes_set.add(tmp_node[0])
                        for idx_elem in tmp_queue:
                                idx_elem[1] *= tmp_node[1]
                                idx_elem[2] = denominator * tmp_node[2]
                                queue.append(idx_elem)
                        
        return terminal_queue

def find_gcd(number1, number2):
        larger = max(number1, number2)
        smaller = min(number1, number2)
        remainder = larger%smaller
        if remainder == 0:
                return smaller
        else:
                return find_gcd(remainder, smaller)

def dividen_add(node1, node2):
        denominator_gcd = find_gcd(node1[1], node2[1])
        lcm = node1[1]*node2[1]//denominator_gcd

        node1_factor = lcm//node1[1]
        node2_factor = lcm//node2[1]
        return [node1[0]*node1_factor+node2[0]*node2_factor, lcm]

def normalized_terminate_nodes(terminal_queue):
        if len(terminal_queue) == 0:
                return -1
        result_dict = {}
        for elem in terminal_queue:
                if elem[0] not in result_dict:
                        result_dict[elem[0]] = [elem[1], elem[2]]
                else:
                        result_dict[elem[0]] = dividen_add(result_dict[elem[0]], [elem[1], elem[2]])

        tmp_tuple = [0, 1]
        for key in result_dict:
                tmp_tuple = dividen_add(tmp_tuple, result_dict[key])
        for key in result_dict:
                factor = tmp_tuple[1]//result_dict[key][1]
                result_dict[key] = [factor*result_dict[key][0], tmp_tuple[1]]
        
        return result_dict, tmp_tuple[0]


def answer(input_matrix):
        scan_result = construct_tree(input_matrix)
        sum_dict, new_denominator = normalized_terminate_nodes(scan_result)
        returning_array = []
        for row_number in range(len(input_matrix)):
                is_all_zero = True
                for col in input_matrix[row_number]:
                        if col != 0:
                                is_all_zero = False
                                break
                if is_all_zero:
                        returning_array.append(row_number)

        for idx in range(len(returning_array)):
                returning_array[idx] = sum_dict.get(returning_array[idx], [0, 1])[0]
        returning_array.append(new_denominator)

        return returning_array

if __name__ == '__main__':
        testcase1 =[
        [0, 1, 0, 0, 0, 1], 
        [4, 0, 0, 3, 2, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

        testcase2 = [
        [0, 2, 1, 0, 0], 
        [0, 0, 0, 3, 4], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]]
        print(answer(testcase1))
        print(answer(testcase2))