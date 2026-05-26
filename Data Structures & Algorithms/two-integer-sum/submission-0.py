class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in countmap:
                return([countmap[diff], i])
            else:
                countmap[num] = i


