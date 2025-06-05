import customtkinter as ctk

def create_compare_tab(self):
    label = ctk.CTkLabel(master=self.tab("compare"), text="Comparison Panel", font=self.fonts)
    label.pack(pady=10)