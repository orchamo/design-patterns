from base_beverages.Beverage import BaseBeverage


class SoyAddon(BaseBeverage):

    def __init__(self, beverage : BaseBeverage):
        self.beverage = beverage

    def description(self):
        return "Soy addon"
    
    def cost(self):
        base = self.beverage.cost()
        return 2 + base