#23121106_Balasubramanian V

import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
import re

# Declare entry variables as global
clearance_id_entry = None
exporter_entry = None
consignee_entry = None
invoice_no_entry = None
product_entry = None
quantity_entry = None
rate_entry = None
net_weight_entry = None
port_of_loading_entry = None
port_of_discharge_entry = None
container_no_entry = None
vessel_entry = None
status_entry = None
update_clearance_id_entry = None
new_status_entry = None
records_text = None
# Function to read data from file
def read_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = {}
            for line in file:
                values = line.strip().split(',')
                if len(values) != 13:
                    print("Error: Invalid data format in the file.")
                    return {}
                clearance_id, exporter, consignee, invoice_no, product, quantity, rate, net_weight, port_of_loading, port_of_discharge, container_no, vessel, status = values
                data[clearance_id] = {
                    "Exporter": exporter,
                    "Consignee": consignee,
                    "Invoice No": invoice_no,
                    "Product": product,
                    "Quantity": quantity,
                    "Rate": rate,
                    "Net Weight": net_weight,
                    "Port of Loading": port_of_loading,
                    "Port of Discharge": port_of_discharge,
                    "Container No": container_no,
                    "Vessel": vessel,
                    "Status": status
                }
            return data
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"Error: File '{file_name}' not found.")
        return {}

# Function to write data to file
def write_data(data, file_name):
    with open(file_name, 'w') as file:
        for clearance_id, details in data.items():
            file.write(f"{clearance_id},{details['Exporter']},{details['Consignee']},{details['Invoice No']},{details['Product']},{details['Quantity']},{details['Rate']},{details['Net Weight']},{details['Port of Loading']},{details['Port of Discharge']},{details['Container No']},{details['Vessel']},{details['Status']}\n")

# Function to add a new customs clearance record
def add_clearance_record():
    global clearance_id_entry, exporter_entry, consignee_entry, invoice_no_entry, product_entry, quantity_entry, rate_entry, net_weight_entry, port_of_loading_entry, port_of_discharge_entry, container_no_entry, vessel_entry, status_entry
    
    clearance_id = clearance_id_entry.get()
    exporter = exporter_entry.get()
    consignee = consignee_entry.get()
    invoice_no = invoice_no_entry.get()
    product = product_entry.get()
    quantity = quantity_entry.get()
    rate = rate_entry.get()
    net_weight = net_weight_entry.get()
    port_of_loading = port_of_loading_entry.get()
    port_of_discharge = port_of_discharge_entry.get()
    container_no = container_no_entry.get()
    vessel = vessel_entry.get()
    status = status_entry.get()
    
    if not all([clearance_id, exporter, consignee, invoice_no, product, quantity, rate, net_weight, port_of_loading, port_of_discharge, container_no, vessel, status]):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    if clearance_id in data:
        messagebox.showerror("Error", "Clearance ID already exists.")
        return
    
    
    # Validate each field to ensure it contains only letters and spaces
    if not re.match("^[a-zA-Z\s]+$", exporter):
        messagebox.showerror("Error", "Exporter name should contain only letters and spaces.")
        return
    if not re.match("^[a-zA-Z\s]+$", consignee):
        messagebox.showerror("Error", "Consignee name should contain only letters and spaces.")
        return
    if not re.match("^[a-zA-Z\s]+$", product):
        messagebox.showerror("Error", "Product name should contain only letters and spaces.")
        return
    if not re.match("^[a-zA-Z\s]+$", port_of_loading):
        messagebox.showerror("Error", "Port of loading should contain only letters and spaces.")
        return
    if not re.match("^[a-zA-Z\s]+$", port_of_discharge):
        messagebox.showerror("Error", "Port of discharge should contain only letters and spaces.")
        return
    if not re.match("^[a-zA-Z\s]+$", vessel):
        messagebox.showerror("Error", "Vessel name should contain only letters and spaces.")
        return
    if not re.match("^[a-zA-Z\s]+$", status):
        messagebox.showerror("Error", "Status should contain only letters and spaces.")
        return
    
    # Validate numeric fields to ensure they contain only digits and dots
    if not quantity.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Quantity should contain only digits and dots.")
        return
    if not rate.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Rate should contain only digits and dots.")
        return
    if not net_weight.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Net weight should contain only digits and dots.")
        return
    
    data[clearance_id] = {
        "Exporter": exporter,
        "Consignee": consignee,
        "Invoice No": invoice_no,
        "Product": product,
        "Quantity": quantity,
        "Rate": rate,
        "Net Weight": net_weight,
        "Port of Loading": port_of_loading,
        "Port of Discharge": port_of_discharge,
        "Container No": container_no,
        "Vessel": vessel,
        "Status": status
    }
    write_data(data, "clearance_data.txt")
    messagebox.showinfo("Success", "Customs clearance record added successfully.")
    clear_entries()

