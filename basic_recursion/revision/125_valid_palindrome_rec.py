def check_palindrome(s, start, end):
  if start > end:
    return True
  
  if not s[start].isalnum():
    return check_palindrome(s, start + 1, end)
  
  if not s[end].isalnum():
    return check_palindrome(s, start, end - 1)
  
  return False if s[start] != s[end] else check_palindrome(s, start + 1, end - 1)


s_arr = ["aaa", "aaab", "race a car"]

for s in s_arr:
  print(check_palindrome(s, 0, len(s) - 1))