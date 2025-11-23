inventory={}
sales = []
# Function to add new items to inventory
def items():
    name=input("Enter item name: ")
    price=int(input("Enter item price: "))
    stock=int(input("Enter stock added: "))
# Add item to inventory
    inventory[name]={"price":price,"stock":stock}
    print("Item added successfully!\n")

# Function to view inventory   
def view():
    if not inventory:
        print("No items in inventory.\n")
        return
    print("\n----- INVENTORY (Remaining Stocks) -----")
    for name,details in inventory.items():
        print(f"Item: {name} | Price: ₹{details['price']} | Stock Left: {details['stock']}")
    print()

# Function to generate bill
def bill():
    bill_items=[]
    total=0
    print("\nEnter items to bill. [Type 'done' when finished].")

    while True:
        item=input("Item name (or 'done'): ")
        if item.lower()=="done":
            break
        if item not in inventory:
            print("Item not found in inventory. Try again.")
            continue
        # get quantity 
        quantity=int(input("Quantity: "))

        if quantity>inventory[item]["stock"]:
            print("Enough stock not available. Try again.")
            continue
        price=inventory[item]["price"]
        cost=price*quantity
        total+=cost
        inventory[item]["stock"]-=quantity
        bill_items.append((item,quantity,price,cost))
        print("\n******BILL******")
        for item,quantity,price,cost in bill_items:
            
            print(f"ITEM: {item} x {quantity} = ₹{cost}\n")
        print("\nTotal Amount: ₹",total)

        #Remaining stock
        print("\n----- REMAINING STOCKS -----")
        for name,details in inventory.items():
            print(f"Item: {name} >>>> Stock Left: {details['stock']}")
        print()

# Saving bill
    sales.append({"items":bill_items,"total":total})

# Sale record
def sales_report():
    if not sales:
        print("No sales yet.\n")
        return

    print("\n----- SALES REPORT -----")
    
    grand_total=0
    for i, bill in enumerate(sales, start=1):
        print(f"\nBill #{i}: ₹{bill['total']}")
        grand_total+= bill['total']
        
    print("------------------------")
    print("Total Sales: ₹", grand_total)
    print() 

    # Main list
def menu():
  global sales
  sales=[]
  while True:
        print("====****** RETAIL STORE SYSTEM *****====")
        print(f"1. Add Item to the Store (Nessecary step) ")
        print("2. View Store (Current Stock)")
        print("3. Create the Bill")
        print("4. View Sales Record")
        print("5. Exit")
# choice according to the buisness person
        choice = input("Enter choice number from above list: ")

        if choice == "1":
            items()
        elif choice == "2":
            view()
        elif choice == "3":
            bill()
        elif choice == "4":
            sales_report()
        elif choice == "5":
            print("***System closed...See you again!***")
            break
        else:
            print("Choice is not from the given list! Try again.\n")


#RUN 
menu()



