import tkinter as tk
import os
import random

# Create the main window
root = tk.Tk()
root.title("Dice Roller")
root.configure(bg='#24292e')  # Set the background color to dark GitHub theme
root.geometry('800x800')  # Set the size of the window

# Get the absolute path to the directory containing the dice images
dir_path = os.path.dirname(os.path.realpath(__file__))
dice_image_path = os.path.join(dir_path, 'images', 'dice{}.png')

# Create the label for the dice image
dice_label = tk.Label(root, bg='#24292e')
dice_label.pack(pady=20)

# Create the button to roll the dice
def roll_dice():
    dice_value = random.randint(1, 6)  # Generate a random number between 1 and 6
    dice_image = tk.PhotoImage(file=dice_image_path.format(dice_value))  # Load the corresponding dice image
    dice_label.configure(image=dice_image)
    dice_label.image = dice_image  # Keep a reference to the image to prevent garbage collection

roll_button = tk.Button(root, text="Roll the Dice", bg='#2ea44f', fg='white', font=('Arial', 16), command=roll_dice)
roll_button.pack(pady=10)

# Run the main event loop
root.mainloop()