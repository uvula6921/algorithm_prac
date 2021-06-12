input = "abadabac"
array = [0] * 26

def find_not_repeating_character(string):
  unique_array = []
  for val in string:
    if str.isalpha(val):
      array[ord(val) - ord("a")] += 1
      
  for i, val in enumerate(array):
    if val == 1:
      unique_array.append(chr(i + ord("a")))

  for i in string:
    if i in unique_array:
      return i # 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오 -> 문자열 인덱스 순서상 첫번재 문자를 반환해야 하므로 unique_array에 있는 알파벳이면 바로 리턴해주어서 구현한다.


result = find_not_repeating_character(input)
print(result)