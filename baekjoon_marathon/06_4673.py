nums = []
for num in range(1, 10001):
  sum = 0
  for x in str(num):
    sum += int(x)
  nums.append(sum + num)
  
result_set = set(list(range(1, 10001))) - set(nums)
result_list = list(result_set)
result_list.sort()
for n in result_list:
  print(n)