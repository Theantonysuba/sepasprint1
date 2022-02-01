import json

products_data = "products.json"

class Product:
    def __init__(self,id:str,name:str,price:float,quantity:int):

        #run validations
        assert price >= 0, f"Price {price} must be greater than 0"
        assert quantity >= 0, f"Amount {quantity} must be greater than 0"

        #assign to self object
        self.id = id
        self.name = name 
        self.price = price
        self.quantity = quantity

def products_menu():
    while True:
        user_input = input(
                           "Enter 1 to insert a new product\n"
                           "Enter 2 to delete a product\n"
                           "Enter 3 to update a product\n"
                           "Enter 4 to search for a product\n"
                           "Enter 5 to list all products\n"
                           "Enter 0 to quit\n")

        if int(user_input) == 1:
            create_product()
        elif int(user_input) == 2:
            delete_product()
        elif int(user_input) == 3:
            update_product()
        elif int(user_input) == 4:
            search_product()
        elif int(user_input) == 5:
            list_products()
        elif int(user_input) == 0:
            break                 

def create_product(filename = products_data):

    with open(filename,'r+') as file:

        id = input('Enter product id ')
        file_data = json.load(file)
        print(file_data)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                print("Product Id already exists")
                break
        else:
            name = input('Enter product name ')
            quantity = int(input('Enter product quantity '))
            price = float(input('Enter product price '))

            product = Product(id,name,price,quantity)
                        
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
    quantity = int(input('Enter new quantity '))
    price = float(input('Enter new price '))

    with open(filename,'r+') as file:
        file_data = json.load(file)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                file_data["products"][i]["name"] = name
                file_data["products"][i]["quantity"] = quantity
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

def search_product(filename = products_data):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        search = input("Enter search item \n")
        for i in range(len(file_data["products"])):
            if file_data["products"][i]["name"][:len(search)].lower() == search.lower():
                print(file_data["products"][i])



