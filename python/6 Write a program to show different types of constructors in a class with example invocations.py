class Employee:

    # Constructor with default values and handling multiple scenarios
    def __init__(self, name="Unknown", age=0, other=None):
        if isinstance(other, Employee):
            # Copy constructor behavior
            self.name = other.name
            self.age = other.age
            print("Copy constructor called")
        else:
            self.name = name
            self.age = age
            print("Constructor with parameters or default values called")

    # Method to display employee details
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating objects using different constructor types

# Using constructor with default values
employee1 = Employee()
employee1.display_details()

# Using constructor with parameters
employee2 = Employee("Alice", 28)
employee2.display_details()

# Using constructor with default values again
employee3 = Employee()
employee3.display_details()

# Using copy constructor (simulated)
employee4 = Employee(employee2)
employee4.display_details()
