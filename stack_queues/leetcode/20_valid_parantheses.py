def validParantheses(s):
  stack = []

  for i in s:
    if i in "([{":
      stack.append(i)
    else:
      if len(stack) == 0:
        return False
      elif (i == ")" and stack[-1] != "("):
        return False
      elif (i == "]" and stack[-1] != "["):
        return False
      elif (i == "}" and stack[-1] != "{"):
        return False
      else:
        stack.pop()
  if len(stack) != 0: return False
  return True

print(validParantheses("()"))
print(validParantheses("(){}[]"))
print(validParantheses("(){}[]"))
print(validParantheses("(){}["))



