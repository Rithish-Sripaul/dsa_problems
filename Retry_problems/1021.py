def remove_parantheses(s):
  ans, stack = [], []
  temp, count = 0, 0

  for i in s:
    if i == "(":
      stack.append("(")
      count += 1
    else:
      temp += 1
      if temp == count:
        stack.pop(0)
        ans.extend(stack)
        stack = []
        temp, count = 0, 0
      else:
        stack.append(i)
  return "".join(ans)

print(remove_parantheses("(()())(())"))
print(remove_parantheses("(()())(())(()(()))"))
print(remove_parantheses("()()"))
