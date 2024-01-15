def combinationSum(candidates, target):

    result = []
    freq = []
    def backtrack(currSum, currArr):
        if currSum == target:
            f = {}
            for i in currArr:
                if i in f:
                    f[i] += 1
                else:
                    f[i] = 0
            if f not in freq:
                freq.append(f)
                result.append(currArr)
            return
        if currSum > target:
            return
        
        for candidate in candidates:
            backtrack(currSum + candidate, currArr + [candidate])

    backtrack(0, [])
    return result

print(combinationSum([2, 3, 6, 7], 7))
