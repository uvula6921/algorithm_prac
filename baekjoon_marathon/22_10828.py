import sys
result_list = []
for _ in range(int(sys.stdin.readline())):
  request = list(sys.stdin.readline().split())
  if request[0] == 'push':
    result_list.append(request[1])
  elif request[0] == 'pop':
    print(result_list.pop() if len(result_list) else -1)
  elif request[0] == 'size':
    print(len(result_list))
  elif request[0] == 'empty':
    print(0 if len(result_list) else 1)
  elif request[0] == 'top':
    print(result_list[-1] if len(result_list) else -1)