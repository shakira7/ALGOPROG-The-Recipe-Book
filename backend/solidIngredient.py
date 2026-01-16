from backend.ingredient import Ingredient
from backend.constants import SIZE_LIST

class SolidIngredient(Ingredient): 
    def __init__(self, name="N/A", quantity=0, unit="tablespoon", size=None, is_ground=False):
        super().__init__(name, quantity, unit)
        self.size = size
        self.is_ground = is_ground

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_value):
        if new_value.lower() in SIZE_LIST:
            self._size = new_value.lower()
        else:
            print(f"Error: size must be in {SIZE_LIST}")

    def set_is_ground(self, is_ground):
        self.is_ground = is_ground
    
    def get_is_ground(self):
        if self.is_ground == True:
            return ("(Grounded)")
        return ""

    def __str__(self):
        return(f"{self.quantity} {self.size} {self.unit} of {self.name} {self.get_is_ground()}")