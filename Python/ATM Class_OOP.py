## **OOP**
#Object Oriented Programing

class to create new Class

class Dog:
    def __init__(self, name, age, species, energy):
        self.name = name
        self.age = age
        self.species = species
        self.energy = energy

    def __str__(self):
        return "I'm a dog :D"

    def greeting(self):
        print(f"Hi my name is {self.name}! and I'm a {self.species}.")

    def eating(self, food):
        print(f"I'm eating {food}!")
        self.energy += 10
        print(self.energy)
    
    def play(self, activity):
        if activity == "sleeping":
            self.energy += 20
        if activity == "running":
            self.energy -= 25
        else:
            self.energy -= 5
        print(self.energy)

# Create instances
dog1 = Dog("Henry",3,"Pug",100)
dog2 = Dog("Burrer",22,"Golden",300)

dog1.greeting()
dog1.eating("Pizza")
dog1.play("running")

print(dog1)

### ATM Class
5 method
- deposit
- cash balance
- เช็คยอด
- changepassword
- check status

class ATM:
    def __init__(self, name, id, location, password):
        self.name = name
        self.id = id
        self.location = location
        self.password = password
        self.money = 0
        self.stm = []
    
    def __str__(self):
        print(f"ATM service of {self.name} id {self.id}")
    
    def deposit(self,money):
        self.money += money
        print(f"You have deposit {money} bath! Your all money is {self.money}.")
        self.stm.append(f"+{money}")

    def withdraw(self,money,pw):
        if pw == self.password:
            self.money -= money
            self.stm.append(f"-{money}")
            print(f"You have withdraw {money} bath! Your all money is {self.money}.")
        else:
            print("Wrong password! Plase try again")

    def check(self,pw):
        if pw == self.password:
            print(self.money, "Bath")
        else:
            print("Wrong password! Plase try again")

    def statement(self,pw):
        if pw == self.password:
            print(self.stm)
        else:
            print("Wrong password! Plase try again")
    
    def change_password(self,pw):
        if pw == self.password:
            self.password = int(input("New password "))
            print(f"Your password had change to {self.password}")
            print(self.password)
        else:
            print("Wrong password! Plase try again")

    def status(self):
        print(f"Name: {self.name} ID: {self.id} Location: {self.location}")
        if self.money >= 1000:
            print("Cool kid Rich boy :D")
        elif self.money >= 300:
            print("Happy Medium guy!")
        else:
            print("OMG your can borrow some :(")



atm1 = ATM("Mawin", 27, "BKK", 2708)
atm2 = ATM("Poom", 28, "BKK", 1111)

atm1.deposit(500)
atm1.withdraw(300,2708)

atm1.change_password(2708)

atm1.change_password(5555)

atm1.check(2708)
atm1.statement(5555)
atm1.status()

