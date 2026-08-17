from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_lst = [0] * len(nested_arr)
    for i, subList in enumerate(nested_arr):
        for j, val in enumerate(subList):
            if val > max_lst[i]:
                max_lst[i] = val
    return max_lst


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
