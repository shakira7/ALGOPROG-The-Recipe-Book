import customtkinter
from backend.constants import (
   UNITS_LIST,
   VISCOSITY_LIST,
   SIZE_LIST,
   SPICE_LEVEL_LIST,
   CUISINE_LIST,
   COURSE_LIST,
   DIFFICULTY_LIST
)


from backend.ingredient import Ingredient
from backend.liquidIngredient import LiquidIngredient
from backend.solidIngredient import SolidIngredient
from backend.spiceIngredient import SpiceIngredient
from backend.instruction import Instruction
from backend.category import Category




class IngredientDialog(customtkinter.CTkToplevel):


   def __init__(self, parent, on_add, on_delete=None):
       super().__init__(parent)
       self.on_add = on_add
       self.on_delete = on_delete
      
       self.title("Add/Edit Ingredient")
       self.geometry("500x600")
       self.resizable(True, True)
       self.attributes("-topmost", True)
      
       self.scroll_frame = customtkinter.CTkScrollableFrame(
           self,
           width=450,
           height=450,
           fg_color="transparent"
       )
       self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)


       self.specific_frame = customtkinter.CTkFrame(
           self.scroll_frame,
           fg_color="transparent"
       )


       # --- TYPE SELECTOR ---
       customtkinter.CTkLabel(
           self.scroll_frame,
           text="Ingredient Type:",
           font=("Arial", 14, "bold")
       ).pack(anchor="w")
      
       self.type_var = customtkinter.StringVar(value="Standard")
       self.type_menu = customtkinter.CTkOptionMenu(
           self.scroll_frame,
           values=["Standard", "Liquid", "Solid", "Spice"],
           variable=self.type_var,
           width=300,
           command=self.update_fields
       )
       self.type_menu.pack(pady=(5, 20), anchor="w")


       # --- COMMON FIELDS ---
       customtkinter.CTkLabel(
           self.scroll_frame,
           text="Name:",
           font=("Arial", 12)
       ).pack(anchor="w")
       self.name_entry = customtkinter.CTkEntry(
           self.scroll_frame,
           width=300
       )
       self.name_entry.pack(pady=5, anchor="w")


       customtkinter.CTkLabel(
           self.scroll_frame,
           text="Quantity:",
           font=("Arial", 12)
       ).pack(anchor="w")
       self.qty_entry = customtkinter.CTkEntry(
           self.scroll_frame,
           width=300
       )
       self.qty_entry.pack(pady=5, anchor="w")


       customtkinter.CTkLabel(
           self.scroll_frame,
           text="Unit:",
           font=("Arial", 12)
       ).pack(anchor="w")
       self.unit_var = customtkinter.StringVar(value=UNITS_LIST[0])
       self.unit_menu = customtkinter.CTkOptionMenu(
           self.scroll_frame,
           values=UNITS_LIST,
           variable=self.unit_var,
           width=300
       )
       self.unit_menu.pack(pady=5, anchor="w")

       # --- PACK DYNAMIC FRAME ---
       self.specific_frame.pack(fill="x", pady=10)
       self.viscosity_var = None
       self.size_var = None
       self.ground_var = None
       self.spice_var = None
       self.optional_var = None

       # --- BUTTONS ROW (Outside Scroll Frame) ---
       btn_frame = customtkinter.CTkFrame(self, fg_color="transparent")
       btn_frame.pack(fill="x", padx=20, pady=(0, 20))


       # Delete Button (Only if editing)
       if self.on_delete:
           customtkinter.CTkButton(
               btn_frame,
               text="Delete",
               fg_color="#8B0000",
               hover_color="red",
               width=80,
               command=self.confirm_delete
           ).pack(side="left")


       # Save Button
       customtkinter.CTkButton(
           btn_frame,
           text="Save",
           fg_color="#4B0082",
           width=100,
           command=self.confirm_add
       ).pack(side="right")


       # Cancel Button
       customtkinter.CTkButton(
           btn_frame,
           text="Cancel",
           fg_color="transparent",
           border_width=1,
           border_color="gray",
           text_color="gray80",
           width=80,
           command=self.destroy
       ).pack(side="right", padx=10)


   def update_fields(self, choice):
       for widget in self.specific_frame.winfo_children():
           widget.destroy()


       if choice == "Liquid":
           customtkinter.CTkLabel(
               self.specific_frame,
               text="Viscosity:",
               font=("Arial", 12)
           ).pack(anchor="w")


           self.viscosity_var = customtkinter.StringVar(value=VISCOSITY_LIST[0])
           customtkinter.CTkOptionMenu(
               self.specific_frame, values=VISCOSITY_LIST,
               variable=self.viscosity_var,
               width=300
           ).pack(pady=5, anchor="w")


       elif choice == "Solid":
           customtkinter.CTkLabel(
               self.specific_frame,
               text="Size:",
               font=("Arial", 12)
           ).pack(anchor="w")


           self.size_var = customtkinter.StringVar(value=SIZE_LIST[0])


           customtkinter.CTkOptionMenu(
               self.specific_frame,
               values=SIZE_LIST,
               variable=self.size_var,
               width=300
           ).pack(pady=5, anchor="w")


           self.ground_var = customtkinter.BooleanVar(value=False)
           customtkinter.CTkCheckBox(
               self.specific_frame,
               text="Is Grounded?",
               variable=self.ground_var
           ).pack(pady=10, anchor="w")






       elif choice == "Spice":
           customtkinter.CTkLabel(
               self.specific_frame,
               text="Spice Level:",
               font=("Arial", 12)
           ).pack(anchor="w")


           self.spice_var = customtkinter.StringVar(value=SPICE_LEVEL_LIST[0])


           customtkinter.CTkOptionMenu(
               self.specific_frame,
               values=SPICE_LEVEL_LIST,
               variable=self.spice_var,
               width=300
           ).pack(pady=5, anchor="w")


           self.optional_var = customtkinter.BooleanVar(value=False)


           customtkinter.CTkCheckBox(
               self.specific_frame,
               text="Is Optional?",
               variable=self.optional_var
           ).pack(pady=10, anchor="w")


   def confirm_add(self):
       name = self.name_entry.get()
       try:
           qty = float(self.qty_entry.get())
       except ValueError:
           print("Invalid Quantity")
           return
       unit = self.unit_var.get()
       ing_type = self.type_var.get()


       new_ingredient = None


       if ing_type == "Standard":
           new_ingredient = Ingredient(name, qty, unit)
       elif ing_type == "Liquid":
           viscosity = self.viscosity_var.get()
           new_ingredient = LiquidIngredient(name, qty, unit, viscosity)
       elif ing_type == "Solid":
           size = self.size_var.get()
           is_ground = self.ground_var.get()
           new_ingredient = SolidIngredient(name, qty, unit, size, is_ground)
       elif ing_type == "Spice":
           spice_level = self.spice_var.get()
           is_optional = self.optional_var.get()
           new_ingredient = SpiceIngredient(name, qty, unit, spice_level, is_optional)


       if new_ingredient:
           self.on_add(new_ingredient)
           self.destroy()


   def confirm_delete(self):
       if self.on_delete:
           self.on_delete()
           self.destroy()





