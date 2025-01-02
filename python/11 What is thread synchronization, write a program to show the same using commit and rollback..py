import threading
import time


class BankAccount:
    def __init__(self, balance=1000):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):

        with self.lock:
            print(f"Depositing ${amount}...")
            time.sleep(1)
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance}")

    def withdraw(self, amount):
        with self.lock:
            print(f"Trying to withdraw ${amount}...")
            time.sleep(1)
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal successful! New balance: ${self.balance}")
            else:
                print("Insufficient funds! Rolling back the transaction.")
                return False
            return True


account = BankAccount(1000)


def banking_transaction():
    if not account.withdraw(1500):
        print("Transaction failed! Rolling back.")
    else:
        account.deposit(500)


threads = []
for _ in range(3):
    t = threading.Thread(target=banking_transaction)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final balance: ${account.balance}")
