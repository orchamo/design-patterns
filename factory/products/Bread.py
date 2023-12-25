from products.IProduct import IProduct


class Bread(IProduct):
    def description(self):
        return "Bread"
    
    def price(self):
        return 7