def maxParant(s):
  stack = []
  ans = 0
  for i in s:
    if i == "(":
      stack.append(i)
    elif i == ")":
      ans = max(ans, len(stack))
      stack.pop()
  return ans

print(maxParant("(1+(2*3)+((8)/4))+1"))
print(maxParant("(1)+((2))+(((3)))"))
print(maxParant("()(())((()()))"))
