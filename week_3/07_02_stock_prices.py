from collections import deque

def solution(prices):
  prices = deque(prices)
  result = []
  
  for _ in range(len(prices)-1):
    price = prices.popleft()
    count = 0

    for p in prices:
      if price > p: # 현재 가격이 다음 시간초보다 작아지면 1초간만 더 가격이 지속했다고보고 가격이 떨어졌으므로 break
        count += 1
        break
      else:
        count += 1
              
      result.append(count)
  result.append(0)
  return result