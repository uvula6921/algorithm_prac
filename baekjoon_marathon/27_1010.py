# 순서에 상관없이 두가지 조합을 뽑으면 되므로 kCn 문제

import sys
x = int(sys.stdin.readline())
for _ in range(x):
  k, n = (map(int, sys.stdin.readline().split()))
  son = 1
  mother = 1
  for i in range(n, n-k, -1):
    son *= i
  for i in range(k, 1, -1):
    mother *= i
    
  print(int(son / mother))