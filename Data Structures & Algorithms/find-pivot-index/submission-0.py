class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        self.prefix = []
        total = sum(nums)
        leftSum = 0
        rightSum = 0
        for i, n in enumerate(nums):
            rightSum = total - leftSum - n
            
            if leftSum == rightSum:
                return(i)
            else:
                leftSum += n

        
        return (-1)

        