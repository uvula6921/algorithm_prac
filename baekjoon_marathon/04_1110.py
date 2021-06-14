first_num = input()
count = 0
num = "0"

while True:
  sum = 0
  if count == 0:
    num = first_num
  for i, v in enumerate(num):
    sum += int(v)
    if i == (len(num) - 1):
      num = v + str(sum)[-1]
  count += 1
  if int(first_num) == int(num):
    break
print(count)