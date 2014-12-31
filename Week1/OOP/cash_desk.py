from copy import deepcopy


class CashDesk:
    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, moni):
        # self.money = moni
        for key in moni:
            self.money[key] += moni[key]
        return self.money

    def total(self):
        totalsum = 0
        for key in self.money:
            totalsum += key*self.money[key]
        return totalsum

    def can_withdraw_money(self, amount):
        pa4ki = deepcopy(self.money)
        while amount > 0:
            for key in [100, 50, 20, 10, 5, 2, 1]:
                if pa4ki[key] > 0:
                    while pa4ki[key] > 0:
                        if amount - key >= 0:
                            amount -= key
                        pa4ki[key] -= 1
                        # print(amount)
                        if amount == 0:
                            return True
            if amount != 0:
                return False
            # if amount == 0:
            #     return True
            # else:
            #     return False

            # for key in self.money:
            #     while amount - key >= 0:
            #         if self.money[key] > 0:
            #             self.money[key] -= 1
            #             amount - key
            # if amount != 0:
            #     return False
            # else:
            #     return True


my_cash_desk = CashDesk()
print(my_cash_desk.take_money({1: 2, 50: 1, 20: 1}))
# print(my_cash_desk.total())
print(my_cash_desk.can_withdraw_money(50))
print(my_cash_desk.can_withdraw_money(30))
print(my_cash_desk.can_withdraw_money(71))
