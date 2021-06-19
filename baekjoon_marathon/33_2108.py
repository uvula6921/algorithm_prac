import sys
import collections

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
  nums.append(int(sys.stdin.readline()))
nums.sort()

# 산술평균  
print(round(sum(nums) / len(nums)))

# 중앙값
print(nums[len(nums)//2])

# 최빈값
dict = collections.Counter(nums).most_common()
if len(dict) >= 2 and dict[0][1] == dict[1][1]:
  print(dict[1][0])
else:
  print(dict[0][0])

# 범위
print(nums[-1]-nums[0])