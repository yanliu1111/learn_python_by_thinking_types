from cash_register import CashRegister
from customer import Customer
from item import Item

milk = Item(100, "Milk", 5.78, "Litre")
egg = Item(101, "Egg", 4.5, "Dozen")
rice = Item(102, "Rice", 10.5, "Kg")
apple = Item(103, "Apple", 5.67, "Kg")

customer1 = Customer ("Peter", "Parker")

cr1 = CashRegister(customer1)
cr1.add_item(milk)
cr1.add_item(egg, 2, 0.5)
cr1.update_item(egg, 1, 0.25)
cr1.add_item(rice, 2, 1.5)
# cr1.add_item(rice, 2, 1.5) # no change, already in cart
# cr1.update_item(apple, 3, 0.75) # not in cart, no change

# print(cr1)
cr1.display_invoice()
cr1. remove_item(rice)
# cr1.display_invoice()

# second customer
customer2 = Customer ("Bruce", "Wayne")
cr2 = CashRegister(customer2)
cr2.add_item(milk, qty=4, discount=10)
cr2.add_item(egg, qty=2)
cr2.update_item(egg, qty=4, discount=2)
cr2.add_item(apple, qty=8, discount=2)
# cr2.display_invoice()

print(cr2.toJSON())