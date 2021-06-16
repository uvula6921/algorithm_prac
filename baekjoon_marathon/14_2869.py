import sys
A, B, Y = map(int, sys.stdin.readline().split())

if (Y - A) % (A - B) != 0:
  print(int((Y - A) // (A - B) + 2))
else:
  print(int((Y - A) // (A - B) + 1))