def find_max_divided_by_3(input_list):
    cpy_list = sorted(input_list)

    list_sum = sum(cpy_list)
    remain = list_sum % 3

    idx_1 = -1
    idx_2 = -1

    if remain == 1:
        for idx in range(len(cpy_list)):
            if cpy_list[idx] % 3 == 1:
                idx_1 = idx
                cpy_list.pop(idx)
                break

    if remain == 2:
        for idx in range(len(cpy_list)):
            if cpy_list[idx] % 3 == 2:
                idx_2 = idx
                cpy_list.pop(idx)
                break

    if remain == 2 and idx_2 == -1:
        for idx in range(len(cpy_list)):
            if cpy_list[idx] % 3 == 1:
                if idx_2 == -1:
                    idx_2 = idx
                    continue
                else:
                    idx_1 = idx
                    cpy_list.pop(idx)
                    cpy_list.pop(idx_2)
                    break

    if remain == 1 and idx_1 == -1:
        for idx in range(len(cpy_list)):
            if cpy_list[idx] % 3 == 2:
                if idx_1 == -1:
                    idx_1 = idx
                    continue
                else:
                    idx_2 = idx
                    cpy_list.pop(idx)
                    cpy_list.pop(idx_1)
                    break

    else:
        str_list = reversed([ str(elem) for elem in cpy_list ])
        value = int(''.join(str_list))
        return value
    return 0
        
def main():
    input_list0 = [3, 1, 4, 1, 9, 5]
    input_list1 = [1, 4, 1, 9, 5]
    input_list2 = [3, 1, 4, 1, 9]
    input_list3 = [3, 1, 3, 1, 9, 5]
    input_list4 = [3, 1, 7, 1, 9, 5, 0]

    print(input_list0)
    print(find_max_divided_by_3(input_list0))
    print(input_list1)
    print(find_max_divided_by_3(input_list1))
    print(input_list2)
    print(find_max_divided_by_3(input_list2))
    print(input_list3)
    print(find_max_divided_by_3(input_list3))
    print(input_list4)
    print(find_max_divided_by_3(input_list4))

if __name__ == '__main__':
    main()
