import sys
num, goal = map(int, sys.stdin.readline().split())
nums = []
sum_array = []
result = 0
for i in list(map(int, sys.stdin.readline().split())):
  nums.append(i)

for i in range(0, len(nums)-2):
  sum_array.append(nums[i])
  for j in range(i+1, len(nums)-1):
    sum_array.append(nums[j])
    for k in range(j+1, len(nums)):
      sum_array.append(nums[k])
      if sum(sum_array) <= goal and sum(sum_array) > result:
        result = sum(sum_array)
      sum_array.pop()
    sum_array.pop()
  sum_array.pop()
        
print(result)