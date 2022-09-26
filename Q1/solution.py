## Add code below with answer clearly stated
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
def sumDigits(n):
    if(n==0):
        return 0
    mod = n%10
    return mod + sumDigits((n-mod)/10)

if __name__ == '__main__':
    i = fact(100)
    sum = sumDigits(i)
    print(i) # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    print(sum) # 675
