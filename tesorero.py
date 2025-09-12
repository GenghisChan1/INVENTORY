# item class
class Item:
  def __init__(self, item, price, quantity):
    self.item = item
    self.price = price
    self.quantity = quantity

  #deposit item quantity
  def deposit_quantity(self, amount):
    self.quantity += amount
    print(f"Added {amount} to {self.name}")

  #withdraw item quantity
  def withdraw_quantity (self, amount):

    if amount > self.quantity:
      print("Insufficient quantity")
      return

    self.quantity -= amount
    print(f"Removed {amount} from {self.item}")
  
  def total_value(self):
    return self.price * self.quantity

#Inventory class
class Inventory:
  def __init__(self):
    self.items = []

  #add set of items
  def add_item(self):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    item = Item(name, price, quantity)
    self.items.append(item)
    print(f"Item {item.item} added to inventory.")
  
  #remove set of items
  def remove_item(self):

    #check if inventory is empty
    if len(self.items) == 0:
      print("Inventory is empty.")
      return
    
    #display inventory for the user to choose from
    print("<---------Inventory---------->")
    for i in range(len(self.items)):
      print(f"{i+1}. {self.items[i].item} - Price: {self.items[i].price} - Quantity: {self.items[i].quantity}")
    self.total_inventory_value()
    print("<---------------------------->")

    choice = int(input("Enter item number to remove on inventory: "))

    #check if choice is valid
    if choice < 1 or choice > len(self.items):
      print("Invalid choice.")
      return
    
    #remove specific item from inventory
    del self.items[choice - 1]
    print("Item removed from inventory.")

    if len(self.items) == 0:
      print("Inventory is empty.")
      return

    print("<---------Inventory---------->")
    for i in range(len(self.items)):
      print(f"{i+1}. {self.items[i].item} - Price: {self.items[i].price} - Quantity: {self.items[i].quantity}")
    print("<---------------------------->")

  #view inventory
  def view_inventory(self):

    #check if inventory is empty
    if len(self.items) == 0:
      print("Inventory is empty.")
      return
    
    #display inventory
    print("<---------Inventory---------->")
    for i in range(len(self.items)):
      print(f"{i+1}. {self.items[i].item} - Price: {self.items[i].price} - Quantity: {self.items[i].quantity}")
    self.total_inventory_value()
    print("<---------------------------->")

  #total inventory value
  def total_inventory_value(self):
    #
    if len(self.items) == 0:
      print("Total inventory value: PHP 0")
      return
    
    total_value = 0
    for item in self.items:
      total_value += item.total_value()
    print(f"Total inventory value: PHP {total_value}")

inventory = Inventory()
while True:
  print("1. Add item")
  print("2. Remove item")
  print("3. View inventory")
  print("4. Total inventory value")
  print("5. Edit item quantity")
  print("0. Exit")

  ch = int(input("Enter your choice: "))

  #Each choices corresponds to different function from Inventory class
  if ch == 1:
    inventory.add_item()
  elif ch == 2:
    inventory.remove_item()
  elif ch == 3:
    inventory.view_inventory()
  elif ch == 4:
    inventory.total_inventory_value()
  elif ch == 5:
    if len(inventory.items) == 0:
      print("Inventory is empty.")
      continue

    inventory.view_inventory()

    print("1. Deposit item quantity")
    print("2. Withdraw item quantity")
    print("0. Back")
    ch1 = int(input("Enter your choice: "))

    if ch1 < 1 or ch1 > 2:
      print("Invalid choice.")
      continue

    if ch1 == 1:
      item = int(input("Enter item number to deposit quantity: "))
      if item < 1 or item > len(inventory.items):
        print("Invalid choice.")
        continue
      amount = int(input("Enter amount to deposit: "))
      #access specific item and call deposit_quantity method
      inventory.items[item - 1].deposit_quantity(amount)

    elif ch1 == 2:
      item = int(input("Enter item number to withdraw quantity: "))
      if item < 1 or item > len(inventory.items):
        print("Invalid choice.")
        continue
      amount = int(input("Enter amount to withdraw: "))
      #access specific item and call withdraw_quantity method
      inventory.items[item - 1].withdraw_quantity(amount)

    elif ch == 0:
      break

  elif ch == 0:
    break

  else:
    print("Invalid choice.")
    continue


