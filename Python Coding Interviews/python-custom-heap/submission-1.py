import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    #           (sort_key, payload)
    max_heap = [(-num, num) for num in nums]
    heapq.heapify(max_heap)
    res = []
    while max_heap:
        sort_key, num = heapq.heappop(max_heap)
        res.append(num)
    return res


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
