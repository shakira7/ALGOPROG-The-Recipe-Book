from backend.constants import UNITS_LIST

class Ingredient:
    def __init__(self, name="N/A", quantity=0, unit="unit(s)"): 
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def unit(self):
        return self._unit
    
    @unit.setter
    def unit(self, new_value):
        if new_value.lower() in UNITS_LIST:
            self._unit = new_value.lower()
        else:
            print(f"Error: unit must be in {UNITS_LIST}")
            self._unit = "unit(s)"

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, new_value):
        if new_value > -1:
            self._quantity = new_value
        else:
            print(f"Error: Quantity cannot be under 0.")
            self._quantity = 0

    def __str__(self):
        return (f"{self.quantity} {self.name} {self.unit}")
    

