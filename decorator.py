def fib(n):
    fib_ser = []
    a,b = 0,1
    while a<= n:
        fib_ser.append(a)
        a,b = b,a+b
    print(fib_ser)

def add(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print('sum=',sum)

fib(12)
add(10)
