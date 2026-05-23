class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        countmap = {}
        for numbers in nums:
            if numbers not in countmap:
                countmap[numbers] = 1
            else:
                countmap[numbers] +=1
                return(True)
        return(False)