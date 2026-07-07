class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most_ones = 0
        curr_ones = 0
        for num in nums:
            if num == 1:
                curr_ones += 1
            elif num == 0:
                curr_ones = 0
            most_ones = max(most_ones, curr_ones)
        return most_ones