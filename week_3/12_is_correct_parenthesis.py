s = "(())()"

def is_correct_parenthesis(string):
  stack = []
  for i in string:
    if i == "(":
      stack.append(i)
    elif i == ")":
      if len(stack):
        stack.pop()
      else:
        return False
  if len(stack) == 0:
    return True
  else:
    return False

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!