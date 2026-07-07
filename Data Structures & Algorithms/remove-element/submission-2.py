class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j  = n-1
        occurrences = 0 
        while i <= j:
            if nums[i] == val and nums[j] == val:
                j -= 1
            elif nums[i] == val and nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j -= 1
                occurrences += 1
            elif nums[i] != val and nums[j] == val:
                i += 1
                j -= 1
                occurrences +=1
            elif nums[i] != val and nums[j] != val:
                i += 1
                occurrences += 1
        return occurrences


            



