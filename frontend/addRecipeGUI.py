import customtkinter
from backend.recipe import Recipe
from backend.ingredient import Ingredient
from frontend.dialogs import IngredientDialog, InstructionDialog, CategoryDialog




class AddRecipeGUI:
   def __init__(self, root, on_back, on_save_success):
       self.root = root
       self.on_back = on_back
       self.on_save_success = on_save_success
       self.new_recipe = Recipe()


       self.root.title("Create New Recipe")
       self.root.geometry("700x700")
       self.root.resizable(width=False, height=True)


       # --- HEADER ---
       header = customtkinter.CTkFrame(self.root, fg_color="transparent")
       header.pack(fill="x", padx=20, pady=20)


       # Back Button
       back_btn = customtkinter.CTkButton(
           header, text="Cancel", width=60, fg_color="transparent",
           text_color="red", hover_color="gray20", command=self.on_back
       )
       back_btn.pack(side="left")


       # Save Button
       save_btn = customtkinter.CTkButton(
           header,
           text="Save Recipe",
           width=100,
           fg_color="#4B0082",
           command=self.save_recipe
       )
       save_btn.pack(side="right")


       self.scroll = customtkinter.CTkScrollableFrame(
           self.root,
           width=600,
           height=600
       )
       self.scroll.pack(
           fill="both",
           expand=True,
           padx=20,
           pady=(0,20)
       )


       # NAME
       customtkinter.CTkLabel(
           self.scroll,
           text="RECIPE NAME",
           font=("Arial", 12, "bold")
       ).pack(anchor="w", pady=(10,0))
       self.name_entry = customtkinter.CTkEntry(
           self.scroll,
           width=400,
           placeholder_text="e.g. Nasi Goreng"
       )
       self.name_entry.pack(
           anchor="w",
           pady=5
       )

       # DESCRIPTION
       customtkinter.CTkLabel(
           self.scroll,
           text="DESCRIPTION",
           font=("Arial", 12, "bold")
       ).pack(anchor="w", pady=(10,0))
       self.desc_entry = customtkinter.CTkEntry(
           self.scroll,
           width=400,
           placeholder_text="Short description..."
       )
       self.desc_entry.pack(anchor="w", pady=5)

       # CATEGORY
       customtkinter.CTkLabel(
           self.scroll,
           text="CATEGORY",
           font=("Arial", 12, "bold")
       ).pack(anchor="w", pady=(20,0))
       self.category_frame = customtkinter.CTkFrame(
           self.scroll,
           fg_color="gray20",
           height=50
       )
       self.category_frame.pack(fill="x", pady=5)
      
       customtkinter.CTkButton(
           self.category_frame,
           text="Set Category",
           width=100,
           fg_color="gray30",
           command=self.open_category_popup
       ).pack(side="left", padx=10, pady=10)
      
       self.category_label = customtkinter.CTkLabel(
           self.category_frame,
           text="None selected"
       )
       self.category_label.pack(side="left", padx=10)


       # 4. INGREDIENTS
       customtkinter.CTkLabel(
           self.scroll, 
           text="INGREDIENTS", 
           font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(20,0))
      
       # The list container
       self.ingredient_list_frame = customtkinter.CTkFrame(self.scroll, fg_color="transparent")
       self.ingredient_list_frame.pack(fill="x", pady=5)

       customtkinter.CTkButton(
           self.scroll, text="+ Add Ingredient", width=150,
           fg_color="gray30", command=self.open_ingredient_popup
       ).pack(anchor="w", pady=5)

       # 5. INSTRUCTIONS
       customtkinter.CTkLabel(
           self.scroll, 
           text="INSTRUCTIONS", 
           font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(20,0))
      
       # The list container
       self.instruction_list_frame = customtkinter.CTkFrame(self.scroll, fg_color="transparent")
       self.instruction_list_frame.pack(fill="x", pady=5)

       customtkinter.CTkButton(
           self.scroll, text="+ Add Step", width=150,
           fg_color="gray30", command=self.open_instruction_popup
       ).pack(anchor="w", pady=5)

   # --- CATEGORY FUNCTIONS ---
   def open_category_popup(self):
       CategoryDialog(self.root, on_confirm=self.set_category)

   def set_category(self, category_object):
       self.new_recipe.category = category_object
       display_text = f"{category_object.cuisine} | {category_object.course} | {category_object.difficulty}"
       self.category_label.configure(
           text=display_text,
           font=("Arial", 14, "bold"),
           text_color="white"
       )

   def open_ingredient_popup(self):
       IngredientDialog(self.root, on_add=self.add_ingredient_to_list)

   def add_ingredient_to_list(self, ingredient_object):
      
       self.new_recipe.addIngredient(ingredient_object)
       label_text = f"• {str(ingredient_object)}"
       label = customtkinter.CTkLabel(
           self.ingredient_list_frame,
           text=label_text,
           anchor="w",
           font=("Arial", 14)
       )
       label.pack(fill="x", padx=10, pady=2)

   def open_instruction_popup(self):
       next_step = len(self.new_recipe.full_instructions) + 1
       InstructionDialog(
           self.root,
           step_number=next_step,
           on_add=self.add_instruction_to_list
       )
   def add_instruction_to_list(self, instruction_object):
       self.new_recipe.addInstruction(instruction_object)
       label_text = f"{instruction_object.step_number}. {instruction_object.description}"
       total_seconds = instruction_object.time.get_total_seconds()
       if total_seconds > 0:
            label_text += f" ({instruction_object.time.minute}m {instruction_object.time.second}s)"
       label = customtkinter.CTkLabel(
           self.instruction_list_frame,
           text=label_text,
           anchor="w",
           font=("Arial", 14),
           wraplength=500
       )
       label.pack(fill="x", padx=10, pady=2)

   def save_recipe(self):
       self.new_recipe.name = self.name_entry.get()
       self.new_recipe.description = self.desc_entry.get()
       if not self.new_recipe.name:
           print("Error: Recipe must have a name")
           return
       print(f"Sending {self.new_recipe.name} to database...")
       self.on_save_success(self.new_recipe)

