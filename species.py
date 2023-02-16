import json
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Read the JSON file
with open('stData.json', 'r') as f:
    data = json.load(f)

# Create a list of characters and their episodes
characters = []
episodes = []
for character in data['characters']:
    characters.append(character['name'])
    episodes.append(character['episodes'])

# Create a Tkinter window
root = tk.Tk()
root.geometry('400x400')
root.title('Star Trek Characters')

# Set the default mode to light
dark_mode = False

# Function to toggle the mode
def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(background='#1F1F1F')
        button.config(text='Light Mode', background='#E0E0E0', foreground='#1F1F1F')
        ax.set_facecolor('#1F1F1F')
        fig.set_facecolor('#1F1F1F')
        plt.rcParams['text.color'] = 'w'
        plt.rcParams['axes.labelcolor'] = 'w'
        plt.rcParams['xtick.color'] = 'w'
        plt.rcParams['ytick.color'] = 'w'
    else:
        root.config(background='#E0E0E0')
        button.config(text='Dark Mode', background='#1F1F1F', foreground='#E0E0E0')
        ax.set_facecolor('#E0E0E0')
        fig.set_facecolor('#E0E0E0')
        plt.rcParams['text.color'] = 'k'
        plt.rcParams['axes.labelcolor'] = 'k'
        plt.rcParams['xtick.color'] = 'k'
        plt.rcParams['ytick.color'] = 'k'
    fig.canvas.draw()

# Create a figure and axis
fig, ax = plt.subplots()

# Create a horizontal bar plot of the number of episodes per character
ax.barh(characters, episodes, color='blue')

# Add the number of episodes to each bar
for i, v in enumerate(episodes):
    ax.text(v + 3, i, str(v), color='black', fontweight='bold')

# Add labels and title
ax.set_xlabel('Number of Episodes')
ax.set_ylabel('Character')
ax.set_title('Star Trek Characters by Number of Episodes')

# Adjust the spacing between the bars
plt.subplots_adjust(left=0.3)

# Embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a toggle button for dark mode
button = tk.Button(root, text='Dark Mode', command=toggle_mode, background='#1F1F1F', foreground='#E0E0E0')
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
