from products.Bread import Bread
from factories.RandomFactory import RandomFactory
from products.Milk import Milk


random_factory = RandomFactory()
random_factory.add_product(Milk())
random_factory.add_product(Bread())

random_factory.return_products()
