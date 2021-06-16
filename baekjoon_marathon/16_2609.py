import sys
x, y = map(int, sys.stdin.readline().split())
euclide = []
euclide.extend([x, y])

while euclide[1] > 0:
  euclide[0], euclide[1] = min(euclide), max(euclide) % min(euclide)
  
print(euclide[0])
print(int(euclide[0] * (x/euclide[0]) * (y/euclide[0])))