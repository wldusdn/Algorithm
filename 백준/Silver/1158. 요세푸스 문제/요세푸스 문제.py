# BOJ 1158
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self,value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur_index += 1
            cur = cur.next
        return cur

def josephus_problem(n, k):
   linked_list = LinkedList(1)
   for i in range(2,n+1):
       linked_list.append(i)
   linked_list.get_node(n-1).next = linked_list.head

   result = []
   last = linked_list.get_node(n-1)
   for i in range(n):
       for _ in range(k-1):
           last = last.next
       num = last.next
       result.append(num.data)
       last.next = num.next
   print("<" + ", ".join(map(str, result)) + ">")

n, k = map(int, input().split())
josephus_problem(n, k)