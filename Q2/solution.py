# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if self.head is None:
            return
        index = 0
        current = self.head

        while current.next and index < n:
            previous = current
            current = current.next
            index += 1

        if index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next

