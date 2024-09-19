class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}. I will use python to be an AI Engineer.")

# Creating an instance of the Person class
person = Person("Felix Kihima Livaha", 23, "Male")

# Call the introduce method to display  information
person.introduce()