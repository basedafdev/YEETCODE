class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0 
        ROMAN_NUMERAL_TABLE = [
            ("M", 1000), ("D", 500),("C", 100),
            ("L", 50),  ("X", 10),("V", 5), ("I", 1)
        ]
        WACK = [("CM", 900),("CD", 400),("XC", 90), ("XL", 40),("IX", 9), ("IV", 4)]
        
        for roman,numeral in WACK:
            if roman in s:
                s = s.replace(roman,"",1)
                value = value + numeral
         
        while(s != ""):
            for roman, numeral in ROMAN_NUMERAL_TABLE:
                if roman in s:
                    s = s.replace(roman,"",1)
                    value = value + numeral
                    
        return value