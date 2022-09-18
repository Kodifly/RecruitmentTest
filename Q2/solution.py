# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev_node = head
        next_node = head

        count = 0

        while prev_node.next != None:

            count += 1

            if prev_node.next.value == value:
                next_node = next_node.next.next
                break

            prev_node = prev_node.next
            next_node = next_node.next

        if head.value == value:
            node = head
            head = head.next
            del node
            
        else:
             del_node = prev_node.next
             next_node = prev_node.next.next
             del del_node
            
        return head
