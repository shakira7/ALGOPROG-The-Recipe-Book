from backend.ingredient import Ingredient
from backend.category import Category
from backend.instruction import Instruction

class Recipe:
    def __init__(self, name="N/A", description="No description", ingredient_list=None, full_instructions=None, category=None):
        self.name = name
        self.description = description

        if ingredient_list is None:
            self.ingredient_list = []
        else: 
            self.ingredient_list = ingredient_list
        
        if full_instructions is None:
            self.full_instructions = []
        else:
            self.full_instructions = full_instructions
        
        if category is None:
            self.category = Category()
        else:
            self.category = category
            

    def addIngredient(self, new_ingredient):
        if isinstance(new_ingredient, Ingredient):
            self.ingredient_list.append(new_ingredient)
        else:
            print("Error: Not an ingredient.")
    
    def addInstruction(self, new_instruction):
        if isinstance(new_instruction, Instruction):
            self.full_instructions.append(new_instruction)
        else:
            print("Error: Not an instruction.")

    


    

