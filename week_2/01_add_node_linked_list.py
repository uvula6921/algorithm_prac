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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
      i = 0
      cur = self.head
      while i < index:
        cur = cur.next
        i += 1
      return cur
      
    def add_node(self, index, value): 
      # index-1과 index의 연결을 끊기 위해 index를 따로 변수 next_node에 저장
      # index-1의 next에 new_node를 저장
      # new_node의 next에 next_node를 저장
      new_node = Node(value)
      if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
      node = self.get_node(index-1)
      next_node = node.next
      node.next = new_node
      new_node.next = next_node
      
    def delete_node(self, index):
      if index == 0:
        self.head = self.head.next
        return
      node = self.get_node(index-1)
      node.next = node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(10)
linked_list.append(15)
# 3 - 5 - 12 - 10 - 15
linked_list.add_node(0, 3)
linked_list.delete_node(1)
print(linked_list.print_all())