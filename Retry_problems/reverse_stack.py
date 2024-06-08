def reverseStack(St, i, j):
  if i >= j:
    return St
  St[i], St[j] = St[j], St[i]
  return reverseStack(St, i + 1, j - 1)

St = [3, 2, 1, 7, 6]
print(reverseStack(St, 0, len(St) - 1))
