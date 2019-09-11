class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestStr = ""
        for i in range (0, len(s)):
            for b in range(len(s), 0 ,-1 ):
                substr = s[i:b]
                if (len(substr) < len(longestStr)):
                    break
                if (substr == substr[::-1] and len(substr) > len(longestStr)):
                    longestStr = substr
            if (len(longestStr) > len(s) - i):
                break
        return longestStr
x = Solution()
print(x.longestPalindrome("babad"))