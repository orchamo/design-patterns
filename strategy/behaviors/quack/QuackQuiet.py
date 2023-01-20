from .IQuack import IQuack
#type of quacking
class QuackQuiet(IQuack):
    def __init__(self):
        super().__init__()
        self.desc = "Quacking-Quiet"

    def quack(self):
        print("quack_quiet")
        
    #allows access to parent variables
    def parent_behavior(self):
        return self.behavior