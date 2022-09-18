# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #used a double pointer approach
    fast = head         #both pointer representing the head
    slow = head
 
    for i in range(n):   #iterating the fast pointer n times
      fast = fast.next
            
    if not fast:
      return head.next
 
    while fast.next:    #iterating the both pointer until fast reaches the end
      fast = fast.next
      slow = slow.next
       
    slow.next = slow.next.next  # replacing the next node of slow pointer with the next to next node.
    return head

        
        
