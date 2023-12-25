from abstract_factories.ProductLabelFactory import ProductLabelFactory
from labels.MilkLabel import MilkLabel
from products.MilkProduct import MilkProduct

milk_label = MilkLabel()
milk_product = MilkProduct()

ProductLabelFactory().instantiate(milk_product,milk_label)