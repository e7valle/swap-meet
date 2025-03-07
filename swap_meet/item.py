import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id or uuid.uuid4().int 
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f'An object of type Item with id {self.id}.'
    
    def condition_description(self):
        if self.condition == 0:
            return "Trendy"
        if self.condition == 1:
            return "In good condition"
        if self.condition == 2:
            return "Cute"
        if self.condition == 3:
            return "Chic"
        if self.condition == 4:
            return "Heavily used"
        if self.condition == 5:
            return "Comfortable"