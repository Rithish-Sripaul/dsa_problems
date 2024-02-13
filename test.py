# 121 - Best time to buy and sell stocks

def best_time_buy_stock(prices):
  left, right = 0, 1
  maxTillNow = 0

  while right < len(prices):
    if prices[left] < prices[right]:
      maxTillNow = max(maxTillNow, prices[right] - prices[left])
    else:
      left = right

    right += 1
  
  return maxTillNow


prices = [7, 1, 5, 3, 6, 4]
print(best_time_buy_stock(prices))