# Function to display all clearance records
def display_clearance_records():
    records_text.delete(1.0, tk.END)
    for clearance_id, details in data.items():
        records_text.insert(tk.END, f"\nClearance ID: {clearance_id}\n")
        records_text.insert(tk.END, f"Exporter: {details['Exporter']}\n")
        records_text.insert(tk.END, f"Consignee: {details['Consignee']}\n")
        records_text.insert(tk.END, f"Invoice No: {details['Invoice No']}\n")
        records_text.insert(tk.END, f"Product: {details['Product']}\n")
        records_text.insert(tk.END, f"Quantity: {details['Quantity']}\n")
        records_text.insert(tk.END, f"Rate: {details['Rate']}\n")
        records_text.insert(tk.END, f"Net Weight: {details['Net Weight']}\n")
        records_text.insert(tk.END, f"Port of Loading: {details['Port of Loading']}\n")
        records_text.insert(tk.END, f"Port of Discharge: {details['Port of Discharge']}\n")
        records_text.insert(tk.END, f"Container No: {details['Container No']}\n")
        records_text.insert(tk.END, f"Vessel: {details['Vessel']}\n")
        records_text.insert(tk.END, f"Status: {details['Status']}\n")
        records_text.insert(tk.END, "----------------------------------------------\n")
# Function to print clearance data as PDF
def print_clearance_data_as_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for clearance_id, details in data.items():
        pdf.cell(200, 10, txt=f"Clearance ID: {clearance_id}", ln=True)
        for key, value in details.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
        pdf.cell(200, 10, txt="----------------------------------------------", ln=True)
    pdf.output("All_clearance_data.pdf")
    messagebox.showinfo("Success", "PDF Generated successfully.")

# Function to update status of a clearance record
def update_clearance_status():
    clearance_id = update_clearance_id_entry.get()
    new_status = new_status_entry.get()

    # Check if the new status is empty
    if not new_status:
        messagebox.showerror("Error", "New status cannot be empty.")
        return

    if clearance_id not in data:
        messagebox.showerror("Error", "Clearance ID not found.")
        return

    data[clearance_id]["Status"] = new_status
    write_data(data, "clearance_data.txt")
    messagebox.showinfo("Success", "Status updated successfully.")
    new_status_entry.delete(0, tk.END)
    update_clearance_id_entry.delete(0, tk.END)

# Function to clear entry fields
def clear_entries():
    clearance_id_entry.delete(0, tk.END)
    exporter_entry.delete(0, tk.END)
    consignee_entry.delete(0, tk.END)
    invoice_no_entry.delete(0, tk.END)
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    net_weight_entry.delete(0, tk.END)
    port_of_loading_entry.delete(0, tk.END)
    port_of_discharge_entry.delete(0, tk.END)
    container_no_entry.delete(0, tk.END)
    vessel_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)

# Function to edit clearance record
def edit_clearance_record():
    global update_clearance_id_entry, new_status_entry
    
    edit_window = tk.Toplevel()
    edit_window.title("Edit Clearance Record")
    
    tk.Label(edit_window, text="Clearance ID:").grid(row=0, column=0, sticky=tk.W)
    update_clearance_id_entry = tk.Entry(edit_window)
    update_clearance_id_entry.grid(row=0, column=1)
    
    tk.Label(edit_window, text="New Status:").grid(row=1, column=0, sticky=tk.W)
    new_status_entry = tk.Entry(edit_window)
    new_status_entry.grid(row=1, column=1)
    
    update_button = tk.Button(edit_window, text="Update Status", command=update_clearance_status)
    update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Main function
