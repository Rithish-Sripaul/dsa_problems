def first_approach(num):
  end = len(num) - 1
  while True:
    if end < 0:
      return ""
    if int(num[end]) % 2 == 1:
      return num[:end + 1]
    end -= 1
  
num = "52"
# num = "1404"
print(first_approach(num))