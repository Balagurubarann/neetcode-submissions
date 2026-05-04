class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        alphabets = [0] * 26
        totalLen = len(s)

        for i in range(totalLen):

            alphabets[ord(s[i]) - ord('a')] += 1
            alphabets[ord(t[i]) - ord('a')] -= 1

        for alpha in alphabets:

            if alpha > 0: return False

        return True
