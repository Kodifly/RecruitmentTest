# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        if val >= 0 and val <= 100:
            self.val = val
            self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        temp_2 = []
        while temp:
            temp_2.append(temp.val)
            temp = temp.next
        print(temp_2)
        
    def removeNthFromEnd(self, n: int):
        if n > 1:
            temp = self.head
            node_stack = []
            counter = 0
            while temp:
                counter += 1
                node_stack.append(temp)
                temp = temp.next
            next_node = node_stack.pop()
            cur_node = next_node
            if n < counter:
                for i in range(n-1):
                    next_node = cur_node
                    cur_node = node_stack.pop()
                node_stack.pop().next = next_node
        
    def make_ll(self, num_list):
        node_stack = []
        if len(num_list) <= 30 :
            for i in val:
                cur_node = ListNode(i)
                ll.head = cur_node if (ll.head == None)  else ll.head
                node_stack.append(cur_node)
            
            cur_node = None
            next_node = node_stack.pop()
            for i in range(len(node_stack)):
                cur_node = node_stack.pop()
                cur_node.next = next_node
                next_node = cur_node

        
val = [1, 2, 3, 4, 5]
k = 2
ll = LinkedList()
ll.make_ll(val)

print("Input Linked list:");
ll.display()
ll.removeNthFromEnd(k)

print("\nOutput:");
ll.display()
