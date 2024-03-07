def with_ascii_values(s, t):
  value = 0

  for i in s:
    value += ord(i)

  for i in t:
    value -= ord(i)
    if value < 0:
      return False
  
  return True if value == 0 else False

s = "anagram"
t = "nagaram"
print(with_ascii_values(s, t))