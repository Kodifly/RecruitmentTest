class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		first = self.head
		second = self.head

		for i in range(n):
			second = second.next
		
		while(second.next != None):
			second = second.next
			first = first.next
		
		first.next = first.next.next
		return self.head