import customtkinter
import json
import os
from frontend.registerGUI import RegisterGUI
from frontend.recipebookGUI import RecipeBookGUI
from frontend.recipeGUI import RecipeGUI
from frontend.addRecipeGUI import AddRecipeGUI


class App:
   def __init__(self, root):
       self.root = root
       self.user = None
       self.filepath = os.path.join("backend", "database.json")
      
       try:
           with open(self.filepath, "r") as f:
               self.db = json.load(f)
       except:
           self.db = {}

       self.start_login()

   def start_login(self):
       self.clean_screen()
       RegisterGUI(self.root, on_login_success=self.open_book)

   def open_book(self, username):
       self.clean_screen()
       self.user = username
      
       if username in self.db:
           data = self.db[username].get("recipes", {})
           recipe_names = list(data.keys())
       else:
           recipe_names = []

       RecipeBookGUI(
           self.root,
           recipe_list=recipe_names,
           on_recipe_select=self.view_recipe,
           on_add_recipe=self.go_to_add
       )

   def go_to_add(self):
       self.clean_screen()
      
       AddRecipeGUI(
           self.root,
           on_back=lambda: self.open_book(self.user),
           on_save_success=self.save_data
       )

   def save_data(self, recipe_obj):
       ing_list = []
       for item in recipe_obj.ingredient_list:
           s = f"{item.quantity} {item.unit} {item.name}"
           ing_list.append(s)

       inst_list = []
       for step in recipe_obj.full_instructions:
           inst_list.append(step.description)
       temp_dict = {
           "name": recipe_obj.name,
           "description": recipe_obj.description,
           "cuisine": recipe_obj.category.cuisine,
           "course": recipe_obj.category.course,
           "difficulty": recipe_obj.category.difficulty,
           "ingredients": ing_list,  
           "instructions": inst_list  
       }

       self.db[self.user]["recipes"][recipe_obj.name] = temp_dict
      
       with open(self.filepath, "w") as f:
           json.dump(self.db, f, indent=4)
       self.open_book(self.user)

   def update_data(self, recipe_name, new_data):
       self.db[self.user]["recipes"][recipe_name] = new_data
       with open(self.filepath, "w") as f:
           json.dump(self.db, f, indent=4)
       self.view_recipe(recipe_name)

   def view_recipe(self, recipe_name):
       self.clean_screen()
       current_data = self.db[self.user]["recipes"][recipe_name]
       RecipeGUI(
           self.root,
           current_data,
           on_back=lambda: self.open_book(self.user),
           on_delete=self.delete_item,
           on_update=lambda x: self.update_data(recipe_name, x)
       )

   def delete_item(self, name):
       if name in self.db[self.user]["recipes"]:
           del self.db[self.user]["recipes"][name]
           with open(self.filepath, "w") as f:
               json.dump(self.db, f, indent=4)
           print("deleted")
           self.open_book(self.user)

   def clean_screen(self):
       for widget in list(self.root.winfo_children()):
           try:
               widget.destroy()
           except Exception as e:
                print(f"error destroying widget: {e}")

if __name__ == "__main__":
   customtkinter.set_appearance_mode("dark")
   customtkinter.set_default_color_theme("dark-blue")

   root = customtkinter.CTk()
   app = App(root)
   root.mainloop()
