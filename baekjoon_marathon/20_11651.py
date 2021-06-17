# import sys
# n = int(sys.stdin.readline())

# dict = {}
# for _ in range(n):
#   location = list(map(int, sys.stdin.readline().split()))
#   x = location[0]
#   y = location[1]
  
#   if y in dict.keys():
#     dict[y].append(x)
#   else:
#     dict[y] = []
#     dict[y].append(x)

# dict = sorted(dict.items(), key = lambda x: x[0])
# for i in dict:
#   i[1].sort()
#   for j in i[1]:
#     print(j, i[0])

import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
  array.append(list(map(int, sys.stdin.readline().split())))
array.sort(key=lambda x: (x[1], x[0])) # 비교할 아이팀의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 된다.
for i in array:
  print(i[0], i[1])