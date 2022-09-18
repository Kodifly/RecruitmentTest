from typing import Optional

class ListNode:

    def __init__(self, val = 0, next = None) -> None:
        self.value = 0
        self.next = next

class Solution:

    def __init__(self) -> None:
        self.head = None
        
    def insert(self, value):
        node = ListNode(val = value)
        node.next = self.head
        node.value = value
        self.head = node
        return node

    def removeNthFromEnd(self, head : Optional[ListNode], n:int) ->Optional[ListNode]:
        start =self.head
        end = self.head

        """Finding relevant index"""
        for i in range(n):
            if end.next == None:
                print("here") 
                if i == n-1:
                    self.head = self.head.next 
            end = end.next

        """Resetting List"""
        while(end.next != None):
            end = end.next
            start = start.next
        start.next = start.next.next


        """Printing"""
        start = self.head
        while(start !=  None):
            print(start.value, " ")
            start = start.next


if __name__ == "__main__":
    list_link = Solution()
    n1 = list_link.insert(1)
    n2 =list_link.insert(2)
    n3 =list_link.insert(3)
    n4 =list_link.insert(4)
    n5 =list_link.insert(5)
    list_link.removeNthFromEnd([n1,n2,n3,n4,n5], 3)

    
