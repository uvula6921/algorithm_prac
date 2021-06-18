seat_count = 10
vip_seat_array = [2, 6, 9]

dict = {
  1: 1,
  2: 2
}

def fibo(n, memo):
  if n in memo:
    return memo[n]
  memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
  return fibo(n-1, memo) + fibo(n-2, memo)

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
  multi = 1
  for i in range(len(fixed_seat_array)-1):
    multi *= fibo(fixed_seat_array[i+1]-fixed_seat_array[i]-1, dict)
  multi *= fibo(fixed_seat_array[0]-1, dict) * fibo(total_count - fixed_seat_array[-1], dict)
  return multi

# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))