def first_approach(num):
  end = len(num) - 1
  while True:
    if end < 0:
      return ""
    if int(num[end]) % 2 == 1:
      return num[:end + 1]
    end -= 1

# Jun 7
def largestOddNumber_Second(num):
  n = len(num) - 1

  while True:
    if int(num[n]) % 2 == 1:
      return num[:n + 1]
    n -= 1
    if n < 0:
      break
  return ""

num = "52"
# num = "1404"
print(first_approach(num))