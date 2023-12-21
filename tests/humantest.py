class Human():
    def __init__(self,name = "no name",age=0,nationality="no nationality",gender="no gender"):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender

    def speak(self):
        print(f"Hello my name is {self.name}")


bob = Human()
print("Object attributes:")
print(f"{bob.name}\n{bob.age}\n{bob.nationality}\n{bob.gender}")
print("*******")
bob.speak()