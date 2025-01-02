class Parent1:
    def __init__(self):
        print("Parent1 constructor called")

    def show(self):
        print("This is the show method of Parent1")


class Parent2:
    def __init__(self):
        print("Parent2 constructor called")

    def display(self):
        print("This is the display method of Parent2")


class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()  # Calls the constructor of the first parent class (Parent1)
        Parent2.__init__(self)  # Explicitly calls the constructor of the second parent class (Parent2)
        print("Child constructor called")

    def show_all(self):
        super().show()  # Calls the show method from Parent1 using super()
        super().display()  # Calls the display method from Parent2 using super()


# Creating an object of Child class
child_obj = Child()
child_obj.show_all()
