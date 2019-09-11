class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempdict = {}
        streaks = [0]
        temp = 0
        start = 0
        i = 0
        while(i < len(s)):
            if s[i] not in tempdict:
                tempdict[s[i]] = 0
                temp = temp + 1
    `       
            else:
                start = start + 1
                i = start
                tempdict = {s[i]: 0}
                temp = 1
            streaks.append(temp)
            i = i+1
        
        return max(streaks)
  
x = Solution()
nice = x.lengthOfLongestSubstring("dvdf") 
print(nice)