s = "* + 3 4 5".split()


stack = []

for i in s:
  if not i.isnumeric(): 
    stack.append(i)
  else:
    if stack[-1].isnumeric():
      x = int(stack.pop())
      y = int(i)
      op = stack.pop()
      if op == "+": stack.append(str(x + y))
      if op == "*": stack.append(str(x * y))
      if op == "-": stack.append(str(x - y))
      if op == "/": stack.append(str(int(x / y)))
      
    else:
      stack.append(i)

print(int(stack[0]))

print(s)