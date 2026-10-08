class CreditCard:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_info(self):
        print(f"Номер счета: {self.number}")
        print(f"Баланс карты: {self.balance}")

card1 = CreditCard(1, 1000)
card2 = CreditCard(2, 49040303)
card3 = CreditCard(3, 4288393)

card1.deposit(405)
card2.deposit(40554)
card3.withdraw(3040)

card1.show_info()
card2.show_info()
card3.show_info()