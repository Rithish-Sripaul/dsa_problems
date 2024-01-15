def containsDuplicate(nums):

    hash_ = {}

    for i in nums:
        if i in hash_:
            return True
        else:
            hash_[i] = 1

    return False
