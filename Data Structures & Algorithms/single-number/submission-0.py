class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}

        for val in nums:
            if val in map:
                map.pop(val)
            else:
                map[val] = 1
        
        for key in map:
            return key