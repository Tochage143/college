class Bank:
    def __init__(self, bank_name, branch, city, manager_name):
        self.bank_name = bank_name
        self.branch = branch
        self.city = city
        self.manager_name = manager_name

    def change_managername(self, new_manager_name):
        self.manager_name = new_manager_name

    def display_details(self):
        print("Bank Name:", self.bank_name)
        print("Branch:", self.branch)
        print("City:", self.city)
        print("Manager Name:", self.manager_name)


bank = Bank("ABC Bank", "Downtown", "New York", "John Doe")
bank.display_details()
bank.change_managername("Alice Smith")
bank.display_details()
