class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition

    def drive(self):
        self.engine.start()

# Object creation
engine = Engine()
car = Car(engine)
car.drive()
