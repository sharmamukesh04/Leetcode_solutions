class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = s[::-1]
        for i in range(len(s), 0, -1):
            for j in range(0, len(s)):
                temp = s[j:j+i]
                if j+i<=len(s) and s[j:j+i]==temp[::-1]:
                    return s[j:j+i]

        return ""

        