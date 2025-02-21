class Logger:
    def log(self, message):
        print("log: " + message)


class Display:
    def display(self, message):
        print("display: " + message)


class Terminal(Logger, Display):
    def __init__(self):
        self.log("Creating an instance of Terminal")
        self.display("Welcome to the terminal")


t = Terminal()
