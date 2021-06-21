import sys
num = int(sys.stdin.readline())
length = len(str(num))

def func(x):
  if x > 18:
    for i in range(x-(9*length), x):
      sum = 0
      for j in str(i):
        sum += int(j)
      if i + sum == x:
        print(i)
        return
  else:
    for i in range(1, x):
      sum = 0
      for j in str(i):
        sum += int(j)
      if i + sum == x:
        print(i)
        return
  print(0)

func(num)