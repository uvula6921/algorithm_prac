# 에라토스테네스의 체 (소수 리스트를 알아낼때 좋음)
# while True:
#   start = int(input())
#   if start == 0:
#     break
  
#   n = start * 2 + 1
#   sieve = [True] * n
#   m = int(n ** 0.5)
#   for i in range(2, m + 2):
#     if sieve[i] == True:
#       for j in range(2*i, n, i):
#         sieve[j] = False
#   print(len(list(filter(lambda x: x == True, sieve[start+1:]))))

# 내 코드 (소수인지 아닌지 알아낼때 좋음)
# while True:
#   start = int(input())
#   if start == 0:
#     break
  
#   finish = 2 * start
#   prime_list = []
#   for num in range(2, finish+1):
#     for prime in prime_list:
#       if prime * prime > num:
#         prime_list.append(num)
#         break
#       else:
#         if num % prime == 0:
#           break
#     else:
#       prime_list.append(num)    
#   result = list(filter(lambda x: x > start, prime_list))
#   print(len(result))


def prime_list(n):
  seive = [True] * n
  m = int(n ** 0.5)
  for i in range(2, m+1):
    if seive[i] == True:
      for j in range(i*2, n, i):
        seive[j] = False
  return [i for i in range(2, n) if seive[i]==True]
  
print(prime_list(10))