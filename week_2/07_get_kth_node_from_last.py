class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self, value):
    self.head = Node(value)

  def append(self, value):
    cur = self.head
    while cur.next is not None:
      cur = cur.next
    cur.next = Node(value)

  def get_kth_node_from_last(self, k):
    # 1번 방법
    # cur = self.head
    # count = 1
    # while cur.next is not None:
    #   cur = cur.next
    #   count += 1
    # while count - k > 0:
    #   cur = self.head.next
    #   count -= 1
    # return cur
    
    # 1 2 3 4 5
    
    # 2번 방법
    fast = self.head
    slow = self.head
    for i in range(k):
      fast = fast.next
    
    while fast is not None:
      slow = slow.next
      fast = fast.next
      
    return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!