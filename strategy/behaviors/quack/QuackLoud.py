from .IQuackBehavior import IQuackBehavior
#type of quacking
class QuackLoud(IQuackBehavior):
    def __init__(self):
        super().__init__()
        self.desc = "Quacking-Loud"

    def quack(self):
        print("quack_loud")
