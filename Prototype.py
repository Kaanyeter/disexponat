import tkinter as tk
from backend import capture_image
from tkinter_webcam import webcam
from time import sleep
import cv2
import numpy as np
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1080x720")
root.configure(bg="black")
label = tk.Label(root, text="AI Visualization", font=("times new roman", 20, "bold"))
f1 = tk.LabelFrame(root, bg="red")
f1.pack()
L1 = tk.Label(f1,bg="red")
L1.pack()
stream = cv2.VideoCapture(0)
Button = tk.Button(root, text="Capture a Picture", command=capture_image)
Button.pack()

while True:

    img = stream.read()[1]
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    L1["image"] = img
    root.update()