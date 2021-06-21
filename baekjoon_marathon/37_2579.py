import sys
num = int(sys.stdin.readline())
stair = []
sum_list = [0] * num
for _ in range(num):
  n = int(sys.stdin.readline())
  stair.append(n)

def recursive(x):
  if x == 0:
    sum_list[0] = stair[0]
    return sum_list[0]
  elif x == 1:
    sum_list[1] = stair[0] + stair[1]
    return sum_list[1]
  elif x == 2:
    sum_list[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    return sum_list[2]
  if not sum_list[x]:
    sum_list[x] = max(recursive(x-3) + stair[x-1] + stair[x], recursive(x-2) + stair[x])
  return sum_list[x]
  
print(recursive(num-1))