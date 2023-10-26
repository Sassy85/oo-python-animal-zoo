from lib.animal import Animal

class Zoo:
    all=[]

    def __init__(self, name='', location=''):
        self.name=name
        self.location=location
        Zoo.all.append(self)

    def animals(self):
        return[animal for animal in Animal.all if animal.zoo==self]
    