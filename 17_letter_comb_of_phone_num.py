def letterCombinations(digits):
    result = []
    if len(digits) == 0:
        return result
    digitToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def backtrack(i, currStr):
        if len(currStr) == len(digits):
            result.append(currStr)
            return

        for c in digitToChar[digits[i]]:
            backtrack(i + 1, currStr + c)

    backtrack(0, "")

    return result

print(letterCombinations("23"))
print(letterCombinations("7362"))


        
