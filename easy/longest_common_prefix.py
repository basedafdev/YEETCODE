class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if strs == []:
            return ""
        while(len(strs) > 1):
            strs.append(self.longCommonPrefix(strs[0],strs[1]))
            if (len(strs) == 2):
                return self.longCommonPrefix(strs[0],strs[1])
            strs.remove(strs[0])
            strs.remove(strs[0])
            
        return strs[0]
        
    def longCommonPrefix(self, s1, s2):
        shorter = ""
        longer = ""
        if len(s1) >= len(s2):
            longer = s1
            shorter = s2
        else:
            longer = s2
            shorter = s1
        for i in range(len(shorter),0,-1):
            print(shorter[0:i])
            if shorter[0:i] in longer:
                if shorter[0:i] in longer[0:len(shorter[0:i])]:
                    return shorter[0:i]
        return ""
            
            
