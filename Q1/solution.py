## Add code below with answer clearly stated

def factorial_sum(n):

    if n == 1:
        return 1

    return n * factorial_sum(n-1)


if __name__ == "__main__":

    n = 10
    res = factorial_sum(n)

    sum_digits = 0

    for i in str(res):

        sum_digits += int(i)

    print(sum_digits)

#648 is the answer of sum of digits of 100!.
