from products.IProduct import IProduct

class Tofu(IProduct):
    def description(self):
        return "Tofu"
    
    def price(self):
        return 4