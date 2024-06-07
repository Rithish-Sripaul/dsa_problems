def first_approach(s):
  s = list(s)[::-1]
  ans = []

  low, high = 0, 0

  while high <= len(s) - 1:
    if s[high] == " " or high == len(s) - 1:
      
      temp_ans = []
      temp = high
      
      while temp >= low:
        if s[temp] == " " and len(temp_ans) == 0:
          temp -= 1
        else:
          temp_ans.append(s[temp])
          temp -= 1
      
      high += 1
      low = high

      if len(temp_ans) != 0:
        ans.append("".join(temp_ans))
        ans.append(" ")
      print(temp_ans)
    else:
      high += 1

  return "".join(ans[:-1])
    
s = "the sky is blue"
s1 = "   hello   world   "
print(first_approach(s))