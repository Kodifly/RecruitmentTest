#!/usr/bin/env python
# coding: utf-8

# In[31]:


## Node Class
## A typical node in the list
class Node:
    def __init__(self, value):
        self.value =value
        self.next = None   ## this is the pointer to the next Node


# In[59]:



# Our List class with basic functions for adding and deleteing nodes.

class MyLinkedList:
    
    def __init__(self):   ## we initialzie the list with an empty head pointer as no nodes are present
        self.head = None
        
    def add(self , value): ## To add a new node to the list
        
        next_node = Node(value)  ## creating a new node with some value
        next_node.next =self.head    ## assigning its next pointer to point to the head of the top node of the list
        self.head = next_node     ## assiging the header pointer to the newly created node
        
        
    def Delete(self, index):  ## To delete the nTH from the end of the list.   
        
        # We will use two pointers to achiece this
        
        
        first_pointer = self.head    ## this pointer will be used to point to the head of the list
        
        second_pointer = self.head   ## this will be used to point to the nth node that we want to delete
        
        
        for i in range(index): ## run the loop till the required index
            #print("i --> " , i)
            #print("first-->", first_pointer.value)
            #print("second-->",second_pointer.value)
            
            # If count of nodes in the
            # given list is less than 'index (position of node for deletion)'
            if(second_pointer.next == None):
                
                # If index = n then
                # delete the head node
                if(i == index - 1):
                    self.head = self.head.next
                return self.head
            
            #print("2nd , second_pointer" , second_pointer)
            second_pointer = second_pointer.next

        while(second_pointer.next != None):
            second_pointer = second_pointer.next
            first_pointer = first_pointer.next

        first_pointer.next = first_pointer.next.next

    def printLinkedList(self): ## print the whole list
        position = self.head
        while(position):
            print(" %d " % (position.value), end=" ")
            position = position.next
  
        


# In[ ]:





# In[58]:


# CHECK THE WORKING OF THE CODE

#Creating and filling the list with values
llist = MyLinkedList()

llist.add(10)
llist.add(20)
llist.add(30)
llist.add(40)
llist.add(50)
  
print("Created Linked List: ")
llist.printLinkedList()

llist.Delete(3)

print("\nLinked List after Deletion at position 3 from end -->  ")
llist.printLinkedList()


# In[ ]:




