class Logger:
    def __init__(self):
        print("Object Created!")
        
    def __del__(self):
        print("Object Destroyed!")

# Object creation
logger = Logger()
del logger  # Object destruction
