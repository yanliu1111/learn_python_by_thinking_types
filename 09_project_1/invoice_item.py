from item import Item

class InvoiceItem:
    def __init__(self, item: Item, qty: int, discount: float = 0) -> None:
        self.item = item
        self.qty = qty
        self.discount = discount
        #private number
        self._sub_total = (item.price * qty) - discount
    def __repr__(self) -> str:
        return "<class 'InvoiceItem'>"
    def __str__(self) -> str:
        return f"Item: {self.item.name}, Qty: {self.qty}, Discount: ${self.discount}, Sub Total: {self.get_sub_total():.2f}"
    def get_sub_total(self) -> float:
        return self._sub_total