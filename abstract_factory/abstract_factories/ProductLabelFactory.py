from abstract_factories.Factory import Factory


class ProductLabelFactory(Factory):
    
    def instantiate(self,product, label):
        self.product = product
        self.label = label
        print(f'The {product} contains {label}')