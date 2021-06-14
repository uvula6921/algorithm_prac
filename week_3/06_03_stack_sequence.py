stack = []
sequence = []
count = 1
result = []
status = False

n = int(input())
for _ in range(n):
  num = int(input())
  while count <= num:
    stack.append(count)
    result.append('+')
    count += 1
  if stack[-1] == num:
    stack.pop()
    result.append('-')
  else:
    status = True
    
if status:
  print("NO")
else:
  for i in result:
    print(i)