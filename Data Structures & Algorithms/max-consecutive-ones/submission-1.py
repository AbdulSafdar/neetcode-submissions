class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_cons = 0
        cons = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cons+=1
                if max_cons < cons:
                    max_cons = cons
            else:
                cons=0
            

            
        return (max_cons)
                