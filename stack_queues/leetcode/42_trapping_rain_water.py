def trappingRainwater(height):
  prefix, suffix = [], []
  stack = []

  # Suffix
  for i in range(len(height) - 2, -1, -1):
    while stack and stack[-1] <= height[i]:
      stack.pop()

    if stack:
      suffix.insert(0, stack[-1])
    else:
      suffix.insert(0, height[i])
    stack.append(height[i])

  # Prefix
  stack=[]
  for i in range(1, len(height)):
    while stack and stack[-1] <= height[i]:
      stack.pop()
    if stack:
      prefix.append(stack[-1])
    else:
      prefix.append(height[i])
    stack.append(height[i])

  print(prefix, suffix)
  ans = []
  for i in range(len(height)):
    ans.append(min(prefix[i], suffix[i]) - height[i])
  print(ans)
  print(sum(ans))

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

trappingRainwater(height)