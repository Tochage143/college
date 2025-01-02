import pymongo

# Connect to MongoDB server and database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["company"]
collection = db["employees"]

# 1. Create: Insert a new employee into the collection
def create_employee():
    employee = {
        "name": "John Doe",
        "age": 30,
        "position": "Software Developer",
        "salary": 60000
    }
    result = collection.insert_one(employee)
    print(f"Employee added with ID: {result.inserted_id}")

# 2. Read: Fetch an employee by name
def read_employee(name):
    employee = collection.find_one({"name": name})
    if employee:
        print("Employee Found:", employee)
    else:
        print(f"Employee with name {name} not found.")

# 3. Update: Update the salary of an employee
def update_employee(name, new_salary):
    result = collection.update_one(
        {"name": name},
        {"$set": {"salary": new_salary}}
    )
    if result.modified_count > 0:
        print(f"Employee {name}'s salary updated to {new_salary}.")
    else:
        print(f"No employee found with the name {name}.")

# 4. Delete: Delete an employee from the collection
def delete_employee(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Employee {name} deleted.")
    else:
        print(f"No employee found with the name {name}.")

# Example usage
create_employee()  # Create employee
read_employee("John Doe")  # Read employee by name
update_employee("John Doe", 75000)  # Update employee's salary
read_employee("John Doe")  # Read employee to verify update
delete_employee("John Doe")  # Delete employee
