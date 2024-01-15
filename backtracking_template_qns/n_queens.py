
"""
example on the left: [1, 3, 0, 2]
example on the right: [2, 0, 3, 1]
"""

def is_valid_state(state):
  
  return True

def get_candidates(state):
  return []

def search(state, solutions):
  if is_valid_state(state):
    solutions.add(state)
  
  for candidate in get_candidates(state):
    state.add(candidate)
    search(state, solutions)
    state.remove(candidate)

def solve(n):
  solutions = []
  state = []
  search(state, solutions, n)
  return solutions