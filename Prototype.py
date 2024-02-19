import tkinter as tk
from backend import capture_image
from tkinter_webcam import webcam

# Create the main window

window = tk.Tk()
window.title("AI Image Recognition")
window.geometry("800x600")

# Create a label to display the webcam feed

video_label = tk.Label(window)
video_label.pack()

# Create a label to display recognized objects

objects_label = tk.Label(window, text="Recognized Objects:")
objects_label.pack()

# Create buttons for yes and no

yes_button = tk.Button(window, text="Yes")
yes_button.pack(side=tk.LEFT)
no_button = tk.Button(window, text="No")
no_button.pack(side=tk.LEFT)

# Function to evaluate the captured image

def evaluate_image():
    # TODO: Add your AI model evaluation code here
    recognized_objects = ["object1", "object2", "object3"]

    # Update the recognized objects label
    objects_label.configure(text="Recognized Objects: " + ", ".join(recognized_objects))

# Bind the capture and evaluate functions to buttons
    
capture_button = tk.Button(window, text="Capture", command=capture_image)
capture_button.pack()
evaluate_button = tk.Button(window, text="Evaluate", command=evaluate_image)
evaluate_button.pack()

# Start the Tkinter event loop

window.mainloop()

# Importing backend functions to capture and evaluate images via the webcam and AI model

while True:
    video = webcam.Box(window, width=800, height=600)
    video.show_frames()
    capture_image()
