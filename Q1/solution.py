def get_factorial(number):
    """Returns Factorial of number, with trailing zeros removed because they don't contribute to the sum"""
    fact = 1
    for num in range(2, number + 1):
        fact *= num
        if num % 5 == 0:
            while fact % 10 == 0:
                fact //= 10
    return fact


def digit_sum_for(number):
    """Returns the sum of the all digits of a number"""
    total = 0
    for digit in str(number):
        total += int(digit)
    return total


factorial = get_factorial(10)
digit_sum = digit_sum_for(factorial)
print(digit_sum)
