from base_beverages.Beverage import BaseBeverage


class CapuccinoBeverage(BaseBeverage):

    def description(self):
        return "capuccino"
    
    def cost(self):
        return 15