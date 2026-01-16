import tkinter as tk
import customtkinter


class RecipeBookGUI:


   def __init__(self, root, recipe_list, on_recipe_select=None, on_add_recipe=None):
       self.root = root
       self.recipe_list = recipe_list
       self.on_recipe_select = on_recipe_select
       self.on_add_recipe = on_add_recipe 
      
       self.root.title("Kira's Recipes")
       self.root.geometry("700x700")
       self.root.resizable(width=False, height=True)
      
       # TITLE
       title_main = customtkinter.CTkLabel(
           self.root,
           text="Recipe App",
           font=("Heavitas", 60)
       )
       title_main.pack(pady=(20, 0))
      
       subtitle_main = customtkinter.CTkLabel(
           self.root,
           text="Made by Kira"
       )
       subtitle_main.pack(pady=2)


       # HEADER BAR
       action_frame = customtkinter.CTkFrame(self.root, fg_color="transparent")
       action_frame.pack(fill="x", padx=40, pady=20)


       # search
       search_entry = customtkinter.CTkEntry(
           action_frame,
           placeholder_text="Search recipes...",
           width=300
       )
       search_entry.pack(side="left")


       # add recipe
       add_btn = customtkinter.CTkButton(
           action_frame,
           text="+ New Recipe",
           width=100,
           fg_color="#4B0082",
           command=self.on_add_recipe
       )
       add_btn.pack(side="right")


       # SCROLLABLE LIST
       self.scroll_frame = customtkinter.CTkScrollableFrame(
           self.root,
           width=600,
           height=400,
           fg_color="transparent"
       )
       self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)


       for recipe_name in self.recipe_list:
           self.recipe_card(recipe_name)


   def recipe_card(self, name):
       card = customtkinter.CTkFrame(
           self.scroll_frame,
           fg_color="gray20"
       )
       card.pack(fill="x", pady=5, padx=10)


       customtkinter.CTkLabel(
           master=card,
           text=name,
           font=("Arial", 18, "bold")
       ).pack(side="left", padx=20, pady=20)


       cook_btn = customtkinter.CTkButton(
           master=card,
           text="Cook",
           width=80,
           command=lambda: self.on_recipe_select(name) if self.on_recipe_select else None
       )
       cook_btn.pack(side="right", padx=20)
