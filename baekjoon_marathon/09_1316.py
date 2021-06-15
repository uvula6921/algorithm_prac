n = int(input())
count = 0
for i in range(n):
  status = True
  word = input()
  if len(word) > 1:
    stack = []
    stack.append(word[0])
    for j in range(1, len(word)):
      if stack[-1] != word[j] and not(word[j] in stack):
        stack.append(word[j])
      elif stack[-1] != word[j] and word[j] in stack:
        status = False
        break
      else:
        stack.append(word[j])
    if status:
      count += 1
  else:
    if status:
      count += 1
print(count)