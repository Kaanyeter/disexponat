import tkinter as tk
from backend import capture_image
from tkinter_webcam import webcam
from time import sleep

while True:
    sleep(2)
    capture_image()
    sleep(2)