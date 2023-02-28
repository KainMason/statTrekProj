# Import necessary libraries
import json
from matplotlib import widgets
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load data from JSON files into DataFrames
with open('species.json', 'r') as f:
    species_data = pd.read_json(f)

with open('stData.json', 'r') as f:
    st_data = pd.read_json(f)

# Create a list of Star Trek species
species_list = species_data['name'].tolist()

# Create a list of Star Trek characters and their episodes
characters = [char['name'] for char in st_data['characters']]
episodes = [char['episodes'] for char in st_data['characters']]

# Create the main application window
root = tk.Tk()
root.title('Star Trek Info')

# Create a notebook to hold the tabs
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=1)

# Create the Home tab
home_tab = ttk.Frame(notebook)
notebook.add(home_tab, text='Home')

# Add a welcome message and instructions to the Home tab
home_label = ttk.Label(home_tab, text='Welcome to the Star Trek Info app!')
home_label.pack(padx=20, pady=20)

home_text = ttk.Label(home_tab, text='Use the tabs to explore information about various Star Trek species and characters.')
home_text.pack(padx=20, pady=20)
home_text = ttk.Label(home_tab, text='Please note that the information presented on this website was collected through unofficial channels \n and may not be entirely accurate or up-to-date. \n We have made every effort to ensure the information is as reliable as possible, but we encourage users to verify it with other sources and to use their own judgment when making decisions based on this information.')
home_text.pack(padx=20, pady=20)
# Create the Species tab
species_tab = ttk.Frame(notebook)
notebook.add(species_tab, text='Species')

# Add a combobox to select a species
species_label = ttk.Label(species_tab, text='Select a species:')
species_label.pack()

species_combo = ttk.Combobox(species_tab, values=species_list)
species_combo.pack()

# Add a textbox to display the species description
species_textbox = tk.Text(species_tab, height=10, width=50)
species_textbox.pack()

# Define a function to display the selected species' description
def show_species_info(event):
    name = species_combo.get()
    description = species_data.loc[species_data['name'] == name, 'description'].item()
    species_textbox.delete('1.0', tk.END)
    species_textbox.insert(tk.END, description)

# Bind the function to the species combobox selection
species_combo.bind('<<ComboboxSelected>>', show_species_info)

# Create the Characters tab
st_tab = ttk.Frame(notebook)
notebook.add(st_tab, text='Characters')

# Create a horizontal bar plot of the number of episodes per character
fig, ax = plt.subplots()
ax.barh(characters, episodes, color='blue')
for i, v in enumerate(episodes):
    ax.text(v + 3, i, str(v), color='white', fontweight='bold')
ax.set_xlabel('Number of Episodes')
ax.set_ylabel('Character')
ax.set_title('Star Trek Characters by Number of Episodes')
plt.subplots_adjust(left=0.3)

# Define a function to show a message box with the selected character's number of episodes
def on_select(event):
    bar = event.artist
    index = bar.get_y().tolist().index(event.mouseevent.ydata)
    name = characters[index]
    num_episodes = episodes[index]
    message = f'{name} appears in {num_episodes} episodes.'
    tk.messagebox
# Bind a Matplotlib widget to allow for interactive selection of characters
widgets.RectangleSelector(ax, on_select)

# Create a canvas to display the Characters tab
canvas = FigureCanvasTkAgg(fig, master=st_tab)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Configure row and column weights for all tabs
for i in range(notebook.index('end')):
    tab = notebook.nametowidget(notebook.tabs()[i])
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_rowconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()