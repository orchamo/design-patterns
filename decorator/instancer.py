from base_beverages.CapuccinoBeverage import CapuccinoBeverage
from addons.CaramelAddon import CaramelAddon
from base_beverages.EspressoBeverage import EspressoBeverage

#Bevrages
c = CapuccinoBeverage()
e = EspressoBeverage()
#Addons
ca = CaramelAddon

final_cost = 0
espresso_caramel = CaramelAddon(e).cost()
print(espresso_caramel)