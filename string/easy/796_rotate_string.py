def first_approach(s, goal):
  if len(s) != len(goal):
    return False
  
  s_start, goal_start = 0, 0

  count = 0
  while True:
    s = s[1:] + s[:1]
    if s == goal:
      return True
    if count == len(s):
      return False
    count += 1
  

s = "abcde"
goal = "abced"
print(first_approach(s, goal))