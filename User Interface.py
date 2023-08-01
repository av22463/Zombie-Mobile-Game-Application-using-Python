import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Zombie Survival Game")

# Set the window size and position it at the center of the screen
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a custom font for the title
title_font = ("Helvetica", 24, "bold")

# Create a label to display the game title
title_label = tk.Label(root, text="Zombie Survival Game", font=title_font)
title_label.pack(pady=40)

# Create a button to start the game
start_button = tk.Button(root, text="Start Game", width=20, height=2)
start_button.pack(pady=10)

# Create a label to display the player's score
score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Create a button to exit the game
exit_button = tk.Button(root, text="Exit Game", width=20, height=2, command=root.destroy)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
