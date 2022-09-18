## Add code below with answer clearly stated

#TASK 1
# Finding factorial using recursive calls

def calculate_factorial(num):
    if num != 1:
        return num * calculate_factorial(num-1)
    else:
	    return 1 #Base Case

# Printing factorial of 100
fact_100 = calculate_factorial(100)
print('Factorial of 100 is : ',fact_100)

#TASK 2
#sum of digits in fact_100 using division

sum_fact = 0		
while (fact_100 != 0):
    sum_fact = sum_fact + (fact_100 % 10) #adding remainder
    fact_100 = fact_100//10 # integeral division clip last digit
print(sum_fact)
                