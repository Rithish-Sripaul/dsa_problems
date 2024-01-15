def is_valid_state(state):
  # check if it is a valid solution
  return True

# finds a list of candidates that can be used to construct the next state
def get_candidates(state):
  return []

# recursive, calls the previous two function and checks if the state is a valid state to the problem
# if it is, it records the state by doing a deepcopy of the state
def search(state, solutions):
  if is_valid_state(state):
    solutions.append(state.copy())
    # return
    # this is commented out, because if the problem requires us to have only one solution, we can exit the code as soon as we found it

  for candidate in get_candidates(state):
    state.add(cadidate)
    search(state, solutions)
    state.remove(candidate)

  
def solve():
  solutions = []
  state = ()
  search(state, solutions)
  return solutions
