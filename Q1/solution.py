# First we need to find the size of factorization for that we need to run the following program

def len_link(list):
    temp=list.head
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count
  # Then we need to factorize the number i.e 100 making loop
   fact =1 
    var= 100
    for i in range (1,var):
      fact =fact*1   
# In the second part of this we need to sum of factorization value we calculated in the case fact using while loop
  sum = 0
  temp =fact
  while (temp):
  sum= sum +(temp % 10)
  temp = int(temp/10)
  #This code will give our desired results.
  
    
