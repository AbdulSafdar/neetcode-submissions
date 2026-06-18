class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countMap_s = {}
        countMap_t = {}

        for l in s:
            if l in countMap_s:
                countMap_s[l]+=1
            else:
                countMap_s[l] = 1
        
        for l in t:
            if l in countMap_t:
                countMap_t[l]+=1
            else:
                countMap_t[l] = 1

        if countMap_s == countMap_t:
            return True
        else:
            return False
