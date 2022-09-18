#!/usr/bin/env python
# coding: utf-8

# In[11]:



## A recursive implementation of quick sort as its the go to
## algorithm for best average case time and space complexity

## Was a bit rusty about which sorting algo to use, so decided to look it up in the internet :)
## Reference https://www.programiz.com/dsa/quick-sort

def sort_array(array): 
    
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1: ## check if the array has atleast 2 values
        
        pivot = array[0] ## our base value for which we check the other values
        for x in array:
            
            ## We basically have 3 pointers moving around determining the values to swap
            
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
       
        return sort_array(less)+equal+sort_array(greater)  # Just use the + operator to join arrays
   
    else: # when we have only one element in the array, just return the array.
        return array


# In[21]:


#Question 3
# Return the median of the conjuntion of 2 sorted arrays


def Median(array):
 
    size_of_array = len(array)
    # check for even case
    if size_of_array % 2 != 0:
        return float(array[int(n/2)]) ## we can get values in decimal so we cast the result as a float
 
    return float((array[int((size_of_array-1)/2)] + array[int(size_of_array/2)])/2.0)




array1 =[]
array2 =[]

size_array=int(input("Number of elements in first array:"))
for i in range(0 , size_array):
    inp=int(input())
    array1.append(inp)
print(array1)

size_array = int(input("Number of elements in second array:"))
for i in range(0,size_array):
    inp=int(input())
    array2.append(inp)
print(array2)

joint_array = list(set(array1 + array2)) ## remove duplicates
final_array = sort_array(joint_array)
print("joint sorted array --> " , joint_array)
Median = Median(final_array)
print("Median for the 2 sorted arrays is -->", Median)


# 

# In[ ]:




