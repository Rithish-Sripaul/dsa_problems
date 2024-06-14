def asteroid_collision(asteroids):
  stack = []
  for ast in asteroids:
    while len(stack) and ast < 0 and stack[-1] > 0:
      if stack[-1] == -ast:
        stack.pop()
        break
      elif stack[-1] < -ast:
        stack.pop()
        continue
      else:
        break
    else:
      stack.append(ast)
  return stack

print(asteroid_collision([5, 10, -5]))
print(asteroid_collision([8, -8]))
print(asteroid_collision([10, 2, -5]))
print(asteroid_collision([-2, -1, 1, 2]))
print(asteroid_collision([-2, 2, -1, -2]))
