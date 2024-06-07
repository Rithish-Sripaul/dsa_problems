def rotateString(s, goal):
  if len(s) != len(goal):
    return False
  
  # Rotating a string
  s = list(s)
  goal = list(goal)
  for i in range(len(s)):
    last = s[0]
    for i in range(len(s) - 1):
      s[i] = s[i + 1]
    s[-1] = last

    if s == goal:
      return True
  return False

def secondApproach(s, goal):
  for i in range(len(s)):
    if s[i] == goal[0]:
      if s[i:] + s[:i] == goal:
        return True
  return False
    

print(rotateString("abcde", "cdeab"))
print(rotateString("abcde", "abced"))


