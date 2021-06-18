import sys
n = int(sys.stdin.readline())
stack = []
max = 0
result = []
status = True
for _ in range(n):
  num = int(sys.stdin.readline())
  if max < num:
    for j in range(max+1, num+1):
      stack.append(j)
      result.append("+")
    stack.pop()
    result.append("-")
    max = num
  else:
    if num == stack[-1]:
      stack.pop()
      result.append("-")
    else:
      status = False

if status:
  for s in result:
    print(s)
else:
  print("NO")