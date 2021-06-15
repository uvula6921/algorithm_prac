weight = int(input())
five_count = weight // 5
three_count = 0
result = -1
for x in range(five_count, -1, -1):
  if (weight - (5 * x)) % 3 == 0:
    result = x + ((weight - (5 * x)) / 3)
    break
print(int(result))