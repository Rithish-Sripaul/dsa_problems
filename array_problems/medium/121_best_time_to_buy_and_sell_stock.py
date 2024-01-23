def first_approach(prices):
  left, right = 0, 1
  maxTillNow = 0

  while right < len(prices):
    currMax = prices[right] - prices[left]
    if prices[left] < prices[right]:
      maxTillNow = max(maxTillNow, currMax)
    elif prices[left] > prices[right]:
      left = right

    right += 1

  return maxTillNow

prices = [7,1,5,3,6,4]
print(first_approach(prices))
  
