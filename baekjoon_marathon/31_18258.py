import sys
n = int(sys.stdin.readline())
from collections import deque
queue = deque()
result = []

for i in range(n):
  input = sys.stdin.readline().split()
  x = input[0]
  if len(input) > 1:
    y = int(input[1])
  
  if x == 'push':
    queue.append(y)
  elif x == 'pop':
    if len(queue):
      result.append(queue.popleft())
    else:
      result.append(-1)
  elif x == 'size':
    result.append(len(queue))
  elif x == 'empty':
    if len(queue):
      result.append(0)
    else:
      result.append(1)
  elif x == 'front':
    if len(queue):
      result.append(queue[0])
    else:
      result.append(-1)
  elif x == 'back':
    if len(queue):
      result.append(queue[-1])
    else:
      result.append(-1)
      
for r in result:
  print(r)