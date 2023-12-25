from base_beverages.Beverage import BaseBeverage


class CaramelAddon(BaseBeverage):

    def __init__(self, beverage : BaseBeverage):
        self.beverage = beverage

    def description(self):
        return "caramel addon"
    
    def cost(self):
        base = self.beverage.cost()
        return 2 + base