class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        def expand(beg, end):
            nonlocal res, reslen
            while beg >= 0 and end < len(s) and s[beg] == s[end]:
                if end - beg + 1 > reslen:
                    res = s[beg:end+1]
                    reslen = end - beg + 1
                beg -= 1
                end += 1

        for i in range(len(s)):
            # Odd length palindrome
            expand(i, i)
            # Even length palindrome
            expand(i, i+1)

        return res