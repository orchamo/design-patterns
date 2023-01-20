from .IQuack import IQuack
#type of quacking
class QuackLoud(IQuack):
    def __init__(self):
        super().__init__()
        self.desc = "Quacking-Loud"

    def quack(self):
        print("quack_loud")

    #allows access to parent variables
    def parent_behavior(self):
        return self.behavior