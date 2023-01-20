# Class Duck creates different ducks with flying and quacking properties that can vary.
# it recieves them when creating different instances of duck
class Duck:
    def __init__(self,name ,fly ,quack):
        self.genus = "Duck"
        self.name = name
        self.fly = fly
        self.quack = quack

    #shows how you can take variables from this class, fly or quack classes and from their parent class.
    def __str__(self) -> str:
        return f'the {self.genus} named {self.name} can {self.fly.parent_behavior()} and {self.quack.parent_behavior()}.\
 He is {self.fly.desc} and {self.quack.desc}'

    