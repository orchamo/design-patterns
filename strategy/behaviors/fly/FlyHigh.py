from .IFly import IFly
#type of flying
class FlyHigh(IFly):
    def __init__(self):
        super().__init__()
        self.desc = "Flying-High"

    def fly(self):
        print("fly_high")

    #allows access to parent variables
    def parent_behavior(self):
        return self.behavior