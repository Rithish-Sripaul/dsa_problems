def infix_to_postfx(str):
  stack = []
  ans = []

  for i in str:
    # Order of precedence
    # ^, */, +-

    if len(stack) == 0 or stack[-1] == "(":
      stack.append(i)
    elif i == "+"

