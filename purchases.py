
import customers
import products

import json

customers_data = "customers.json"
products_data = "products.json"
purchases_data = "purchases.json"

def purchases_menu():
    while True:
        user_input = input(
                           "Enter 1 to check out a customer\n"
                           "Enter 2 to see purchase history\n"
                           "Enter 0 to quit\n")

        if int(user_input) == 1:
            check_out()
        elif int(user_input) == 2:
            list_purchases()
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
    product = product_check()
  
    customer_id = customer["id"]
    customer_name = customer["name"]
    
    product_id = product["id"]
    product_name = product["name"]
    product_price = product["price"]
    product_quantity = int(product["quantity"])
    
    purchase_quantity = int(purchase_validator(product_quantity))
    total_price = purchase_quantity * product_price 
    print(f"""
            Order details: 
            Product name: {product_name}
            Product price: {product_price}
            Product quantity: {purchase_quantity}
            Your total price: {total_price}
        
    """)

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

        product = Purchases(customer_id,customer_name,product_name, product_price,purchase_quantity,total_price)
                        
        file_data["purchases"].append(product.__dict__) 
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
           
    
def list_purchases(filename = purchases_data):

    with open(filename,'r+') as file:
        file_data = json.load(file)
        for i in file_data['purchases']:
            print(i)

check_out()







    