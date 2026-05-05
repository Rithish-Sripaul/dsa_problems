def maxProfit(prices: list[int]) -> int:
  buy_index = 0
  sell_index = 1
  n = len(prices)

  profit = 0

  while buy_index < sell_index and sell_index < n:
    if prices[buy_index] < prices[sell_index]:
      profit += prices[sell_index] - prices[buy_index]

    buy_index += 1
    sell_index += 1
  return profit

def maxProfit(prices: list[int]) -> int:
  profit = 0

  for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
      profit += profit[i] - profit[i - 1]
  return profit

prices =  [1, 2, 3, 4, 5]
prices = [7, 1, 5, 3, 6, 4]
prices = [5, 4, 3, 2, 1]
print(maxProfit(prices))

