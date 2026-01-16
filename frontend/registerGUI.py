import customtkinter
import json 
import os  


class RegisterGUI:
   def __init__(self, root, on_login_success):
       self.root = root
       self.on_login_success = on_login_success

       self.root.title("Welcome")
       self.root.geometry("700x700")
       self.root.resizable(width=False, height=True)

       title = customtkinter.CTkLabel(
           self.root,
           text="The Recipe Book",
           font=("Heavitas", 40)
       )
       title.pack(pady=(100, 20))

       self.tab_view = customtkinter.CTkTabview(
           self.root, 
           width=400, 
           height=400
        )
       self.tab_view.pack(pady=20)

       self.tab_view.add("Login")
       self.tab_view.add("Register")
       # login tab
       self.setup_login_tab()
       # register tab
       self.setup_register_tab()


   def setup_login_tab(self):
       login_frame = self.tab_view.tab("Login")
       #get username
       self.login_user_entry = customtkinter.CTkEntry(
           login_frame,
           placeholder_text="Username",
           width=300
       )
       self.login_user_entry.pack(pady=(40, 15))
       #get password
       self.login_pass_entry = customtkinter.CTkEntry(
           login_frame,
           placeholder_text="Password",
           width=300,
           show="*"
       )
       self.login_pass_entry.pack(pady=(0, 30))
       login_btn = customtkinter.CTkButton(
           login_frame,
           text="LOG IN",
           width=300,
           command=self.perform_login
       )
       login_btn.pack(pady=10)
       self.login_status_label = customtkinter.CTkLabel(
           login_frame, 
           text="", 
           text_color="red"
       )
       self.login_status_label.pack(pady=5)


   def setup_register_tab(self):
       reg_frame = self.tab_view.tab("Register")
       #make username
       self.reg_user_entry = customtkinter.CTkEntry(
           reg_frame,
           placeholder_text="Username",
           width=300
       )
       self.reg_user_entry.pack(pady=(30, 15))
       #make pass
       self.reg_pass_entry = customtkinter.CTkEntry(
           reg_frame,
           placeholder_text="Password",
           width=300,
           show="*"
       )
       self.reg_pass_entry.pack(pady=(0, 15))
       #retry pass
       self.reg_confirm_entry = customtkinter.CTkEntry(
           reg_frame,
           placeholder_text="Password",
           width=300,
           show="*"
       )
       self.reg_confirm_entry.pack(pady=(0, 30))
       reg_btn = customtkinter.CTkButton(
           reg_frame,
           text="CREATE ACCOUNT",
           command=self.perform_register
       )
       reg_btn.pack(pady=10)
       self.status_label = customtkinter.CTkLabel(
           reg_frame,
           text="",  #empatayyy
           font=("Arial", 12),
           text_color="red"
       )
       self.status_label.pack(pady=5)


   # --- Load Data ---
   def load_db(self):
       file_path = os.path.join("backend", "database.json")
       if not os.path.exists(file_path):
           return {}
       with open(file_path, "r") as file:
           return json.load(file)


   # --- Save Data ---
   def save_db(self, data):
       file_path = os.path.join("backend", "database.json")
       with open(file_path, "w") as file:
           json.dump(data, file, indent=4)




   # --- THE REAL LOGIC!!!!111 ---


   def perform_login(self):
       username = self.login_user_entry.get()
       password = self.login_pass_entry.get()
       db = self.load_db()
       if username in db and db[username]["password"] == password:
           print("login suces")
           self.on_login_success(username)
       else:
           self.login_status_label.configure(text="Invalid Username or Password")


   def perform_register(self):
       user = self.reg_user_entry.get()
       p1 = self.reg_pass_entry.get()
       p2 = self.reg_confirm_entry.get()
       if user == "" or p1 == "" or p2 == "":
           self.status_label.configure(text="Please fill in all fields!", text_color="red")
           return
       if p1 != p2:
           self.status_label.configure(text="Error: Passwords do not match.", text_color="red")
           return
       db = self.load_db()
       if user in db:
            self.status_label.configure(text="Error: Username already taken.", text_color="red")
            return
       db[user] = {
           "password": p1,
           "recipes": {}
       }
       self.save_db(db)
       self.status_label.configure(text="Success! Please log in.", text_color="green")