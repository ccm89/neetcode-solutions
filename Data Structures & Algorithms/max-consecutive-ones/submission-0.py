class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most_ones = 0
        curr_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_ones += 1
            elif nums[i] == 0:
                if curr_ones > most_ones:
                    most_ones = curr_ones
                curr_ones = 0
        if curr_ones > most_ones:
            return curr_ones
        else:
            return most_ones