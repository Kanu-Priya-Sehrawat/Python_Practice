# Program 4
test = int(input("Time want to check"))

while test>0:
    n = int(input("Enter the number : "))
    prime = True
    if n==2 :
        prime = True
    if n==1 :
        prime = False
    for i in range(2,n):
        if n%i == 0:
            prime = False

    if (prime):
        print("Prime no")
    else:
        print("Not a prime no")
    test = test-1