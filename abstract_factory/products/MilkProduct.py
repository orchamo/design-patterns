from products.Products import Products


class MilkProduct(Products):
    
    def product_name(self):
        return "Milk Product"
    
    def __str__(self):
        return "Milk Product"