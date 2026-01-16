from backend.cooktime import CookTime

class Instruction: 

    def __init__(self, step_number=1, description="No description", minute=0, second=0):
        self.step_number = step_number
        self.description = description
        self.time = CookTime(minute, second)

    @property
    def step_number(self):
        return self._step_number 
    
    @step_number.setter
    def step_number(self, new_value):
        if new_value > 0:
            self._step_number = new_value
        else: 
            print(f"Error: The step number cannot be under 1.")
            self._step_number = 1

    def __str__(self):
        return(f"{self.step_number}) {self.description}")
    