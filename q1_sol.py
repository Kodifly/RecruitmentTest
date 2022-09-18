def find_factorial_sum(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print("The factorial is: ", fact)
    
    sum = 0
    for x in str(fact):
        sum += int(x)
    print("The sum of digits of factorial is: ", sum)


n = 100
find_factorial_sum(n)
