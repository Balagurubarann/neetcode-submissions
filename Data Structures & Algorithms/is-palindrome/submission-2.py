class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1: return True

        s = "".join(i.lower() for i in s if i.isalnum())

        s = "".join(s.split(" "))

        i = 0
        j = len(s) - 1

        while i <= j:

            if s[i] != s[j]: return False

            i += 1
            j -= 1

        return True
        