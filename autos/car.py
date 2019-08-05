class Car:
    def __init__(self, name = "Das Boot", fuel = 100):
        self.name = name
        self.fuel = fuel

    def hello(self):
        print(f'hi, I am {self.name}')

    def honk(self):
        print("Beep Beep")
        self.hello()

    def current_fuel(self):
        return self.fuel

    def drive(self):
        if self.fuel > 0:
            self.fuel = self.fuel - 1
            return True
        else:
            return False