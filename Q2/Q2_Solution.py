class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to add node at the end
    def create(self, x):
 
        new_node = Node(x)
 
        if self.head is None:
            self.head = new_node
            return
 
        last = self.head
        while last.next:
            last = last.next
 
        last.next = new_node
 
    # This function prints contents of linked
    # list starting from the given node
    def display(self):
        temp = self.head
 
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
 
# Function to remove nth node from last
def removeNthFromEnd(head, k):
     
    # the function uses two pointer method
    first = head
    second = head
    count = 1
    while count <= k:
        second = second.next
        count += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
 
# Driver code
 
# val list contains list of values
val = [1, 2, 3, 4, 5]
k = 2
ll = LinkedList()
for i in val:
    ll.create(i)
 
print("Linked list before modification:");
ll.display()
 
removeNthFromEnd(ll.head, k)
 
print("\nLinked list after modification:");
ll.display()
