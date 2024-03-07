def first_approach(s):

  isNegative = False
  numberStarted = False
  ans = []

  i = 0
  n = len(s)
  while i < n:
    
    if s[i] == " " and i + 1 != n:
      i += 1
    else:
      if s[i] == "-":
        isNegative = True
      elif s[i] == "+":
        isNegative = False
      
      if s[i].isnumeric():
        ans.append(s[i])
        numberStarted = True
      else:
        if numberStarted:
          break
      i += 1
  
  ans = int("".join(ans))
  return ans if not isNegative else -ans

s = " asdasd  -423 with asdas"
print(first_approach(s))
  
        