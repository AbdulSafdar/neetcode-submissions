class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        countmap = {}

        for n in nums:
            if n in countmap:
                countmap[n] += 1
            else:
                countmap[n] = 1
        largest = -1

        for keys, vals in countmap.items():
            if keys > largest:
                if vals == 1:
                    largest = keys
        return largest
                        