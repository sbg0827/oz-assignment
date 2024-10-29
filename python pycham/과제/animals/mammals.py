class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.breed} dog."