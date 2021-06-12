input = "abcddba"

def is_palindrome(string):
  n = len(string)
  if n == 1:
    return True
  if string[0] != string[-1]:
    return False
  return is_palindrome(string[1:-1]) # 스스로를 리턴해야 재귀함수다.

print(is_palindrome(input))