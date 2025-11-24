#   🛒 Retail Store Inventory & Billing System 


This is an easy-to-use Python console app to manage store inventory, create bills for customers, and maintain a sales history.





# 📌  Features


✅  Add Items to Inventory


Add a new product name


Set the price of the product


Update stock quantity


Stores all of this in a Python dictionary



✅  View Inventory


Displays all inventory items with:


Name


Price


Remaining Stock



✅  Create Customer Bill


Add multiple items to customer bill


Automatically checks if the items/stocks are available


Updates inventory stocks and removes the quantity that has been sold


Generates an itemized bill that shows the costs


Saves each bill in sales history



✅  Sales Report


This functionality shows:


The total number of bills generated


The total amount of bills generated (the total funds generated)



✅  Interactive Menu


This Python console application has a simple menu-driven interface:


1. Add Item




2. View Inventory




3. Create Bill




4. View Bill Sale Reports




5. Exit



《



# 🗂  File Contents


Main Code Structure



items() → Add Inventory Items


view() → View Inventory


bill() → Create Bill and update stock


sales_report() → View all sales history


menu() → Main menu function



《



# ▶  How to Run


1. Save the Python code in a file below:


store.py


2. Then in terminal:


python store.py


3. Then in the menu, use the system functions.



《



《


# 🧩  Data Structures Used


Inventory


inventory = {
    "Soap": {"price": 30, "stock": 47},
    "Shampoo": {"price": 120, "stock": 20}
}


Sales history


sales = [
    {"items": [("Soap", 3, 30, 90)], "total": 90}
]


《


# 👨‍💻 AVNI GUPTA


Retail Store Billing System - Python Console App


《
