import math


def sumOfFac(number):
    
    value = []
    value.append(1)

    for i in range(1, number+1):
        getCalcFac(value, i)
    
    sum = 0
    for i in range(len(value)):
        sum += value[i]
    return sum


def getCalcFac(value, j ):
    carry = 0

    for i in range(len(value)):
        result  = carry + value[i] * j
        value[i] = result % 10 
        carry = result //10

    while carry != 0:
        value.append(carry % 10)
        carry = carry // 10
    

if __name__ == "__main__":
    print(str(math.factorial(100)))
    print(sumOfFac(100))
