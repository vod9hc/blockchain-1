from datetime import date
#Class

class Customer:
    def __init__(self,customerID, customerName, customerEmail):
        self.customerID = customerID
        self.customerName = customerName
        self.customerEmail = customerEmail
    
    def getInformation(self):
        print("CustomerID: ", self.customerID, "CustomerName: ", self.customerName, "CustomerEmail: ", self.customerEmail)

    
    def createSalesOrder(self):
        print("Creating sales order")

    @classmethod
    def getBOD(cls, customerName, year):
        return cls(customerName, date.today().year - year)
    
    @staticmethod
    def getIsAdult(age):
        return age >= 21

class CustomerBalance(Customer):
    def __init__(self,customerID, customerName, customerEmail, balance):
        super().__init__(customerID, customerName, customerEmail)
        self.balance = balance
    
    def getBlance(self):
        print("CustomerID: ", self.customerID, "CustomerBalance: ", self.balance)

def main():
    cus = Customer('C0001', 'John Adam', 'abc@gmail.com')
    cus.getInformation()

    cusBalance = CustomerBalance('C0001','John Adam', 'abc@gmail.com',1000000000)
    cusBalance.getBlance()

    cus1 = Customer.getBOD('John Adam', 2021)
    cus1.age

if __name__ == '__main__':
    main()