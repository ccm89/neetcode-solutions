class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointer solution:
        # The idea is to swap the target to the back and move the desired values up.
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k +=1
        return k