# INSTRUCTIONS DIALOGUE

class InstructionDialog(customtkinter.CTkToplevel):
   def __init__(self, parent, step_number, on_add, on_delete=None):
       super().__init__(parent)
       self.step_number = step_number
       self.on_add = on_add
       self.on_delete = on_delete
      
       self.title(f"Add/Edit Step {step_number}")
       self.geometry("500x400")
       self.attributes("-topmost", True)
      
       customtkinter.CTkLabel(
           self,
           text="Description:",
           font=("Arial", 14, "bold")
       ).pack(pady=(20,5), padx=20, anchor="w")
      
       self.desc_text = customtkinter.CTkTextbox(
           self,
           height=100,
           width=400
       )
       self.desc_text.pack(pady=5)

       customtkinter.CTkLabel(
           self,
           text="Cook Time:",
           font=("Arial", 14, "bold")
       ).pack(pady=(20,5), padx=20, anchor="w")
      
       time_frame = customtkinter.CTkFrame(self, fg_color="transparent")
       time_frame.pack(pady=5)


       self.min_entry = customtkinter.CTkEntry(
           time_frame,
           width=60,
           placeholder_text="0"
       )
       self.min_entry.pack(side="left", padx=5)
       customtkinter.CTkLabel(time_frame, text="min").pack(side="left")


       self.sec_entry = customtkinter.CTkEntry(
           time_frame,
           width=60,
           placeholder_text="0"
       )
       self.sec_entry.pack(side="left", padx=(15, 5))
       customtkinter.CTkLabel(time_frame, text="sec").pack(side="left")

       self.error_label = customtkinter.CTkLabel(
           self,
           text="",
           text_color="#FF4444", 
           font=("Arial", 12, "bold")
       )
       self.error_label.pack(pady=5)

       btn_frame = customtkinter.CTkFrame(self, fg_color="transparent")
       btn_frame.pack(fill="x", padx=20, pady=30)

       if self.on_delete:
           customtkinter.CTkButton(
               btn_frame,
               text="Delete",
               fg_color="#8B0000",
               hover_color="red",
               width=80,
               command=self.confirm_delete
           ).pack(side="left")

       customtkinter.CTkButton(
           btn_frame,
           text="Save",
           fg_color="#4B0082",
           width=100,
           command=self.confirm_add
       ).pack(side="right")

       customtkinter.CTkButton(
           btn_frame,
           text="Cancel",
           fg_color="transparent",
           border_width=1,
           border_color="gray",
           text_color="gray80",
           width=80,
           command=self.destroy
       ).pack(side="right", padx=10)

       

   def confirm_add(self):
       desc = self.desc_text.get("1.0", "end-1c")
       mins = self.min_entry.get()
       secs = self.sec_entry.get()

       if mins == "": mins = "0"
       if secs == "": secs = "0"

       try:
           mins = int(mins)
           secs = int(secs)
       except ValueError:
           self.error_label.configure(text="Time must be numbers")
           return

       if desc.strip() == "":
           self.error_label.configure(text="Description cannot be empty")
           return

       new_instruction = Instruction(self.step_number, desc, mins, secs)
       self.on_add(new_instruction)
       self.destroy()

   def confirm_delete(self):
       if self.on_delete:
           self.on_delete()
           self.destroy()


