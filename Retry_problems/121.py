def first_approach(prices):

    low, high = 0, 1
    maxTillNow = 0
    while low <= high and high < len(prices):
        if prices[low] < prices[high]:
            diffInPrice = prices[high] - prices[low]
            maxTillNow = max(maxTillNow, diffInPrice)
        else:
            low = high
        high += 1

    return maxTillNow

prices = [7, 1, 5, 3, 6, 4]
prices1 = [4, 3, 2, 1]
print(first_approach(prices1))