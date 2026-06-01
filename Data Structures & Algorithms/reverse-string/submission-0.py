class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        L, R = 0, len(s) - 1
        val_L = 0
        val_R = 0
        while L < R:
            val_L = s[L]
            val_R = s[R]
            s[R] = val_L
            s[L] = val_R
            R-=1
            L+=1
