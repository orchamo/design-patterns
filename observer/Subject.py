from ISubject import ISubject
import observers

class Subject(ISubject):

    #array of listed observers of the subject - to notify for change in the count
    observers_arr = []

    current_count = 0

    #adds an observer to the observers array
    def add(self, obs):
        self.observers_arr.append(obs)
        return print("added")
        
    #removes an observer from the observers array    
    def remove(self,obs):
        self.observers_arr.remove(obs)
        return print("removed")

    #updates all listed in the observers array
    def notify(self):
        for obs in self.observers_arr:
            obs.update()
            
    #adds one to the count and calls the notify to let the observers know a change accured
    def plus_one(self):
        self.current_count += 1
        self.notify()

    # a method to get the state of the count
    def count(self):
        return self.current_count

    
    