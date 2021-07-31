class dog:
    def __init__(self, name):
        self.name = name
        self.genki = 0

    def bark(self):
        print(f'({self.name})wan{"!"*self.genki}')


class cat:
    def __init__(self, name):
        self.name = name
        self.genki = 0

    def bark(self):
        print(f'({self.name})miaw{"!"*self.genki}')
