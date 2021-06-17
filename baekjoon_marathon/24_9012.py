import sys
n = int(sys.stdin.readline())
for _ in range(n):
  stack = []
  status = True
  string = sys.stdin.readline()
  for s in string:
    if s == '(':
      stack.append(s)
    elif s == ')':
      if len(stack):
        stack.pop()
      else:
        print("NO")
        status = False
        break
  if len(stack) > 0 and status:
    print("NO")
  elif len(stack) == 0 and status:
    print("YES")