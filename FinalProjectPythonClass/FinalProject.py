import tkinter as tk
from tkinter import messagebox, ttk

class IceCreamOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kevin's Creamy Confections Order System")
        self.create_main_window()

    def create_main_window(self):
        # the main window frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Welcome label
        welcome_label = tk.Label(self.main_frame, text="Welcome to Kevin's Creamy Confections!", font=("Arial", 14))
        welcome_label.pack(pady=10)

        # Order button
        order_button = tk.Button(self.main_frame, text="Order Now", command=self.create_order_window)
        order_button.pack(pady=5)

        # Exit button
        exit_button = tk.Button(self.main_frame, text="Exit", command=self.root.quit)
        exit_button.pack(pady=5)

    def create_order_window(self):
        # Destroy main window frame and create order window frame
        self.main_frame.destroy()
        self.order_frame = tk.Frame(self.root)
        self.order_frame.pack()

        # Order header label
        tk.Label(self.order_frame, text="Place Your Order", font=("Arial", 14)).pack(pady=10)

        # Radio buttons for pickup or dine-in
        self.pickup_dinein = tk.StringVar(value="Pickup")
        tk.Radiobutton(self.order_frame, text="Pickup", variable=self.pickup_dinein, value="Pickup").pack(anchor=tk.W)
        tk.Radiobutton(self.order_frame, text="Dine-in", variable=self.pickup_dinein, value="Dine-in").pack(anchor=tk.W)

        # Combo box for choosing size
        tk.Label(self.order_frame, text="Choose Size:").pack(anchor=tk.W)
        self.size_var = tk.StringVar(value="One Scoop")
        size_options = ["One Scoop", "Two Scoops", "Three Scoops"]
        ttk.Combobox(self.order_frame, textvariable=self.size_var, values=size_options).pack(anchor=tk.W)

        # Checkboxes for choosing toppings
        tk.Label(self.order_frame, text="Choose Type:").pack(anchor=tk.W)
        self.type_var = tk.StringVar(value="Cone")
        type_options = ["Cone", "Sundae"]
        ttk.Combobox(self.order_frame, textvariable=self.type_var, values=type_options).pack(anchor=tk.W)
        
        # Checkboxes for choosing toppings
        tk.Label(self.order_frame, text="Choose Toppings:").pack(anchor=tk.W)
        self.toppings = {}
        toppings_list = ["Nuts", "Chocolate", "Strawberry Syrup", "Pineapple Syrup", "Whipped Cream", "Sprinkles", "Sugar Cookies", "Bananas", "Cherry"]
        for topping in toppings_list:
            self.toppings[topping] = tk.BooleanVar()
            tk.Checkbutton(self.order_frame, text=topping, variable=self.toppings[topping]).pack(anchor=tk.W)

        # Submit order and back buttons
        tk.Button(self.order_frame, text="Submit Order", command=self.create_confirmation_window).pack(pady=5)
        tk.Button(self.order_frame, text="Back", command=self.create_main_window).pack(pady=5)

    def create_confirmation_window(self):
        # Generate order summary
        order_summary = f"Order Type: {self.pickup_dinein.get()}\n"
        order_summary += f"Size: {self.size_var.get()}\n"
        order_summary += f"Type: {self.type_var.get()}\n"
        order_summary += "Toppings:\n"
        for topping, selected in self.toppings.items():
            if selected.get():
                order_summary += f"- {topping}\n"

        # Destroy order window frame and create confirmation window frame
        self.order_frame.destroy()
        self.confirmation_frame = tk.Frame(self.root)
        self.confirmation_frame.pack()

        # Confirmation message label
        tk.Label(self.confirmation_frame, text="Order Confirmation", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.confirmation_frame, text=order_summary, justify=tk.LEFT).pack(pady=10)

        # Confirm, edit, and exit buttons
        tk.Button(self.confirmation_frame, text="Confirm", command=self.confirm_order).pack(pady=5)
        tk.Button(self.confirmation_frame, text="Edit Order", command=self.create_order_window).pack(pady=5)
        tk.Button(self.confirmation_frame, text="Exit", command=self.root.quit).pack(pady=5)

    def confirm_order(self):
        # Display order confirmed message
        messagebox.showinfo("Order Confirmed", "Thank you for your order!")
        self.create_main_window()

if __name__ == "__main__":
    # Create the main tkinter window and start the application
    root = tk.Tk()
    app = IceCreamOrderApp(root)
    root.mainloop()
