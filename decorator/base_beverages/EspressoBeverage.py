from base_beverages.Beverage import BaseBeverage


class EspressoBeverage(BaseBeverage):

    def description(self):
        return "espresso"
    
    def cost(self):
        return 10