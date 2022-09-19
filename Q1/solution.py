## Add code below with answer clearly stated
def factorial(num):
    if num==1:
        return 1
    else:
        var = 1
        for i in range(1, num):
            var *= i
        return var
## The above function will be used to calculate the factorial of given number.
def sum_factorial(num):
    if num < 1: #if given number is negative or zero  its a invalid number
        print("Invalid Value!!!")
        return None
    if num == 1:
        return 1
    else:
        fact_num = factorial(n) # calculate the factorial of tgiven number
        var = 0 # initiallize a veriable
        for i in str(fact_num): #First convert the number to string to iteratively choose one digit from the output
            var += int(i) # add that number to the Var that is initially zero
        return var

print("The sum of factorial is ", sum_factorial(100))
