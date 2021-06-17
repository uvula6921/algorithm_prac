import sys
n, h = map(int, (sys.stdin.readline().split()))
trees = list(map(int, (sys.stdin.readline().split())))
start = 1
end = max(trees)
while start <= end: # 이분 탐색은 start가 end보다 더 커질때까지 진행함.
  x = (start + end) // 2
  cut_trees = 0
  for i in trees:
    if i > x:
      cut_trees += (i - x)
  if cut_trees >= h: # 자른 나무가 필요한 양보다 더 많은 채로 끝나는 경우도 생각해야함. (나무들 길이에 따라 딱 맞게 떨어지지 않을수도 있음.)
    start = x + 1
  else:
    end = x - 1
print(end)