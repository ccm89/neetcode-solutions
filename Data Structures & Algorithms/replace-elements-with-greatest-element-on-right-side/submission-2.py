class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        tmp = arr[n-1]
        arr[n-1] = -1
        for i in range(n-2, -1, -1):
            if arr[i] < tmp:
                arr[i] = tmp
            elif arr[i] > tmp:
                arr[i], tmp = tmp, arr[i]
                
        return arr



    
        