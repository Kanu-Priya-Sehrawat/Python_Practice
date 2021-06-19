t = int(input("Testcase number : "))
i = 0
while i<t:
    n = int(input("Enter the number : "))
    for r in range(0,n):
       if r==0 or r==n-1:
           print("*"*n)
       else:
            print("*", end="")
            print(" "*(n-2), end="")
            print("*")

       
    i = i+1