import tkinter as tk
from tkinter import messagebox  # Needed for the popup
import customtkinter
from frontend.dialogs import IngredientDialog, InstructionDialog, CategoryDialog


class RecipeGUI:


   def __init__(self, root, recipe_data, on_back, on_delete, on_update):
       self.root = root
       self.recipe_data = recipe_data 
       self.on_back = on_back
       self.on_delete = on_delete
       self.on_update = on_update
      
       self.root.title(self.recipe_data.get('name', "Recipe"))
       self.root.geometry("700x700")
       self.root.resizable(width=False, height=True)

       # --- HEADER FRAME ---
       header_frame = customtkinter.CTkFrame(
           self.root,
           fg_color="transparent"
       )
       header_frame.pack(fill="x", padx=20, pady=(20, 0))


       back_btn = customtkinter.CTkButton(
           header_frame,
           text="← Back",
           width=50,
           height=20,
           fg_color="transparent",
           text_color="gray70",
           anchor="w",
           command=self.on_back
       )
       back_btn.pack(side="left")

       delete_btn = customtkinter.CTkButton(
           header_frame,
           text="Delete Recipe",
           width=80,
           height=25,
           fg_color="#8B0000",
           hover_color="#FF0000",
           font=("Arial", 12, "bold"),
           command=self.confirm_delete_click
       )
       delete_btn.pack(side="right")
       # --- TITLE ---
       title_recipe = customtkinter.CTkLabel(
           master=self.root,
           text=self.recipe_data.get('name', 'Unknown'),
           font=("Rosela", 40)
       )
       title_recipe.pack(pady=(10,0), padx=(100,0), anchor="w")
       # --- CATEGORY SECTION ---
       category_frame = customtkinter.CTkFrame(
           master=self.root,
           fg_color="transparent"
       )
       category_frame.pack(pady=(30, 10), padx=(100, 0), anchor="w")

       def category_text_container(parent, label_text, value_text):
           pill_frame = customtkinter.CTkFrame(
               parent,
               fg_color="transparent"
           )
           pill_frame.pack(side="left", padx=(0, 30))
           customtkinter.CTkLabel(
               pill_frame,
               text=label_text.upper(),
               font=("Arial", 10, "bold"),
               text_color="gray60",
               height=10
           ).pack(anchor="w")
           customtkinter.CTkLabel(
               pill_frame,
               text=value_text,
               font=("Arial", 16),
               text_color="white"
           ).pack(anchor="w")

       category_text_container(category_frame, "Cuisine", self.recipe_data.get('cuisine', '-'))
       category_text_container(category_frame, "Course", self.recipe_data.get('course', '-'))
       category_text_container(category_frame, "Difficulty", self.recipe_data.get('difficulty', '-'))

       edit_cat_btn = customtkinter.CTkButton(
           category_frame,
           text="Edit",
           width=50,
           height=25,
           fg_color="gray30",
           hover_color="gray40",
           font=("Arial", 12),
           command=self.open_category_dialog
       )
       edit_cat_btn.pack(side="left", anchor="center")

       # --- INGREDIENTS SECTION ---
       ingredient_frame = customtkinter.CTkFrame(
           master=self.root,
           fg_color="transparent"
       )
       ingredient_frame.pack(fill="x", padx=100, pady=(20,0))

       header_ingredient_frame = customtkinter.CTkFrame(
           master=ingredient_frame,
           fg_color="transparent"
       )
       header_ingredient_frame.pack(fill="x", pady=(0,5))

       customtkinter.CTkLabel(
           master=header_ingredient_frame,
           text="INGREDIENTS",
           font=("Arial", 20, "bold")
       ).pack(side="left", anchor="w")

       add_ingredient_btn = customtkinter.CTkButton(
           master=header_ingredient_frame,
           text="+",
           width=40,
           fg_color="gray30",
           hover_color="gray40",
           command=self.open_add_ingredient_dialog
       )
       add_ingredient_btn.pack(side="right", anchor="e")

       line = customtkinter.CTkFrame(
           master=ingredient_frame,
           height=2,
           fg_color="gray50"
       )
       line.pack(fill="x", pady=(0, 15))

       # --- INGREDIENTS LOOP ---
       for index, item in enumerate(self.recipe_data.get('ingredients', [])):
           row = customtkinter.CTkFrame(
               ingredient_frame,
               fg_color="transparent"
           )
           row.pack(fill="x", pady=2)
          
           lbl = customtkinter.CTkLabel(
               row,
               text=f"•  {item}",
               font=("Arial", 16),
               anchor="w"
           )
           lbl.pack(side="left", fill="x", expand=True)


           edit_btn = customtkinter.CTkButton(
               row,
               text="Edit",
               width=40,
               height=20,
               font=("Arial", 10),
               fg_color="transparent",
               text_color="#242424",
               hover=False,
               command=lambda i=index: self.open_edit_ingredient_dialog(i)
           )
           edit_btn.pack(side="right", padx=5)

           def on_enter(e, btn=edit_btn):
               btn.configure(fg_color="gray30", text_color="white")
          
           def on_leave(e, btn=edit_btn):
               btn.configure(fg_color="transparent", text_color="#242424")


           row.bind("<Enter>", on_enter)
           row.bind("<Leave>", on_leave)
           lbl.bind("<Enter>", on_enter)
           lbl.bind("<Leave>", on_leave)
           edit_btn.bind("<Enter>", on_enter)


       # --- INSTRUCTIONS SECTION ---
       instructions_frame = customtkinter.CTkFrame(
           master=self.root,
           fg_color="transparent"
       )
       instructions_frame.pack(fill="x", padx=100, pady=(20,0))


       header_instructions_frame = customtkinter.CTkFrame(
           master=instructions_frame,
           fg_color="transparent"
       )
       header_instructions_frame.pack(fill="x", pady=(0,5))


       customtkinter.CTkLabel(
           master=header_instructions_frame,
           text="INSTRUCTIONS",
           font=("Arial", 20, "bold")
       ).pack(side="left", anchor="w")


       add_instructions_btn = customtkinter.CTkButton(
           master=header_instructions_frame,
           text="+",
           width=40,
           fg_color="gray30",
           hover_color="gray40",
           command=self.open_add_instruction_dialog
       )
       add_instructions_btn.pack(side="right", anchor="e")


       line = customtkinter.CTkFrame(
           master=instructions_frame,
           height=2,
           fg_color="gray50"
       )
       line.pack(fill="x", pady=(0, 15))


       # --- INSTRUCTIONS LOOP ---
       for index, step in enumerate(self.recipe_data.get('instructions', []), start=1):
           row = customtkinter.CTkFrame(
               instructions_frame,
               fg_color="transparent"
           )
           row.pack(fill="x", pady=2)
          
           lbl = customtkinter.CTkLabel(
               row,
               text=f"{index}. {step}",
               font=("Arial", 16),
               anchor="w",
               wraplength=450
           )
           lbl.pack(side="left", fill="x", expand=True)

           edit_btn = customtkinter.CTkButton(
               row,
               text="Edit",
               width=40,
               height=20,
               font=("Arial", 10),
               fg_color="transparent",
               text_color="#242424",
               hover=False,
               command=lambda i=index-1: self.open_edit_instruction_dialog(i)
           )
           edit_btn.pack(side="right", padx=5)

           def on_enter(e, btn=edit_btn):
               btn.configure(fg_color="gray30", text_color="white")
          
           def on_leave(e, btn=edit_btn):
               btn.configure(fg_color="transparent", text_color="#242424")

           row.bind("<Enter>", on_enter)
           row.bind("<Leave>", on_leave)
           lbl.bind("<Enter>", on_enter)
           lbl.bind("<Leave>", on_leave)
           edit_btn.bind("<Enter>", on_enter)
           edit_btn.bind("<Leave>", on_leave)




  
   def confirm_delete_click(self):
       answer = tk.messagebox.askyesno(
           title="Confirm Delete",
           message=f"Are you sure you want to delete '{self.recipe_data.get('name')}'?\nThis cannot be undone."
       )
      
       if answer:
           self.on_delete(self.recipe_data.get('name'))




   # --- LOGIC FUNCTIONS ---


   # 1. CATEGORY
   def open_category_dialog(self):
       CategoryDialog(
           self.root,
           on_confirm=self.handle_category_update
       )


   def handle_category_update(self, category_obj):
       self.recipe_data['cuisine'] = category_obj.cuisine
       self.recipe_data['course'] = category_obj.course
       self.recipe_data['difficulty'] = category_obj.difficulty
       self.on_update(self.recipe_data)


   # 2. INGREDIENTS
   def open_add_ingredient_dialog(self):
       IngredientDialog(
           self.root,
           on_add=self.handle_add_ingredient
       )


   def handle_add_ingredient(self, ingredient_obj):
       if 'ingredients' not in self.recipe_data:
           self.recipe_data['ingredients'] = []
       self.recipe_data['ingredients'].append(str(ingredient_obj))
       self.on_update(self.recipe_data)


   def open_edit_ingredient_dialog(self, index):
       # REPLACE Logic
       def handle_replace(ingredient_obj):
           self.recipe_data['ingredients'][index] = str(ingredient_obj)
           self.on_update(self.recipe_data)
      
       # DELETE Logic
       def handle_delete():
           del self.recipe_data['ingredients'][index]
           self.on_update(self.recipe_data)


       IngredientDialog(
           self.root,
           on_add=handle_replace,
           on_delete=handle_delete
       )


   # 3. INSTRUCTIONS
   def open_add_instruction_dialog(self):
       next_step = len(self.recipe_data.get('instructions', [])) + 1
       InstructionDialog(
           self.root,
           step_number=next_step,
           on_add=self.handle_add_instruction
       )


   def handle_add_instruction(self, instruction_obj):
       desc = instruction_obj.description
       if instruction_obj.time.get_total_seconds() > 0:
           desc += f" ({instruction_obj.time.minute}m {instruction_obj.time.second}s)"
      
       if 'instructions' not in self.recipe_data:
           self.recipe_data['instructions'] = []
       self.recipe_data['instructions'].append(desc)
       self.on_update(self.recipe_data)


   def open_edit_instruction_dialog(self, index):
       # REPLACE Logic
       def handle_replace(instruction_obj):
           desc = instruction_obj.description
           if instruction_obj.time.get_total_seconds() > 0:
               desc += f" ({instruction_obj.time.minute}m {instruction_obj.time.second}s)"
           self.recipe_data['instructions'][index] = desc
           self.on_update(self.recipe_data)


       # DELETE Logic
       def handle_delete():
           del self.recipe_data['instructions'][index]
           self.on_update(self.recipe_data)


       InstructionDialog(
           self.root,
           step_number=index+1,
           on_add=handle_replace,
           on_delete=handle_delete
       )
