import heapq

ramen_stock = 4
supply_dates = [4, 10, 15, 20]
supply_supplies = [20, 5, 10, 5]
supply_recover_k = 40

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
  
  result = 0
  heap = []
  i = 0
  while k > stock: # k와 stock이 같을때엔 딱 맞아떨어지므로 밀가루를 더 가져오지 않아도 된다.
    while i < len(dates) and dates[i] <= stock: # dates는 순차정렬되어있고, 공급이 불가능한 경우는 매개변수에 받지않는다고 가정한다.
      heapq.heappush(heap, -1 * supplies[i])
      i += 1
    
    result += 1
    stock += -1 * heapq.heappop(heap)
  return result

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))