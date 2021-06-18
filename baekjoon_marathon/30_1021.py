# deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
# deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
# deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
# deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
# deque.remove(item): item을 데크에서 찾아 삭제한다.
# deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
request = list(map(int, sys.stdin.readline().split()))
queue = deque(range(1, n+1))
rotate_right = 0
rotate_left = 0

for r in request:
  if queue.index(r) < (len(queue) / 2):
    while queue[0] != r:
      queue.rotate(-1)
      rotate_left += 1
    queue.popleft()
  else:
    while queue[0] != r:
      queue.rotate(1)
      rotate_right += 1
    queue.popleft()
print(rotate_left + rotate_right)