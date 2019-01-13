class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        print('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
hydrogen.dump()
