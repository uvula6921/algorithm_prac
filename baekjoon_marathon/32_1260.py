import sys
node_count, line_count, start_node = map(int, sys.stdin.readline().split())
graph = {}
dfs_visited = []
bfs_visited = []
dfs_stack = [start_node]
bfs_queue = [start_node]
for _ in range(line_count):
  line = list(map(int, sys.stdin.readline().split()))
  
  if line[0] in graph:
    graph[line[0]].append(line[1])
  else:
    graph[line[0]] = [line[1]]
    
  if line[1] in graph:
    graph[line[1]].append(line[0])
  else:
    graph[line[1]] = [line[0]]

# dfs
if start_node not in graph:  # 시작 노드가 아무것도 연결이 안되어있을수 있는 경우를 예외처리 해야한다.
  print(start_node)
else:
  for x in graph:
    graph[x].sort(reverse=True)

  while len(dfs_stack):
    cur = dfs_stack.pop()
    if cur not in dfs_visited:
      dfs_visited.append(cur)
    for i in graph[cur]:
      if i not in dfs_visited:
        dfs_stack.append(i)

  for x in dfs_visited:
    if x == dfs_visited[-1]:
      print(x)
    else:
      print(x, end=' ')

# bfs
if start_node not in graph: # 시작 노드가 아무것도 연결이 안되어있을수 있는 경우를 예외처리 해야한다.
  print(start_node)
else:
  for x in graph:
    graph[x].sort()
    
  while len(bfs_queue):
    cur = bfs_queue.pop(0)
    if cur not in bfs_visited:
      bfs_visited.append(cur)
    for i in graph[cur]:
      if i not in bfs_visited:
        bfs_queue.append(i)

  for x in bfs_visited:
    if x == bfs_visited[-1]:
      print(x, end='')
    else:
      print(x, end=' ')