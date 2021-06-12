finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_existing_target_number_binary(target, array):
  finding_numbers.sort() # 이진 탐색을 하기 위해선 반드시 배열을 오름차순 정렬해놔야 한다.
  while array:
    half = len(array) // 2
    if array[half] == target:
      return True
    elif array[half] > target:
      array = array[:half]
    else:
      array = array[half+1:]
  return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)