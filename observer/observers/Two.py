from Subject import Subject
from observers.IObserver import IObserver
from observers.IDisplay import IDisplay


#observer of the Subject. which implements IDisplay and IObserver interfaces..
class Two(IDisplay, IObserver):
    subject_counter = 0

    #recieves a Subject object to allow access to its methods when needed
    def __init__(self, sub : Subject):
        self.subject = sub
    
    def update(self):
        self.subject_counter = self.subject.count()

    #prints the current state of the count in the Subjected object
    def display(self):
        print (f'two says, the count is {self.subject_counter}')