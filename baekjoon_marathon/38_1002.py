import sys
num = int(sys.stdin.readline())
for _ in range(num):
  x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
  
  r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
  m = max(r1, r2, r)
  array = [r1, r2, r]
  array.remove(m) 
  # 원이 닿는지 안닿는지는 r1, r2, r 중 가장 큰 값과 나머지 두 개의 대소관계에 따라 결정된다.
  # 굳이 r이 가장 길때, r2가 가장 길때 이런 식으로 세분화하지 않아도 된다.
  sum_array = sum(array)
  
  if r == 0 and r1 == r2:
    print(-1)
  else:
    if m > sum_array: # 두 원이 서로 떨어져있거나, 한 원이 다른 원을 품고있을때
      print(0)
    elif m == sum_array: # 외접, 내접
      print(1)
    elif m < sum_array: # 두 점에서 만남
      print(2)