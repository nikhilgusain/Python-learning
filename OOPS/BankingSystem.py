from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, name, balance=0 ):
        self.__balance = balance
        self.name = name
    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.name
    def set_balance(self, balance):
        self.__balance = balance
    def add_money(self, ammount):
        self.__balance += ammount
        print(f"{self.name} deposited {ammount}")

    def __str__(self):
        return (f"Name -- {self.name}\nBalance -- {self.__balance}")
    
class SavingsAccount(Account):
    def withdraw(self, ammount):
        if self.get_balance() < ammount:
            print("❌ Insufficient Balance")
            return
        self.set_balance(self.get_balance() - ammount)
        print("✅ Withdrawal Success")
class CurrentAccount(Account):
    def withdraw(self, ammount):
        
        fee = 10
        total_ammount = ammount + fee
        if self.get_balance() < total_ammount:
            print("❌ Insufficient Balance")
            return
        self.set_balance(self.get_balance() - total_ammount)
        print("$10 widthdrwal fee\n✅ Withdrawal success")



acc = Account("Alice", 5000)

print(acc)