# 어떤 자연수의 제곱근보다 작은 소수들로 나누어떨어지지 않으면 그 자연수는 소수이다.
# 예를 들어 17은 소수인데 17의 제곱근인 4.xxx 보다 작은 소수들 2,3로 나누어떨어지지 않으므로 17은 소수이다.
# 반면 18은 2,3 중 2,3으로 나누어떨어지므로 소수가 아니다.

number = 287
prime_list = []

for n in range(2, number + 1):
  for i in prime_list:
    if i * i > n:
      prime_list.append(n)
      break
    elif n % i == 0:
      break
  else:
    prime_list.append(n)

print(prime_list)