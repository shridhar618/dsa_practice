def fib(num):
    if num<1:
        return num
    a=0
    b=1
    for i in range(num):
        sum=a+b
        a=b
        b=sum
    return b

num=int(input("Enter Range:"))
result=fib(num)
print(result)