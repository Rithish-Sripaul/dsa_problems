def reverse_string(s):
  s = list(s)[::-1]
  low, high = 0, 0
  ans = []
  while high < len(s):
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
      
      ans.append(temp_ans)
      ans.append(" ")
  
  return "".join(ans)[::-1]

print(reverse_string("the sky is blue"))