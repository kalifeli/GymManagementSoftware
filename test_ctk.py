import customtkinter as ctk


print("Inizio customtkinter")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("400x200")
label = ctk.CTkLabel(app, text="Test customtkinter")
label.pack(padx=20, pady=20)
app.mainloop()
print("Fine customtkinter")