from commands.ICommand import ICommand


class Invoker():
    def __init__(self, com1: ICommand):
        self.command_one = com1.execute
        self.command_two = com1.unexecute

    def click(self):
        self.command_one()

    def click_again(self):
        self.command_two()
       



        