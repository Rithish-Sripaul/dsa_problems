def rec(index, path):
  if index >= len(digits):
    res.append(path)
    return

  letters = dic[digits[index]]
  for i in letters:
    rec(index + 1, path + i)

dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

res = []
digits = "23"
rec(0, '')
print(res)