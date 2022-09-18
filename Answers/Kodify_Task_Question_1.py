#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Question 1 
# Regarding factorial and the sume of individual numbers of the result gotten from the 
# factorial of the number 


# Program will keep running till a correct number is inputed to calculate its factorial.
result = 1
choice = True
while (choice):
    user_number  = int(input("Enter a number to calculate factorial -> "))    

    if user_number < 0:    
        print(" Number is negative")    
    elif user_number == 0:
        print("1 is the factorial of 0")    
    else:    
        for i in range(1,user_number + 1):    
            result = result*i    
        print("The factorial of",user_number,"is",result)    
        choice = False

# We have the factorial in the result variable 
# Moving to move to 2nd phase

sum = 0

while result!=0:
    digit = int(result%10)
    sum += digit
    result = result/10

print("The sum of the factorial we got is --> " , sum)


# In[16]:





# In[ ]:




