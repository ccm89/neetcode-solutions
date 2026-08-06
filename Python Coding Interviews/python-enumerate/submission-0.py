from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    # returns the index of the first 
    # occurrence of the number 7 in 
    # the list nums, or -1 if 7 is not found.
    notFound = -1
    for i, num in enumerate(nums):
        if num == 7:
            return i
    return notFound
            

    


def get_dist_between_sevens(nums: List[int]) -> int:
    # returns the distance between the first 
    # and second occurrence of the number 7 in the list nums.
    i, j = -1, -1
    cnt = 0
    for index, num in enumerate(nums):
        if num == 7 and cnt == 0:
            i = index
            cnt += 1
        elif num == 7 and cnt == 1:
            j = index
            return j - i

# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
