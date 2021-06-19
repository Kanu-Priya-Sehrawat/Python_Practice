n = int(input("Enter the number "))
l =  []
for i in range(1, 11):
    l.append(str(n)+" * " + str(i) + " = " + str(n*i))
print(l)
l.reverse()
print(l)
