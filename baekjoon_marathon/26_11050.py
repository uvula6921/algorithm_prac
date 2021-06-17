# 이항계수란...
# n개의 요소를 순서없이 k개 뽑을때의 조합 수이다.
# nCk

import sys
n, k = (map(int, sys.stdin.readline().split()))
son = 1
mother = 1
for i in range(n, n-k, -1):
  son *= i
for i in range(k, 1, -1):
  mother *= i
  
print(int(son / mother))