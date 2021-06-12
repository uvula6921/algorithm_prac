input = "0101010"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
  change_to_zero_count = 0
  change_to_one_count = 0
  for i in range(len(string)-1):
    if int(string[i+1]) - int(string[i]) == 1:
      change_to_zero_count += 1
    elif int(string[i+1]) - int(string[i]) == -1:
      change_to_one_count += 1
  
  if int(string[0]) - int(string[-1]) == 1:
    change_to_zero_count += 1
  elif int(string[0]) - int(string[-1]) == -1:
    change_to_one_count += 1
      
  return min(change_to_one_count, change_to_zero_count)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)