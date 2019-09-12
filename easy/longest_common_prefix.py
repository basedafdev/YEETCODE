def longestCommonPrefix(strs):
    c = strs
    i = 0
    while(len(strs) > 1):
        print("STEP")
        vlong = longCommonPrefix(c[0],c[1])
        print(c, vlong)
        c.append(longCommonPrefix(c[0],c[1]))
        print(c)
        c.remove(c[0])
        c.remove(c[0])
        print(c)
        
    print(strs)
    return c[0]
def longCommonPrefix( s1, s2):
    shorter = ""
    longer = ""
    if len(s1) >= len(s2):
        longer = s1
        shorter = s2
    else:
        longer = s2
        shorter = s1
    for i in range(len(shorter),0,-1):
        if shorter[0:i] in longer:
            return shorter[0:i]
    return ""

longestCommonPrefix(["abca","aba","aaab"])