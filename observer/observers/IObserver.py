#an interface to make sure an observer must have an update method for when the Subject object changes,
# it will update.
class IObserver:
    def update(self):
        pass
