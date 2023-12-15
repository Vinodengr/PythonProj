import csv

class item:    
    pay_rate = 0.8

    all =[]
    def __init__(self, name: str, price:float, quantity: int):

        assert price >=0, f"Price {price} should be greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} should be greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        item.all.append(self)


    def calc_total_amount(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open ('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
        
    
    def __repr__(self) -> str:
        return f"item('{self.name}', {self.price},{self.quantity})"


item.instantiate_from_csv()