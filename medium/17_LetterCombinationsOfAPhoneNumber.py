class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i): #generate all str starting at index i
            if len(digits) == 0:
                return

            if len(res) == len(digits):
                return ans.append("".join(res))

            for j in range(i, len(digits)):
                letters = keyboard[digits[j]]
                for l in letters:
                    res.append(l)
                    backtrack(j + 1)
                    res.pop(-1)
        
        res = []
        ans = []
        backtrack(0)
        return ans
