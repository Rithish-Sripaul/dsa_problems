def time(prices):
  low, high = 0, 1
  maxProfit = 0

  while high < len(prices):
    if prices[low] < prices[high]:
      diff = prices[high] - prices[low]
      maxProfit = max(maxProfit, diff)
    else:
      low = high
    high += 1
  return maxProfit