import tkinter as tk
from tkinter import messagebox

# Window 1
root = tk.Tk()
root.title("Window 1")

# Labels
label1 = tk.Label(root, text="3!")
label1.pack()
label2 = tk.Label(root, text="2!")
label2.pack()
label3 = tk.Label(root, text="1!")
label3.pack()
label4 = tk.Label(root, text="BLAST OFF!")
label4.pack()

# Buttons and callback functions
def callback1():
    messagebox.showinfo("Callback 1", "You have entered Space")

def callback2():
    messagebox.showinfo("Callback 2", "You have entered the ISS")

def callback3():
    messagebox.showinfo("Callback 3", "You have left the Milky Way Galaxy")

def callback4():
    root.destroy()

button1 = tk.Button(root, text="Go to Space", command=callback1)
button1.pack()
button2 = tk.Button(root, text="Go into the ISS", command=callback2)
button2.pack()
button3 = tk.Button(root, text="Go outside of Galaxy", command=callback3)
button3.pack()
button4 = tk.Button(root, text="Exit", command=callback4)
button4.pack()

# Window 2
root2 = tk.Toplevel(root)
root2.title("Window 2")

# Images 
image1 = tk.PhotoImage(file="image1.png")
image2 = tk.PhotoImage(file="image2.png")

label_image1 = tk.Label(root2, image=image1)
label_image1.pack()
label_image2 = tk.Label(root2, image=image2)
label_image2.pack()

root.mainloop()
