import sys
n = sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
if len(num_list) == 1:
  print(num_list[0] ** 2)
else:
  print(min(num_list) * max(num_list))