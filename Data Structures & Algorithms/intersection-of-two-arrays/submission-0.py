class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = []
        for num in nums1:
            if num in nums2 and num not in array:
                array.append(num)


        return(array)