from products.Products import Products


class TofuProduct(Products):
    
    def product_name(self):
        return "Tofu Product"
    
    def __str__(self):
        return "Tofu Product"