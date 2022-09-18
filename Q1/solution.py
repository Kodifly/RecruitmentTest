## Add code below with answer clearly stated
# TO CALCULATE FACTORIAL I HAVE USED RECURSION BUT I COULD HAVE ALSO USED FOR LOOP 
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
      
#taking factorial of 100
fact_100=factorial(100)
print('factorial of 100 : ',fact_100)

my_int = fact_100

#spliting the result into individual digits using comprehension
fact_100 = [int(x) for x in str(fact_100)]

print(fact_100)

#taking sum of the digits in the number 100! using the sum function
sum_fact_100=sum(fact_100,0)

print('the sum of the digits in the number 100! is : ',sum_fact_100)

'''
when this code is run, it gives the following output

factorial of 100 :  93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
[9, 3, 3, 2, 6, 2, 1, 5, 4, 4, 3, 9, 4, 4, 1, 5, 2, 6, 8, 1, 6, 9, 9, 2, 3, 8, 8, 5, 6, 2, 6, 6, 7, 0, 0, 4, 9, 0, 7, 1, 5, 9, 6, 8, 2, 6, 4, 3, 8, 1, 6, 2, 1, 4, 6, 8, 5, 9, 2, 9, 6, 3, 8, 9, 5, 2, 1, 7, 5, 9, 9, 9, 9, 3, 2, 2, 9, 9, 1, 5, 6, 0, 8, 9, 4, 
1, 4, 6, 3, 9, 7, 6, 1, 5, 6, 5, 1, 8, 2, 8, 6, 2, 5, 3, 6, 9, 7, 9, 2, 0, 8, 2, 7, 2, 2, 3, 7, 5, 8, 2, 5, 1, 1, 8, 5, 2, 1, 0, 9, 1, 6, 8, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
the sum of the digits in the number 100! is :  648

'''
