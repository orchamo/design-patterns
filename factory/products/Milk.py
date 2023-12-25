from products.IProduct import IProduct

class Milk(IProduct):
    def description(self):
        return "Milk"
    
    def price(self):
        return 5
    
    