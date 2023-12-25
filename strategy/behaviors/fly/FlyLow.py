from .IFly import IFly
#type of flying
class FlyLow(IFly):
    def __init__(self):
        super().__init__()
        self.desc = "Flying-Low"

    def fly(self):
        print("fly_low")


