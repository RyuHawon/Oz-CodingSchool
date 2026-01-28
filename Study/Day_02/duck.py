from abc import ABC, abstractmethod

class duck(ABC):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None
    
    def set_fly(self, flybehavior):
        self.fly_behavior = flybehavior
    
    def set_quack(self, quackbehavior):
        self.quack_behavior = quackbehavior

    def perform_fly(self):
        self.fly_behavior.fly()
    
    def perform_quack(self):
        self.quack_behavior.quack()

class quack_behavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class fly_behavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class fly_high(fly_behavior):
    def fly(self):
        print("I can fly high")

class fly_low(fly_behavior):
    def fly(self):
        print("I can fly low")

class fly_not(fly_behavior):
    def fly(self):
        print("I can't fly")

class quack_loud(quack_behavior):
    def quack(self):
        print("I can quack loud")

class quack_quiet(quack_behavior):
    def quack(self):
        print("I can quack quiet")

class real_duck(duck):
    def __init__(self):
        super().__init__()
        self.set_fly(fly_high())
        self.set_quack(quack_loud())

class rubber_duck(duck):
    def __init__(self):
        super().__init__()
        self.set_fly(fly_not())
        self.set_quack(quack_quiet())