def main():
    global data, clearance_id_entry, exporter_entry, consignee_entry, invoice_no_entry, product_entry, quantity_entry, rate_entry, net_weight_entry, port_of_loading_entry, port_of_discharge_entry, container_no_entry, vessel_entry, status_entry, update_clearance_id_entry, new_status_entry, records_text
    
    data = read_data("clearance_data.txt")
    
    root = tk.Tk()
    root.title("Customs Clearance Management System")

    # Create labels and entry fields for adding a new clearance record
    tk.Label(root, text="Clearance ID:").grid(row=0, column=0, sticky=tk.W)
    clearance_id_entry = tk.Entry(root)
    clearance_id_entry.grid(row=0, column=1)
    
    tk.Label(root, text="Exporter:").grid(row=1, column=0, sticky=tk.W)
    exporter_entry = tk.Entry(root)
    exporter_entry.grid(row=1, column=1)
    
    tk.Label(root, text="Consignee:").grid(row=2, column=0, sticky=tk.W)
    consignee_entry = tk.Entry(root)
    consignee_entry.grid(row=2, column=1)
    
    tk.Label(root, text="Invoice No:").grid(row=3, column=0, sticky=tk.W)
    invoice_no_entry = tk.Entry(root)
    invoice_no_entry.grid(row=3, column=1)
    
    tk.Label(root, text="Product:").grid(row=4, column=0, sticky=tk.W)
    product_entry = tk.Entry(root)
    product_entry.grid(row=4, column=1)
    
    tk.Label(root, text="Quantity:").grid(row=5, column=0, sticky=tk.W)
    quantity_entry = tk.Entry(root)
    quantity_entry.grid(row=5, column=1)
    
    tk.Label(root, text="Rate:").grid(row=6, column=0, sticky=tk.W)
    rate_entry = tk.Entry(root)
    rate_entry.grid(row=6, column=1)
    
    tk.Label(root, text="Net Weight:").grid(row=7, column=0, sticky=tk.W)
    net_weight_entry = tk.Entry(root)
    net_weight_entry.grid(row=7, column=1)
    
    tk.Label(root, text="Port of Loading:").grid(row=8, column=0, sticky=tk.W)
    port_of_loading_entry = tk.Entry(root)
    port_of_loading_entry.grid(row=8, column=1)
    
    tk.Label(root, text="Port of Discharge:").grid(row=9, column=0, sticky=tk.W)
    port_of_discharge_entry = tk.Entry(root)
    port_of_discharge_entry.grid(row=9, column=1)
    
    tk.Label(root, text="Container No:").grid(row=10, column=0, sticky=tk.W)
    container_no_entry = tk.Entry(root)
    container_no_entry.grid(row=10, column=1)
    
    tk.Label(root, text="Vessel:").grid(row=11, column=0, sticky=tk.W)
    vessel_entry = tk.Entry(root)
    vessel_entry.grid(row=11, column=1)
    
    tk.Label(root, text="Status:").grid(row=12, column=0, sticky=tk.W)
    status_entry = tk.Entry(root)
    status_entry.grid(row=12, column=1)

    # Buttons to add new record and display all records
    add_record_button = tk.Button(root, text="Add New Clearance Record", command=add_clearance_record)
    add_record_button.grid(row=13, column=0, columnspan=2, pady=10)
    
    display_records_button = tk.Button(root, text="Display All Clearance Records", command=display_clearance_records)
    display_records_button.grid(row=14, column=0, columnspan=2, pady=10)
    
    edit_record_button = tk.Button(root, text="Edit Clearance Record", command=edit_clearance_record)
    edit_record_button.grid(row=15, column=0, columnspan=2)

    # Text box to display clearance records
    records_text = tk.Text(root, width=80, height=20)
    records_text.grid(row=17, column=0, columnspan=2)

    print_pdf_button = tk.Button(root, text="Print Clearance Data as PDF", command=print_clearance_data_as_pdf)
    print_pdf_button.grid(row=16, column=0, columnspan=2, pady=(20, 20))

    root.mainloop()

if __name__ == "__main__":
    main()
