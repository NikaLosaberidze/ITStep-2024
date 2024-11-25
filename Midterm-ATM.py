import json, os, re
from time import sleep
from datetime import datetime



def makeRecord(customer):
    with open(f"transactions/{customer.name}-{customer.customerId}.json","w",encoding='utf-8') as file:
        json.dump(customer.to_dict(),file,indent=4)





class Customer:
    customerId = 1
    def __init__(self, name, id, deposit=0) -> None:
        if deposit < 0:
            raise ValueError("deposit Must Be Greater Or Equal Than 0\n")
        if not re.match(r"^\d{11}$", id):
            raise ValueError("ID Must Be 11 Digits Long")


        self.__name = name
        self.__id = id
        self.__balance = deposit
        self.customerId = Customer.customerId
        self.__transactions = []
        Customer.customerId += 1

        if deposit > 0:
            self.__transactions.append(f"{deposit} GEL Was Deposited On Your Account | Date : {datetime.now()}")

        

        with open(f"transactions/{self.__name}-{self.customerId}.json","w",encoding='utf-8') as file:
            json.dump(self.to_dict(),file,indent=4)


    def to_dict(self):
        return {
                "Name" : self.__name,
                "ID" : self.__id,
                "Balance" : self.__balance,
                "CustomerID" : self.customerId,
                "Transactions" : self.__transactions
               }
    


    def withdraw(self, amount):

        # Checking Validation
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError("Amount Must Be A Positive Number, Greater Than 0!\n")
        
        if self.__balance < amount:
            raise ValueError("You Do Not Have Enough Money On Your Account.\n")
        
        sleep(0.5)
        print("\nProcessing...\n")
        sleep(1)

        self.__balance -= amount

        print(f"{amount} GEL Is Withdrawed From Account\n")

        self.__transactions.append(f"{amount} GEL Was Withdrawed From Your Account | Date : {datetime.now()}")
        makeRecord(self)



    
    def deposit(self, amount):

        # Checking Validation
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError("Amount Must Be A Positive Number, Greater Than 0!\n")
        
        self.__balance += amount

        sleep(0.5)
        print("Processing...\n")
        sleep(1)

        print(f"{amount} GEL Is Deposited On Your Account")

        self.__transactions.append(f"{amount} GEL Was Deposited On Your Account | Date : {datetime.now()}")
        makeRecord(self)
        

    
    def checkBalance(self):
        sleep(0.5)
        print("Checking...")
        sleep(0.5)

        print(f"Your Balance Is: {self.__balance} GEL\n")
        




    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def transactions(self):
        return self.__transactions
    
    @property
    def balance(self):
        return self.__balance
    





if __name__ == "__main__":
    os.makedirs("transactions",exist_ok=True)
    
    customer1 = Customer("Nika Losaberidze","50001152326",2000)
    customer2 = Customer("Luka Losaberidze","12123123123",1000)
    customer3 = Customer("Vaxo Vaxoashvili","20523245211")

    customer1.deposit(2334)
    customer2.withdraw(254)
    customer3.deposit(20)