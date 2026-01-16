from backend.ingredient import Ingredient
from backend.constants import VISCOSITY_LIST

class LiquidIngredient(Ingredient): 
    def __init__(self, name="N/A", quantity=0, unit="tablespoon", viscosity=None):
        super().__init__(name, quantity, unit)
        self.viscosity = viscosity

    @property
    def viscosity(self):
        return self._viscosity

    @viscosity.setter
    def viscosity(self, new_value):
        if new_value.lower() in VISCOSITY_LIST:
            self._viscosity = new_value.lower()
        else:
            print(f"Error: viscosity must be in {VISCOSITY_LIST}")
            self._viscosity = None

    def __str__(self):
        return(f"{self.quantity} of {self.unit} {self.name} ({self.viscosity})")
    