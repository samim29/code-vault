"""5.Write a code for Restaurant Management System Using OOPS:
Create a MenuItem class that has attributes such as name, description, price, and category.
Implement methods to add a new menu item, update menu item information, and remove a menu item from the menu.
Use encapsulation to hide the menu item's unique identification number.
Inherit from the MenuItem class to create a FoodItem class and a BeverageItem class, each with their own specific attributes and methods.
"""

class MenuItem:
    next_id=1
    def __init__(self,name,description,price,category):
        self._id=MenuItem.next_id
        self._name=name
        self._description=description
        self._price=price
        self._category=category
        MenuItem.next_id+=1
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    def set_name(self, new_name):
        self._name = new_name

    def set_description(self, new_description):
        self._description = new_description

    def set_price(self, new_price):
        self._price = new_price

    def set_category(self, new_category):
        self._category = new_category

class FoodItem(MenuItem):
    def __init__(self,name,description,price,category,calories):
        super().__init__(name,description,price,category)
        self._calories=calories
    def get_calories(self):
        return self._calories
    def set_calories(self,new_calories):
        self._calories=new_calories

class BeverageItem(MenuItem):
    def __init__(self, name, description, price, category,volume):
        super().__init__(name, description, price, category)
        self._volume=volume

    def get_volume(self):
        return self._volume

    def set_volume(self, new_volume):
        self._volume = new_volume



# Create menu items
food_item = FoodItem("Veg Burger", "Delicious vegetable patty with buns", 10.99, "Main Course", 500)
beverage_item = BeverageItem("Coke", "Refreshing carbonated drink", 2.99, "Beverage", 355)

# Print menu item information
print(f"Food Item ID: {food_item.get_id()}")
print(f"Food Item Name: {food_item.get_name()}")
print(f"Food Item Description: {food_item.get_description()}")
print(f"Food Item Price: ${food_item.get_price()}")
print(f"Food Item Category: {food_item.get_category()}")
print(f"Food Item Calories: {food_item.get_calories()} calories")

print("\n")

print(f"Beverage Item ID: {beverage_item.get_id()}")
print(f"Beverage Item Name: {beverage_item.get_name()}")
print(f"Beverage Item Description: {beverage_item.get_description()}")
print(f"Beverage Item Price: ${beverage_item.get_price()}")
print(f"Beverage Item Category: {beverage_item.get_category()}")
print(f"Beverage Item Volume: {beverage_item.get_volume()} ml")



        
    