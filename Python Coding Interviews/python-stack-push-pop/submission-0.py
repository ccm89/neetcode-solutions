from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    stack = []
    for e in arr:
        stack.append(e)
    rev_lst = []
    while len(stack) > 0:
        rev_lst.append(stack.pop())
    return rev_lst

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
