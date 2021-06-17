import sys

def hanoi(n, start, end, assist):
  if n == 1:
    print(start, end)
  else:
    hanoi(n-1, start, assist, end)
    print(start, end)
    hanoi(n-1, assist, end, start)
    
n = int(sys.stdin.readline())
print(2**n - 1)
hanoi(n, 1, 3, 2)