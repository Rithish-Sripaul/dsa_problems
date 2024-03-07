def string_to_int(s, num, flag):

  if len(s) == 0: return num if not flag else -num
  # if len(s) == 1:
  #   if s.isnumeric() : return int(s) + (num * 10) if not flag else -(int(s) + (num * 10))
  #   return num * 10 if not flag else -(num * 10)
  
  if s[0].isnumeric() == False:
    if s[0] == "-": return string_to_int(s[1:], num, True)
    elif s[0] == "+": return string_to_int(s[1:], num, False)
    return 0 if num == 0 else string_to_int(s[1:], num, flag)
  num = int(s[0]) + (num * 10)
  return string_to_int(s[1:], num, flag)

  

s = 'words and 987'
print(string_to_int(s, 0, False))
  