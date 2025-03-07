from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0):
        self.width = width
        self.length = length
        super().__init__(id, condition)

    def get_category(self):
        # return "Decor"
        return self.__class__.__name__
    
    def __str__(self):
        return f'An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space.'
    
    def condition_description(self):
        some_condition = super().condition_description()
        return some_condition