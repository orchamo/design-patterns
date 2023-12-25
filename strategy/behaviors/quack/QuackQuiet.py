from .IQuackBehavior import IQuackBehavior
#type of quacking
class QuackQuiet(IQuackBehavior):
    def __init__(self):
        super().__init__()
        self.desc = "Quacking-Quiet"

    def quack(self):
        print("quack_quiet")
        
