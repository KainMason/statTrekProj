import json
import tkinter as tk
from tkinter import ttk

def print_species_info(file_path):
    species_list = []
    with open(file_path, 'r') as file:
        species_data = json.load(file)
        for species in species_data:
            species_list.append(species['name'])
    return species_data, species_list

def show_description(event, species_data, textbox):
    name = species_combo.get()
    for species in species_data:
        if species['name'] == name:
            textbox.delete('1.0', tk.END)
            textbox.insert(tk.END, species['description'])

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Species Information")
    species_data, species_list = print_species_info('species.json')
    
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TLabel', background='#1C2331', foreground='white')
    style.configure('TCombobox', background='#1C2331', foreground='white')
    style.configure('TText', background='#1C2331', foreground='white')
    style.configure('TCheckbutton', background='#1C2331', foreground='white')
    
    species_label = ttk.Label(root, text="Select a species:")
    species_label.grid(row=0, column=0, padx=10, pady=10)
    
    species_combo = ttk.Combobox(root, values=species_list)
    
    species_combo.grid(row=0, column=1, padx=10, pady=10)
    species_combo.bind("<<ComboboxSelected>>", lambda event: show_description(event, species_data, textbox))
    
    textbox = tk.Text(root, height=10, width=70)
    textbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    root.configure(background='#1C2331')
    root.mainloop()
