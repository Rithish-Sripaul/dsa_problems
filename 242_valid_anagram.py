# There are two possible methods for this:
# 1. Hash Table
# 2. Sorting

# Method 1:  Hash Table
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    hash_s, hash_t = {}, {}

    for i in range(len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

    return hash_s == hash_t


# print(isAnagram("anagram", "nagaram"))

# Method 2: Sorting
def isAnagramSorting(s, t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    return s == t

# print(isAnagramSorting("ana", "aan"))
# print(isAnagramSorting("rat", "car"))

# 08/05/2025

def isAnagram2025(s, t):
    arr = [0] * 26

    for char in s:
        arr[97 - ord(char)] += 1
        
    for char in t:
        if arr[97 - ord(char)] == 0:
            return False
        arr[97 - ord(char)] -= 1
    
print(isAnagram2025("anagram", "nagaram"))
print(isAnagram2025("car", "cat"))