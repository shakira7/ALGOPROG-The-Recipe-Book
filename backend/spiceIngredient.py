from backend.ingredient import Ingredient
from backend.constants import SPICE_LEVEL_LIST

class SpiceIngredient(Ingredient): 
    def __init__(self, name="N/A", quantity=0, unit="tablespoon", spice_level="not spicy", is_optional=False):
        super().__init__(name, quantity, unit)
        self.spice_level = spice_level
        self.is_optional = is_optional
    
    @property
    def spice_level(self):
        return self._spice_level
    
    @spice_level.setter
    def spice_level(self, new_value):
        if new_value.lower() in SPICE_LEVEL_LIST:
            self._spice_level = new_value.lower()
        else:
            print(f"Error: Spice level must be in {SPICE_LEVEL_LIST}")
            self._spice_level = "not spicy"

    def get_is_optional(self):
        if self.is_optional:
            return "(Optional)"
        return ""

    def __str__(self):
        return(f"{self.quantity} {self.unit} of {self.name} {self.get_is_optional()} ({self.spice_level})")