# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass
    def creat_LList(self, arr: list) -> ListNode:
        if arr == []:
            print("Invalid Entry")
        else:
            head = ListNode(arr[0])
            for i in arr[1:]:
                last_node = head
                while(last_node.next):
                    last_node = last_node.next
                last_node.next = ListNode(i)
            return head

    def display(self, head: ListNode) -> None:
        temp = head
        print("[", end="")
        while (temp):
            if temp.next:
                print(temp.val, end=",")
            else:
                print(temp.val, end="")
            temp = temp.next
        print("]")

    def remove_nth_value(self, head: ListNode, n: int) -> ListNode:
        if n < 1:
            print("Invalid Entry")
        else:
            counter = 1
            temp = head
            while counter < n - 1:
                temp = temp.next
                counter += 1
            if temp == None:
                return head
            temp.next = temp.next.next
        return head
    
    def reverse_LL(self, head: ListNode) -> ListNode:
        current_node = head
        prev = None
        while current_node:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp
        return prev


    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return []
        else:
            head_node = self.reverse_LL(head)
            head_node = self.remove_nth_value(head_node, n)
            head_node = self.reverse_LL(head_node)
            return head_node
        
if __name__ == '__main__':
    ll = Solution()
    list = [1, 2, 3, 4, 5]
    head_node = ll.creat_LList(list)
    ll.display(head_node)
    head_node = ll.removeNthFromEnd(head_node, 2)
    ll.display(head_node)
    list = [1]
    head_node = ll.creat_LList(list)
    ll.display(head_node)
    head_node = ll.removeNthFromEnd(head_node, 1)
    ll.display(head_node)
    list = [1, 2]
    head_node = ll.creat_LList(list)
    ll.display(head_node)
    head_node = ll.removeNthFromEnd(head_node, 1)
    ll.display(head_node)
