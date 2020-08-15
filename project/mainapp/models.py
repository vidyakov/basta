class Category:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc

    @property
    def link(self):
        return self.name.replace(' ', '_').lower() + '/'
