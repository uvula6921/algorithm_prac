import sys
while True:
  ex = sys.stdin.readline().rstrip()
  if ex == '.':
    break
  stack = []
  status = True
  for i in ex:
    if i == "(" or i == "[":
      stack.append(i)
    elif i == ")":
      if not len(stack):
        status = False
        print("no")
        break
      if stack[-1] == "(":
        stack.pop()
        continue
      elif stack[-1] != "(":
        status = False
        print("no")
        break
    elif i == "]":
      if not len(stack):
        status = False
        print("no")
        break
      if stack[-1] == "[":
        stack.pop()
        continue
      elif stack[-1] != "[":
        status = False
        print("no")
        break
  if status and len(stack):
    print("no")
  elif status and not len(stack):
    print("yes")