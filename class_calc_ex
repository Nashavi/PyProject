class Calculator(object):

    def __init__(self):
        self.current = 0

    def add(self,amount):
        self.current += amount


    def subtract(self,amount):
        self.current -= amount


    def product(self,amount):
        self.current *= amount


    def divide(self,amount):
        if amount != 0:
            self.current = self.current / amount
        else :
            raise RuntimeError('Not divisible by zero!')

    def get_current(self):
        print(self.current)


cal = Calculator()
cal.add(5)
cal.product(5)
cal.subtract(5)
cal.divide(0)
cal.get_current()
