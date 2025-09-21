def is_palindrome(num):
    num=str(num)
    return num==num[::-1]
    
num=int(input("enter a number:"))
result=is_palindrome(num)
print(result)