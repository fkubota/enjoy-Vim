class keeper:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'({self.name})nya-n!!')

    def feed(self, animal):
        animal.genki += 1
