def first_approach(s):
  arr = [0] * 26

  for i in s:
    arr[ord(i) - 97] += 1
  
  print(arr)

s = "aabcb"
print(first_approach(s))