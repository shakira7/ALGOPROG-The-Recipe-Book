from backend.constants import DIFFICULTY_LIST

class Category:
    def __init__(self, cuisine="N/A", course="All", difficulty="N/A"):
        self.cuisine = cuisine
        self.course = course
        self.difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty
    
    @difficulty.setter
    def difficulty(self, new_value):
        if new_value.lower() in DIFFICULTY_LIST:
            self._difficulty = new_value.lower()
        else:
            print(f"Error: Difficulty must be {DIFFICULTY_LIST}")
            self._difficulty="N/A"