class CategoryDialog(customtkinter.CTkToplevel):
   def __init__(self, parent, on_confirm):
       super().__init__(parent)
       self.on_confirm = on_confirm
      
       self.title("Set Category")
       self.geometry("400x400")
       self.attributes("-topmost", True)
       self.resizable(False, False)

       # 1. Cuisine
       customtkinter.CTkLabel(
           self,
           text="Cuisine:",
           font=("Arial", 14, "bold")
       ).pack(pady=(20,5))
       self.cuisine_var = customtkinter.StringVar(value=CUISINE_LIST[0])
       customtkinter.CTkOptionMenu(
           self,
           values=CUISINE_LIST,
           variable=self.cuisine_var
       ).pack(pady=5)

       # 2. Course
       customtkinter.CTkLabel(
           self,
           text="Course:",
           font=("Arial", 14, "bold")
       ).pack(pady=(20,5))
       self.course_var = customtkinter.StringVar(value=COURSE_LIST[0])
       customtkinter.CTkOptionMenu(
           self,
           values=COURSE_LIST,
           variable=self.course_var
       ).pack(pady=5)

       # 3. Difficulty
       customtkinter.CTkLabel(
           self,
           text="Difficulty:",
           font=("Arial", 14, "bold")
       ).pack(pady=(20,5))
       self.diff_var = customtkinter.StringVar(value=DIFFICULTY_LIST[0])
       customtkinter.CTkOptionMenu(
           self,
           values=DIFFICULTY_LIST,
           variable=self.diff_var
       ).pack(pady=5)

       # --- BUTTONS ROW ---
       btn_frame = customtkinter.CTkFrame(self, fg_color="transparent")
       btn_frame.pack(fill="x", padx=40, pady=40)

       # Save
       customtkinter.CTkButton(
           btn_frame,
           text="Confirm",
           fg_color="#4B0082",
           command=self.confirm_selection
       ).pack(side="right")

       # Cancel
       customtkinter.CTkButton(
           btn_frame,
           text="Cancel",
           fg_color="transparent",
           border_width=1,
           border_color="gray",
           text_color="gray80",
           width=80,
           command=self.destroy
       ).pack(side="right", padx=10)


   def confirm_selection(self):
       new_category = Category(
           cuisine=self.cuisine_var.get(),
           course=self.course_var.get(),
           difficulty=self.diff_var.get()
       )
       self.on_confirm(new_category)
       self.destroy()