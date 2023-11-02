import customtkinter as ctk

class MainFrame(ctk.CTkFrame) :
	def __init__(self, master):
		super().__init__(master)
		
		self.grid_columnconfigure(0, minsize=150, weight=1);
		self.grid_rowconfigure(0, minsize=150, weight=1);
		self.label = ctk.CTkLabel(master=self, text="main_frame", corner_radius=10, height=350, text_color="#ffffff", fg_color="#333333")
		self.label.grid(pady=10, padx=5, row=0, column=0, sticky="we")

class LeftFrame(ctk.CTkFrame) :
	def __init__(self, master):
		super().__init__(master)
		
		self.button = ctk.CTkButton(master=self, text="left frame")
		self.button.grid(row=0, column=0, sticky="e")

class RightFrame(ctk.CTkFrame) :
	def __init__(self, master):
		super().__init__(master)
		
		self.button = ctk.CTkButton(master=self, text="right frame")
		self.button.grid(row=0, column=0, sticky="e")
		