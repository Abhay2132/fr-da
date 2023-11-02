import customtkinter as ctk
import ui_

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("800x400")
		self.title("Abhay")
		self.resizable(False, True)
		
		mainFrame = ui_.MainFrame(self)
		leftFrame = ui_.LeftFrame(self)
		rightFrame = ui_.RightFrame(self)
		
		self.grid_columnconfigure((0,2), minsize=150);
		self.grid_columnconfigure(1,minsize=500);
		self.grid_rowconfigure(0, minsize=150, weight=1);
		
		padx = 3
		pady = 6
		mainFrame.grid(padx=padx, pady=pady,row=0, column=1, sticky="nswe")
		leftFrame.grid(row=0, padx=padx, pady=pady,column=0, sticky="nswe")
		rightFrame.grid(row=0, padx=padx, pady=pady,column=2, sticky="nswe")
		
		
		
if __name__ == "__main__":
	# ctk.set_default_color_theme("green")
	ctk.set_appearance_mode("light")
	app = App()
	app.mainloop()