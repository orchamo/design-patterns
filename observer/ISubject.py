#interface for subject to notify observers of change
class ISubject:
    def add(self):
        pass

    def remove(self):
        pass

    def notify(self):
        pass