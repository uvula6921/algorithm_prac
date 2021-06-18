class MaxHeap:
  def __init__(self):
    self.items = [None] # 완전 이진 트리는 배열로 표현할 수 있는데 0번째 인덱스는 None으로 채워서 계산이 편하게 한다.

  def insert(self, value):
    self.items.append(value)
    cur_index = len(self.items) - 1
    while cur_index > 1:
      parent_index = cur_index // 2
      if self.items[cur_index] > self.items[parent_index]:
        self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
        cur_index = parent_index
      else:
        break
    return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

# O(log(N))