def isValid(board: list[list[int]]) -> bool:
  nums = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
  }

  n, m = len(board), len(board[0])

  for i in range(n):
    for j in range(m):
      if board[i][j] != ".":
        nums[board[i][j]].append([i, j, i // 3, j // 3])

  for num, positions in nums.items():
    check_board = [["."] * 9 for _ in range(9)]

    for k in range(len(positions)):
      
      row = positions[k][0]
      col = positions[k][1]
      subBoxPosX = positions[k][2]
      subBoxPosY = positions[k][3]

      if num in check_board[row]:
        print("In the same row")
        return False
      
      for i in range(n):
        if num == check_board[i][col]:
          print(f"In the same column. Num: {num}. Row: {row}. Col: {col}. Check Row: {i}, Check Col: {col}")
          return False

      for m in range(k + 1, len(positions)):
        if positions[m][2] == subBoxPosX and positions[m][3] == subBoxPosY:
          print("In the same subbox")
          return False
      check_board[row][col] = num
  return True

import collections
def isValidHashSet(board: list[list[str]]) -> bool:
  cols = collections.defaultdict(set)
  rows = collections.defaultdict(set)
  squares = collections.defaultdict(set)

  for r in range(9):
    for c in range(9):
      if board[r][c] == ".":
        continue

      if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
        return False
      
      cols[c].add(board[r][c])
      rows[c].add(board[r][c])
      squares[(r // 3, c // 3)].add(board[r][c])
  
  return True




board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidHashSet(board))
