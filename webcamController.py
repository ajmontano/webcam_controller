import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import cv2

# Define the dimensions, in pixels, of a full screen
width = 1920
height = 1080

# Define the focus level of the camera
focus = 0
FOCUS = 5
FOCUS_MIN = 0
FOCUS_MAX = 255

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Change the focus
cap.set(cv2.CAP_PROP_FOCUS, focus) 

root = tk.Tk()

# Setup the image frame
imageFrame = tk.Frame(root, width=width, height=height)
imageFrame.grid(row=0, column=0, padx=10, pady=10)

lmain = tk.Label(root)
lmain.grid(row=0, column=0)

def show_frame():
    # Capture frame-by-frame
    retVal, frame = cap.read()

    # Convert the frame into a an ImageTk
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imageTk = ImageTk.PhotoImage(image=img)
    
    # Display the window
    lmain.imgtk = imageTk
    lmain.configure(image=imageTk)
    lmain.after(10, show_frame)

# Run the display loop
show_frame()
root.mainloop()

# When finished, release the capture
cap.release()
