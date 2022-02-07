
import customers
import products

import json
import pprint

customers_data = "customers.txt"
products_data = "products.txt"
purchases_data = "purchases.txt"

def purchases_menu():
    while True:
        user_input = input(
                           "Enter 1 for purchase\n"
                           "Enter 2 to see past purchases\n"
                           "Enter 3 to search for a purchases\n"
                           "Enter 0 to quit\n")

        if int(user_input) == 1:
            check_out()
        elif int(user_input) == 2:
            list_purchases()
        elif int(user_input) == 3:
            search_menu()
        elif int(user_input) == 0:
            break        

class Purchases:
    def __init__(self,customer_id,customer_name,product_name,product_price,product_quantity,total_price):

        
        #assign to self object
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.product_name = product_name 
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.total_price = total_price

def customer_check(filename = customers_data):

    with open(filename,'r+') as file:

        id = input('Enter user id ')
        file_data = json.load(file)

        for i in range(len(file_data["customers"])):
            if file_data["customers"][i]["id"] == id:
                print("Customer found:", file_data["customers"][i]['name'] )
                return(file_data["customers"][i])
        else:
            print("No user with the given Id exists")
            new_id = input("Enter 1 to enter a new ID\n"
                                "Enter 2 to create a new customer\n")
            if new_id == "1":
                return customer_check(filename = customers_data)
            elif new_id == "2":
                customers.create_customer(filename = customers_data)
                return customer_check(filename = customers_data)
                

def product_check(filename = products_data):

    with open(filename,'r+') as file:

        id = input('Enter product id ')
        file_data = json.load(file)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                print("Product details:")
                print("Product name:",file_data["products"][i]["name"])
                print("Price:", file_data["products"][i]["price"])
                print("Amount in stock:", file_data["products"][i]["quantity"])
                return file_data["products"][i]
        else:
            print("No product with the given Id exists")
            new_id = input("Enter 1 to enter a new ID\n"
                            "Enter 2 to create a new product\n")
            if new_id == "1":
                return product_check(filename = products_data)
            elif new_id == "2":
                products.create_product(filename = products_data)
                return product_check(filename = products_data)


def purchase_validator(quantity):
    purchase_quantity = int(input("Enter the quantity to purchase"))
    if purchase_quantity < 0:
        print("Please enter a positive integer")
        purchase_validator(quantity)
    elif purchase_quantity > quantity:
        print("Sorry, not enough items in stock")
        purchase_validator(quantity)
    else:
        return(purchase_quantity)

def check_out():
    customer = customer_check()
    customer_name = customer["name"]

    total_price = []
    cart_list = []

    while True:
        product = product_check()
    
        customer_id = customer["id"]
        
        
        product_id = product["id"]
        product_name = product["name"]
        product_price = product["price"]
        product_quantity = product["quantity"]
        
        purchase_quantity = int(purchase_validator(product_quantity))
        item_price = purchase_quantity * product_price 
        
        print(f"""
                Order details: 
                Product name: {product_name}
                Product price: {product_price}
                Product quantity: {purchase_quantity}
                Your item price: {item_price}
            
        """)

        total_price.append(item_price)
        cart = {'Product name': product_name, 'Product price': product_price, 'Product quantity': purchase_quantity, 'Item Price': item_price }
        cart_list.append(cart)


        #####update customer records

        with open(products_data,'r+') as file:
            file_data = json.load(file)
            for i in range(len(file_data["products"])):
                if file_data["products"][i]["id"] == product_id:
                    file_data["products"][i]["quantity"] = product_quantity - purchase_quantity

            # # Sets file's current position at offset.
            file.seek(0)
            # # convert back to json.
            with open( products_data,'w') as file:
                json.dump(file_data, file, indent = 4)
            # return(file_data["products"][i])

        ##### update purchase records
        with open(purchases_data,'r+') as file:
            file_data = json.load(file)

            product = Purchases(customer_id,customer_name,product_name, product_price,purchase_quantity,item_price)
                            
            file_data["purchases"].append(product.__dict__) 
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
        
        
        new_item = input("Press 1 to enter another item, 2 to check out or 0 to quit\n" )

        if int(new_item) == 2:
            final_amount = sum(total_price)
            print("Receipt: \n")
            pprint.pprint(cart_list)
            print(f"The total price of your item is:", {final_amount})
            break
        elif int(new_item) == 0:
            break
            
    
def list_purchases(filename = purchases_data):

    with open(filename,'r+') as file:
        file_data = json.load(file)
        for i in file_data['purchases']:
            print(i)

def search_menu():

    while True:
        user_input = input(
                           "Enter 1 to search by user name\n"
                           "Enter 2 to search by product name \n"
                           "Enter 0 to quit\n")

        if int(user_input) == 1:
            search_by_user()
        elif int(user_input) == 2:
            search_by_product()
        elif int(user_input) == 0:
            break       

def search_by_user(filename = purchases_data):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        search = input("Enter search item \n")
        for i in range(len(file_data["purchases"])):
            if file_data["purchases"][i]["customer_name"][:len(search)].lower() == search.lower():
                print(file_data["purchases"][i])

def search_by_product(filename=purchases_data):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        search = input("Enter search item \n")
        for i in range(len(file_data["purchases"])):
            if file_data["purchases"][i]["product_name"][:len(search)].lower() == search.lower():
                print(file_data["purchases"][i])










    