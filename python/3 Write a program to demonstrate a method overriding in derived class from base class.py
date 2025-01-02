class Animal:
    def speak(self):
        print("Animal is making a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")



# Demonstrating method overriding
animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

