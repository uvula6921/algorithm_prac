# BOJ 1158

def josephus_problem(n, k):
  result_arr = []
  people_arr = list(range(1, n + 1))
  next_index = k - 1
  while people_arr:
    result_arr.append(people_arr.pop(next_index))
    if next_index != 0:
      next_index = (next_index + (k - 1)) % len(people_arr)

  print("<", ", ".join(map(str, result_arr)), ">", sep='')

n, k = map(int, input().split())
josephus_problem(n, k)