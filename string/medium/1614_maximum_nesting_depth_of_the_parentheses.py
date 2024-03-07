def first_approach(s):

  stack = []
  curr_open, max_open = 0, 0
  for i in range(len(s)):
    if s[i] == "(":
      curr_open += 1
      max_open = max(max_open, curr_open)
      stack.append("(")
    elif s[i] == ")":
      curr_open -= 1
      stack.pop()
  
  return max_open

s = "(1+(2*3)+((8)/4))+1"
s1 = "(1)+((2))+(((3)))"
print(first_approach(s))
print(first_approach(s1))
