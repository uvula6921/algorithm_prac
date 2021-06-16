import sys
x, y = map(int, sys.stdin.readline().split())
y += 1

prime_list = [True] * y
prime_list[0] = False
prime_list[1] = False
int_sqrt = int((y-1) ** 0.5)
for n in range(2,int_sqrt+1):
  if prime_list[n] == True:
    for m in range(n*2, y, n):
      prime_list[m] = False
      
for i in range(x, len(prime_list)):
  if prime_list[i]==True:
    print(i)