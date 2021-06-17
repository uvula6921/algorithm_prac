import sys
n = int(sys.stdin.readline())
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  euclide = sorted([x, y], reverse=True)
  while euclide[1] > 0:
    euclide[0], euclide[1] = euclide[1], euclide[0] % euclide[1]
  print(int(x * y / euclide[0]))