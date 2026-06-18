class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap = {}
        for n in nums:
            if n in countmap:
                return True
            else:
                countmap[n] = 1
        return False