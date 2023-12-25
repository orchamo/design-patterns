
from products.IProduct import IProduct
from factories.IFactory import IFactory


class RandomFactory(IFactory):
    prod_list = []

    # def __init__(self, product : Product):
    #     self.product = product

    def add_product(self, product : IProduct):
        self.prod_list.append(product)

    def remove_product(self, product : IProduct):
        self.prod_list.remove(product)

    def return_products(self):
        for x in self.prod_list:
            print( x.description())

        