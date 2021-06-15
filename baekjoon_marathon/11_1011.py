import math

num = int(input())
result = []
for i in range(num):
  start, finish = map(int, input().split())
  distance = finish - start
  sqrt_distance = math.sqrt(distance)
  if sqrt_distance - int(sqrt_distance) > 0.5:
    result.append(2 * int(sqrt_distance) + 1)
  elif sqrt_distance == int(sqrt_distance):
    result.append(2 * int(sqrt_distance) -1)
  else:
    result.append(2 * int(sqrt_distance))
    
for i in result:
  print(int(i))