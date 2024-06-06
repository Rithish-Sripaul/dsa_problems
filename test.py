for _ in range(int(input())):
  n, k = list(map(int, input().split()))
  arr = list(map(int, input().split()))
  ans = 0
  ind = arr.index(min(arr))
  # Checking by replacing with one
  arr[ind] = 1
  for i in range(0, len(arr) - 1):
    ans += abs(arr[i] - arr[i+1])
  
  sec_ans = 0
  arr[ind] = k
  for i in range(0, len(arr) - 1):
    sec_ans += abs(arr[i] - arr[i+1])
  print(max(ans, sec_ans))
  