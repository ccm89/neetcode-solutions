class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        # res = []
        res = 0
        for num in nums:
            if num:
                cnt += 1
            else:
                # res.append(cnt)
                cnt = 0
        # res.append(cnt)
            res = max(cnt, res)
        
        return res
