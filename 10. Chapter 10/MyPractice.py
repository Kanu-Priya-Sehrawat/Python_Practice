class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary ):
        self.name = name
        self.salary = salary
        print(f"Programmer {self.name} instance is created !!")
     
    def getDetails(self):
        print(f"The name of the programmer is {self.name} working in {self.company} and salary is {self.salary}")

kanu = Programmer("Kanu", 100000000)
kanu.getDetails()
karan = Programmer("Karan", 10000000)    
karan.getDetails()