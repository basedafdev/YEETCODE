class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numtoletters = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        combinations = []
        if (len(digits) == 0):
            return combinations
        elif (len(digits) == 1):
            return numtoletters[digits[0]]
        initial = numtoletters[digits[0]]
        for i in range(1, len(digits)):
            temparr = numtoletters[digits[i]]
            product = [i+str(j) for i in initial for j in temparr]
            combinations = product
            initial = combinations
            
        return combinations

            
            