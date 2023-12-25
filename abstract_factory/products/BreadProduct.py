from products.Products import Products


class BreadProduct(Products):

    def product_name(self):
        return "Bread Product"
    
    def __str__(self):
        return "Bread Product"