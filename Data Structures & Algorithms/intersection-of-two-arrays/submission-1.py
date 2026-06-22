class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}



        for num in nums1:
            if num in nums1 and num in nums2 and num not in hashMap:
                hashMap[num] = 1
        
        return(list(hashMap.keys()))
