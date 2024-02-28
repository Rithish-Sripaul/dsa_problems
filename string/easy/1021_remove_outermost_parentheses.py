def first_approach(s):
  ans = []
  stack = []
  temp = 0
  count = 0
  for i in range(len(s)):
    if s[i] == "(":
      stack.append(s[i])
      count += 1
    else:
      temp += 1
      if temp == count:
        stack.pop(0)
        ans.extend(stack)
        stack = []
        temp, count = 0, 0
      else:

        stack.append(s[i])
  
  return "".join(ans)

s = "(()())(())"
s1 = "(()())(())(()(()))"
s2 = "()()"
# print(first_approach(s))
print(first_approach(s1))
# print(first_approach(s2))
