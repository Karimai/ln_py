
class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        if money < self.item_price * req_items:
            raise ValueError("Not enough coins")
        self.num_items -= req_items
        return "The change given back after the purchase"


init = input()
items, price = init.split()
machine = VendingMachine(items, price)
num_operators = int(input())
for i in range(num_operators):
    buy_req = input()
    items, money = buy_req.split()
    machine.buy(items, money)




