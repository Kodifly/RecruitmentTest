## Add code below with answer clearly stated
def factorial(n):
    if n==1:
        return 1
    else:
        temp = 1
        for i in range(1, n):
            temp *= i
        return temp

def sum_factorial(n):
    if n < 1:
        print("Invalid Value!!!")
        return None
    if n == 1:
        return 1
    else:
        fact_n = factorial(n)
        temp = 0
        for i in str(fact_n):
            temp += int(i)
        return temp

print("The sum of 100! is ", sum_factorial(100))