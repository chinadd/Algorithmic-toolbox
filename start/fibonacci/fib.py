#use python3 
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        fibs=[0,1]
        for i in range(2,n+1):
            fibs.append(fibs[-1]+fibs[-2])
            fibs=fibs[1:]
        return fibs[1]

n = int(input())
print(calc_fib(n))
