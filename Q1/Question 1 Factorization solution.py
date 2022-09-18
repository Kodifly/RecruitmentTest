#First we need to define varriable and then using for loop we will calulate factors .
fact= 1 
var =100
for i in range (1,var):
  fact =fact*i
  #Now we need summation of factorizarition value
  sum = 0
  temp = fact
  while (temp):
    sum =sum + (temp % 10)
    temp =int (temp/10)
    #This will provide us our answer
