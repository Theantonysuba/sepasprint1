import json

products_data = "products.json"

class Product:
    def __init__(self,id,name,price,amount):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self,price):
        self.price = price

    def get_amount(self):
        return self.amount

    def set_amount(self,amount):
        self.amount = amount

def products_menu():
    while True:
        user_input = input("Enter 1 to load product data\n"
                           "Enter 2 to insert a new product\n"
                           "Enter 3 to delete a product\n"
                           "Enter 4 to update a product\n"
                           "Enter 5 to list all products\n"
                           "Enter 6 to list a product's details\n"
                           "Enter 0 to quit\n")

        if int(user_input) == 1:
            load_product()
        elif int(user_input) == 2:
            create_product()
        elif int(user_input) == 3:
            delete_product()
        elif int(user_input) == 4:
            update_product()
        elif int(user_input) == 5:
            list_products()
        elif int(user_input) == 0:
            break

def load_product(filename = products_data):

    while True:
        user_input = input('Enter id of product to view or "exit" to go back to main menu \n')

        if user_input.lower() == "exit":
            break
        else:
            with open(filename,'r+') as file:
                file_data = json.load(file)
                for i in range(len(file_data["products"])):
                    if file_data["products"][i]["id"] == user_input:
                        print( file_data["products"][i])
                        break
                else:
                     print("No product with the given id found")
                        
                    

def create_product(filename = products_data):

    with open(filename,'r+') as file:

        id = input('Enter product id ')
        file_data = json.load(file)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                print("Product Id already exists")
                break
        else:
            name = input('Enter product name ')
            amount = input('Enter product amount ')
            price = input('Enter product price ')

            product = Product(id,name,amount,price)
                        
            file_data["products"].append(product.__dict__) 
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
    

def delete_product(filename = products_data):
    id = input('Enter id of customer to delete')

    with open(filename,'r+') as file:
        file_data = json.load(file)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                del file_data["products"][i]
                break
        
        # # Sets file's current position at offset.
        file.seek(0)
        # # convert back to json.
        with open(filename,'w') as file:
            json.dump(file_data, file, indent = 4)

def update_product(filename = products_data):
    id = input('Enter id to update')
    name = input('Enter new name ')
    amount = input('Enter new amount ')
    price = input('Enter new price ')

    with open(filename,'r+') as file:
        file_data = json.load(file)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                file_data["products"][i]["name"] = name
                file_data["products"][i]["amount"] = amount
                file_data["products"][i]["price"] = price
               
        
        # # Sets file's current position at offset.
        file.seek(0)
        # # convert back to json.
        with open(filename,'w') as file:
            json.dump(file_data, file, indent = 4)

def list_products(filename = products_data):

    with open(filename,'r+') as file:
        file_data = json.load(file)
        for i in file_data['products']:
            print(i)
