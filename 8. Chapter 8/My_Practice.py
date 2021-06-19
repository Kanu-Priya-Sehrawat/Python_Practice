def fun(n):
    if n==0:
        return 0
    else:
        print("*" * fun(n-1))
    

degree = int(input("Enter the temp : "))
print(fun(degree))
