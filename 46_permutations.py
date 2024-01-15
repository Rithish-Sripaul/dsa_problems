def permute(nums):

    result = []

    # base case
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        # print(f"Before: {perms}")
        for perm in perms:
            perm.append(n)

        # print(f"After: {perms}")
        result.extend(perms)
        print(result)
        nums.append(n)
    return result

print(permute([1, 2, 3]))
