class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons = 0
        max_val = 0

        if max_val >= cons:
            for i in range(len(nums)):
                if nums[i] == 1:
                    cons+=1
                    if cons > max_val:
                        max_val = cons
                else:
                    cons=0
                    
        

        return(max_val)