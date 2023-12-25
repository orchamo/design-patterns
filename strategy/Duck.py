# Class Duck creates different ducks with flying and quacking properties that can vary.
# it recieves them when creating different instances of duck
from strategy.behaviors.fly.IFly import IFly
from strategy.behaviors.quack.IQuack import IQuackBehavior


class Duck:
    def __init__(self,name ,fly: IFly ,quack: IQuackBehavior):
        self.genus = "Duck"
        # self.name = name
        # self.fly = fly
        # self.quack = quack

    def fly(self):
        self.fly()
        pass
    #shows how you can take variables from this class, fly or quack classes and from their parent class.
    def __str__(self) -> str:
        return f'the {self.genus} named {self.name} can {self.fly.desc} and {self.quack.desc}'

    