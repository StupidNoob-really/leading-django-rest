class ProfileModel:
    def __init__(self):
        self._observers = []

    def notify_observers(self):
        return self._observers

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)