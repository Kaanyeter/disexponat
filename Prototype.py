import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
import cv2

def capture_image():
        vidcap = cv2.VideoCapture(0)

        success, frame = vidcap.read()

        cv2.imshow("Webcam", frame)
        cv2.waitKey()
        cv2.destroyAllWindows()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)

        # you can specify the revision tag if you don't want the timm dependency
        processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
        model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)

        # convert outputs (bounding boxes and class logits) to COCO API
        # let's only keep detections with score > 0.9
        target_sizes = torch.tensor([image.size[::-1]])
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
        output = ""
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
                box = [round(i, 2) for i in box.tolist()]
                output += f"Detected {model.config.id2label[label.item()]} with confidence {round(score.item(), 3)} at location {box}"
        if output == "":
            output = "Ich konnte keine Objekte erkennen :("
        displaytext.set(output)
    

placeholder = "Nehmen sie ein Bild auf um die KI zu testen :)"
root = tk.Tk()
root.geometry("1080x720")
root.configure(bg="black")
root.title("KI Bilderkennung")
displaytext = tk.StringVar()
displaytext.set(placeholder)

label = tk.Label(root, text="KI Bilderkennung", font=("Arial", 20), bg="black", fg="white")
label.pack(pady=20)
out = tk.Label(root, textvariable=displaytext, font=("Arial", 20), bg="black", fg="white")
out.pack(pady=20)
Capturebutton = tk.Button(root, text="Capture a Picture", command=lambda:capture_image())
Capturebutton.pack(padx=10, pady=100)
root.mainloop()