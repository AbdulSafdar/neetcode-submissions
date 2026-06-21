class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max = arr[-1]

        for i in range(n-1, -1, -1):
            if arr[i] < max:
                arr[i] = max
            elif max < arr[i]:
                temp = arr[i]
                arr[i] = max
                max = temp
        
        arr[-1] = -1
        return arr
        


        