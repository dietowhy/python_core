class ATM:
    def __init__(self, count_20, count_50, count_100):
        self.count_20 = count_20
        self.count_50 = count_50
        self.count_100 = count_100
    
    def add_money(self, count_20=0, count_50=0, count_100=0):
        self.count_20 += count_20
        self.count_50 += count_50
        self.count_100 += count_100

    def withdraw(self, amount):
        for n100 in range(min(self.count_100, amount // 100), -1, -1):
            balance = amount - n100 * 100

            for n50 in range(min(self.count_50, balance // 50), -1, -1):
                balance2 = balance - n50 * 50

                if balance2 % 20 == 0 and balance2 // 20 <= self.count_20:
                    n20 = balance2 // 20

                    self.count_100 -= n100
                    self.count_50  -= n50
                    self.count_20  -= n20

                    print(f"Выдано: 100×{n100}, 50×{n50}, 20×{n20}")
                    return True
    
        print(f"Невозможно выдать сумму {amount}")
        return False
   
    def show_balance(self):
        total = self.count_20 * 20 + self.count_50 * 50 + self.count_100 * 100
        print(f"В банкомате: 100×{self.count_100}, 50×{self.count_50}, 20×{self.count_20} (итого {total} руб.)")

atm = ATM(count_20=14, count_50=3, count_100=5)
atm.show_balance()

atm.add_money(count_20=5, count_50=2)
atm.show_balance()

atm.withdraw(180)
atm.show_balance()

atm.withdraw(560)
atm.show_balance()

atm.withdraw(326)
atm.show_balance()