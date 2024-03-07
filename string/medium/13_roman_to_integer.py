def first_approach(s):
  romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

  prev = False
  ans = 0
  for i in s:
    if not prev:
      ans += romans[i]
    else:
      if romans[prev] >= romans[i]:
        ans += romans[i]
      else:
        ans -=  romans[prev]
        ans += romans[i] - romans[prev]

    prev = i
  return ans

s = "III"
s1 = "LVIII"
s2 = "MCMXCIV"
print(first_approach(s))
print(first_approach(s1))
print(first_approach(s2))