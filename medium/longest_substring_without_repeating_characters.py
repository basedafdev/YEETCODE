class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      tempdict = {}
      streaks = []
      temp = 0
      for l in s:
        if l not in tempdict:
          tempdict[l] = 0
          temp = temp + 1
        else:
          tempdict = {l: 0}
          streaks.append(temp)
          temp = 1

      return max(streaks)