def factorial(number):
  if number == 1:
    return 1
  else:
    return (number*factorial(number-1)) # return the factorial of a number

def sum_factorial_100(n):

  factorial_100 = factorial(n)
  sum = 0
  for i in range(len(str(factorial_100))): # iterating through result of factorial
    sum+= int(str(factorial_100)[i]) #adding the result to sum variable
  return sum
