import tkinter as tk
import time
import random
import getpass
import sys

def saturate_message(duration_seconds, message):
    """Displays a custom message with animations, random placements, and a festive effect."""
    root = tk.Tk()
    root.title(message)

    # Make the window fullscreen and transparent
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.8)  # Transparency
    root.configure(bg="black")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    username = getpass.getuser()

    colors = ["red", "green", "gold", "white"]
    fonts = ["Helvetica", "Times", "Comic Sans MS", "Courier"]

    labels = []

    # Create Christmas lights effect
    lights = []
    for _ in range(50):
        light = tk.Label(root, text="\u25CF", font=("Arial", 12), fg=random.choice(colors), bg="black")
        light.place(x=random.randint(0, screen_width), y=random.randint(0, screen_height))
        lights.append(light)

    # Create moving text labels
    for _ in range(20):
        label = tk.Label(root, text=f"{message}, {username}!", font=(random.choice(fonts), random.randint(20, 40), "bold"), 
                         fg=random.choice(colors), bg="black")
        label.place(x=random.randint(0, screen_width - 200), y=random.randint(0, screen_height - 50))
        labels.append(label)

    end_time = time.time() + duration_seconds

    def animate():
        if time.time() < end_time:
            # Animate lights
            for light in lights:
                new_x = random.randint(0, screen_width)
                new_y = random.randint(0, screen_height)
                new_color = random.choice(colors)
                light.place(x=new_x, y=new_y)
                light.config(fg=new_color)

            # Animate text labels
            for label in labels:
                new_x = random.randint(0, screen_width - 200)
                new_y = random.randint(0, screen_height - 50)
                new_color = random.choice(colors)
                label.place(x=new_x, y=new_y)
                label.config(fg=new_color)

            root.after(200, animate)
        else:
            root.destroy()

    animate()
    root.mainloop()

if __name__ == "__main__":
    # Allow overriding duration and message via command-line arguments
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 15  # Default to 60 seconds
    custom_message = sys.argv[2] if len(sys.argv) > 2 else "Merry Christmas"
    saturate_message(duration, custom_message)
