def find(index, path):
  if len(path) == len(digits):
    res.append(path)
    return
  for i in range(len(keyboard[digits[index]])):
    find(index + 1, path + keyboard[digits[index]][i])



keyboard = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}
digits = "23"
res = []
find(0, "")
print(res)