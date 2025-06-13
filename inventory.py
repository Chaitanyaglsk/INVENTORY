import tkinter as tk
from tkinter import messagebox
import random

# Dummy login details
users_db = {"admin": "admin123", "user": "pass"}

inventory = {}

class InventoryManager:
    def __init__(self, window):
        self.window = window
        window.title("Inventory Manager")
        window.geometry("450x450")

        self.user_logged_in = False
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Enter Username").pack()
        self.username_input = tk.Entry(self.window)
        self.username_input.pack()

        tk.Label(self.window, text="Enter Password").pack()
        self.password_input = tk.Entry(self.window, show="*")
        self.password_input.pack()

        tk.Button(self.window, text="Login", command=self.validate_login).pack(pady=10)

    def validate_login(self):
        username = self.username_input.get()
        password = self.password_input.get()
        if users_db.get(username) == password:
            self.user_logged_in = True
            self.main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def main_menu(self):
        self.clear_screen()
        tk.Button(self.window, text="Add Item", width=20, command=self.add_item_screen).pack(pady=5)
        tk.Button(self.window, text="Edit Item", width=20, command=self.edit_item_screen).pack(pady=5)
        tk.Button(self.window, text="Remove Item", width=20, command=self.remove_item_screen).pack(pady=5)
        tk.Button(self.window, text="Low Stock Alert", width=20, command=self.low_stock_alert).pack(pady=5)
        tk.Button(self.window, text="Exit", width=20, command=self.window.quit).pack(pady=5)

    def add_item_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Item Name").pack()
        item_name_input = tk.Entry(self.window)
        item_name_input.pack()
        tk.Label(self.window, text="Quantity").pack()
        quantity_input = tk.Entry(self.window)
        quantity_input.pack()

        def add_item():
            name = item_name_input.get()
            try:
                quantity = int(quantity_input.get())
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a number.")
                return
            item_id = random.randint(100, 999)
            inventory[item_id] = {"name": name, "quantity": quantity}
            messagebox.showinfo("Success", f"Item added with ID {item_id}.")
            self.main_menu()

        tk.Button(self.window, text="Add Item", command=add_item).pack()

    def edit_item_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Enter Item ID").pack()
        item_id_input = tk.Entry(self.window)
        item_id_input.pack()
        tk.Label(self.window, text="New Quantity").pack()
        new_quantity_input = tk.Entry(self.window)
        new_quantity_input.pack()

        def update_item():
            try:
                item_id = int(item_id_input.get())
                new_quantity = int(new_quantity_input.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid input.")
                return
            if item_id in inventory:
                inventory[item_id]["quantity"] = new_quantity
                messagebox.showinfo("Success", "Item quantity updated.")
            else:
                messagebox.showerror("Error", "Item ID not found.")
            self.main_menu()

        tk.Button(self.window, text="Update Item", command=update_item).pack()

    def remove_item_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Enter Item ID to remove").pack()
        item_id_input = tk.Entry(self.window)
        item_id_input.pack()

        def delete_item():
            try:
                item_id = int(item_id_input.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid Item ID.")
                return
            if item_id in inventory:
                del inventory[item_id]
                messagebox.showinfo("Success", "Item removed.")
            else:
                messagebox.showerror("Error", "Item ID not found.")
            self.main_menu()

        tk.Button(self.window, text="Remove Item", command=delete_item).pack()

    def low_stock_alert(self):
        self.clear_screen()
        tk.Label(self.window, text="Items with Low Stock (Less than 5)").pack()
        for item_id, details in inventory.items():
            if details["quantity"] < 5:
                tk.Label(self.window, text=f"ID {item_id} - {details['name']}: {details['quantity']}").pack()
        tk.Button(self.window, text="Back to Menu", command=self.main_menu).pack(pady=10)

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()


root = tk.Tk()
app = InventoryManager(root)
root.mainloop()
