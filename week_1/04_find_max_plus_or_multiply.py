input = [0,1, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
  total = 0
  for val in array:
    if val <= 1 or total <= 1: # 0일떄와 1일때는 곱하기보다 더하기가 더 값을 키운다
      total += val
    else:
      total *= val
  return total


result = find_max_plus_or_multiply(input)
print(result)