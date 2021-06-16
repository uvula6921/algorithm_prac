import sys
num = int(sys.stdin.readline())

i = 0
count = 0
while count < num:
  i += 1
  if '666' in str(i):
    count += 1
print(i)