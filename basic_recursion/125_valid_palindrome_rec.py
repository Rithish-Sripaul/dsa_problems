def check_palindrome(string, i):
  if i == len(string):
    return True
  if string[i] != string[len(string) - i - 1]:
    return False

  return True and check_palindrome(string, i + 1)
s = "A man, a plan, a canal: Panama"
s = "".join(letter for letter in s if letter.isalnum()).lower()
print(check_palindrome(s, 0))
print(s)
# print(" ".isalnum())
