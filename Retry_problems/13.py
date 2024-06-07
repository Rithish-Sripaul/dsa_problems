def romanToInteger(s):
  romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  if len(s) == 1:
    return romans[s]
  ans = romans[s[0]]
  for i in range(1, len(s)):
    if romans[s[i]] > romans[s[i - 1]]:
      ans -= romans[s[i - 1]]
      ans += romans[s[i]] - romans[s[i - 1]]
    else:
      ans += romans[s[i]]
  return ans

print(romanToInteger("III"))

print(romanToInteger("LVIII"))
print(romanToInteger("MCMXCIV"))



