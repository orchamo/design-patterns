from commands.ICommand import ICommand
from recievers.Light import Light


class LightOnCommand(ICommand):
    
    def __init__(self):
        self.light = Light()

    def execute(self):
        self.light.light_on()
    
    def unexecute(self):
        self.light.light_off()