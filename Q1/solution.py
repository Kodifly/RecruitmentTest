def calculate_factorial(n):
    r = 1
    while(n > 1):
        r = r*n
        n = n-1
    return r


def digit_sum(num):
    r = 0
    while(num != 0):
        r += num%10
        num = num//10
    return r


if __name__ == "__main__":

    inputNumber = 100
    factorial = calculate_factorial(inputNumber)
    result = digit_sum(factorial)
    print(f"Factorial of {inputNumber}! is: {factorial} \nand sum of digits for {inputNumber}! is: {result}")
