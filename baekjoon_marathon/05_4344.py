iteration = int(input())

while iteration > 0:
  score_array = list(map(int, input().split()))
  del score_array[0]
  iteration -= 1
  over_avg_count = 0
  
  average = sum(score_array) / len(score_array)
  for i in score_array:
    if i > average:
      over_avg_count += 1
  print(f'{((over_avg_count / len(score_array)) * 100):.3f}%')