def largestOddNumber(num):
  n = len(num) - 1

  while True:
    if int(num[n]) % 2 == 1:
      return num[:n + 1]
    n -= 1
    if n < 0:
      break
  return ""

print(largestOddNumber("55634"))
print(largestOddNumber("42"))