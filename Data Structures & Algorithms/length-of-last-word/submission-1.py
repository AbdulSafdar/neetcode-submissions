class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ''
        for c in s.split():
            last_word = c
        
        return len(last_word)
            