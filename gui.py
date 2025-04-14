import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import csv  

# Initialize the main app
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Data Recorder")
        self.geometry("600x400")

        # Data storage
        self.data = []

        # Frames
        self.left_pane = ctk.CTkFrame(self, width=150)
        self.main_frame = ctk.CTkFrame(self)
        self.records_frame = ctk.CTkFrame(self)

        self.setup_left_pane()
        self.setup_main_frame()
        self.setup_records_frame()

        self.left_pane.pack(side="left", fill="y")
        self.show_main_frame()

    def setup_left_pane(self):
        self.view_button = ctk.CTkButton(self.left_pane, text="View Records", command=self.show_records_frame)
        self.view_button.pack(pady=10, padx=10)

        self.export_button = ctk.CTkButton(self.left_pane, text="Export to CSV", command=self.export_to_csv)
        self.export_button.pack(pady=10, padx=10)

    def setup_main_frame(self):
        # Input Fields
        self.name_label = ctk.CTkLabel(self.main_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ctk.CTkEntry(self.main_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.age_label = ctk.CTkLabel(self.main_frame, text="Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = ctk.CTkEntry(self.main_frame)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.duration_label = ctk.CTkLabel(self.main_frame, text="Duration:")
        self.duration_label.grid(row=2, column=0, padx=10, pady=10)
        self.duration_entry = ctk.CTkEntry(self.main_frame)
        self.duration_entry.grid(row=2, column=1, padx=10, pady=10)

        self.id_label = ctk.CTkLabel(self.main_frame, text="ID:")
        self.id_label.grid(row=3, column=0, padx=10, pady=10)
        self.id_entry = ctk.CTkEntry(self.main_frame)
        self.id_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = ctk.CTkButton(self.main_frame, text="Add Record", command=self.add_record)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def setup_records_frame(self):
        self.tree = ttk.Treeview(self.records_frame, columns=("Name", "Age", "Duration", "ID"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Duration", text="Duration")
        self.tree.heading("ID", text="ID")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.delete_button = ctk.CTkButton(self.records_frame, text="Delete Selected", command=self.delete_record)
        self.delete_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self.records_frame, text="Back", command=self.show_main_frame)
        self.back_button.pack(pady=10)

    def show_main_frame(self):
        self.records_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def show_records_frame(self):
        self.main_frame.pack_forget()
        self.update_records_view()
        self.records_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def add_record(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        duration = self.duration_entry.get()
        record_id = self.id_entry.get()

        if name and age and duration and record_id:
            self.data.append({"Name": name, "Age": age, "Duration": duration, "ID": record_id})
            messagebox.showinfo("Success", "Record added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill all fields!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)

    def update_records_view(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for record in self.data:
            self.tree.insert("", tk.END, values=(record["Name"], record["Age"], record["Duration"], record["ID"]))

    def delete_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                values = self.tree.item(item, "values")
                self.data = [record for record in self.data if record["ID"] != values[3]]
                self.tree.delete(item)
            messagebox.showinfo("Success", "Record deleted successfully!")
        else:
            messagebox.showwarning("Warning", "No record selected!")

    def export_to_csv(self):
        if not self.data:
            messagebox.showwarning("Warning", "No data to export!")
            return

        try:
            with open("exported_data.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Duration", "ID"])
                writer.writeheader()
                writer.writerows(self.data)
            messagebox.showinfo("Success", "Data exported to 'exported_data.csv' successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
