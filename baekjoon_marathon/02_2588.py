n = int(input())
m = input()

i = len(m)
while i > 0:
  print(n * int(m[i - 1]))
  i -= 1
  
print(n * int(m))