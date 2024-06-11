def asteroid_collision(asteroids):
  stack = []

  for i in range(len(asteroids) - 1, -1, -1):
    if not stack:
      stack.append(asteroids[i])
      continue
    
    if stack[-1] < 0 and asteroids[i] > 0:
      if asteroids[i] > abs(stack[-1]):
        stack.pop()
        stack.append(asteroids[i])
      elif asteroids[i] < abs(stack[-1]):
        continue
      else:
        stack.pop()
    elif stack[-1] > 0 and asteroids[i] < 0:
      if abs(asteroids[i]) > stack[-1]:
        stack.pop()
        stack.append(asteroids[i])
      elif abs(asteroids[i]) < stack[-1]:
        continue
      else:
        stack.pop()
    else:
      stack.append(asteroids[i])
  return stack[::-1]

print(asteroid_collision([5, 10, -5]))
print(asteroid_collision([8, -8]))
print(asteroid_collision([10, 2, -5]))
print(asteroid_collision([-2, -1, 1, 2]))
