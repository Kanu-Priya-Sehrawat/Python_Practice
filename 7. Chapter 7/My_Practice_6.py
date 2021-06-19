t = int(input("Test case : "))
i = 0
while i<t:
    n = int(input("Enter the number : "))
    fact = 1
    i = 1
    for i in range(i,n+1):
        fact = fact*i
    print(fact)