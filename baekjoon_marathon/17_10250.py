import sys
repeat = int(sys.stdin.readline())
for _ in range(repeat):
  h, w, n = map(int, sys.stdin.readline().split())
  room = n // h + 1
  floor = n % h
  if not floor:
    floor += h
    room -= 1
  if room < 10:
    print(int(str(floor) + '0' + str(room)))
  else:
    print(int(str(floor) + str(room)))