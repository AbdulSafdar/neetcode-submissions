class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        countmap_S = {}
        countmap_T = {}

        for l in s:
            if l in countmap_S:
                countmap_S[l] +=1
            else:
                countmap_S[l] = 1
        
        for l in t:
            if l in countmap_T:
                countmap_T[l] +=1
            else:
                countmap_T[l] = 1

        if countmap_S == countmap_T:
            return True
        else:
            return False


