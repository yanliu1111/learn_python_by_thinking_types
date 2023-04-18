from datetime import datetime
from customer import Customer
from invoice_item import InvoiceItem
from item import Item

class CashRegister:

    def __init__(self, customer: Customer)-> None:
        self.customer = customer
        self.items: dict [str, InvoiceItem] = {}
        self.purchase_date = datetime.now()
        self._invoice_total:float = 0

    def __repr__(self) -> str:
        return "<class 'CashRegister'>"
    
    def __str__(self) -> str:
        return f"Customer: {self.customer}, Total Items: {len(self.items)}"
    
    # i want to give inc_invoice_total a private number, I don't want any developer to change my logic
    def _inc_invoice_total(self, item:InvoiceItem)-> None:
        self._invoice_total += item.get_sub_total()
    # next is decrement
    def _dec_invoice_total(self, item:InvoiceItem)-> None:
        self._invoice_total -= item.get_sub_total()
    
    def add_item(self, item: Item, qty: int=1, discount: float = 0) -> None:
        if item.name not in self.items:
            new_item = InvoiceItem(item, qty, discount)
            self.items [item.name] = new_item
            self._inc_invoice_total(new_item)

        else:
            print(f"{item.name} is already in the cart")