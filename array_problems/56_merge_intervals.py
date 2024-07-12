def merge_intervals(intervals):
  intervals.sort()

  stack = []

  for i in intervals:
    if not stack:
      stack.append(i)
    else:
      if stack[-1][1] > i[0]:
        interval = stack.pop()
        stack.append([min(interval[0], i[0]), max(interval[1], i[1])])
      else:
        stack.append(i)
  return stack

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,4],[0,4]]))