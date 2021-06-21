import sys
num = int(sys.stdin.readline())
row = [0] * num # 인덱스가 행, 값이 열
result = 0
def validation(x):
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
      # 같은 열이거나, 대각선상에 있으면 다음 행으로 넘어갈 필요가 없어지므로 false를 줘서 recursive를 실행 안함.
      return False
  return True # 상위 행들을 모두 확인하며 하나도 false가 걸리지 않아야 비로소 true를 받을수 있음.
def recursive(x):
  global result
  if x == num:
    result += 1
  else:
    for i in range(num):
      row[x] = i
      if validation(x):
        recursive(x+1)
        
recursive(0)
print(result)