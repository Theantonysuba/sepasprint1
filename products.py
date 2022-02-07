import json

products_data = "products.txt"

class Product:
    def __init__(self,id,name,price,quantity):

        #run validations
        assert price >= 0, f"Price {price} must be greater than 0"
        assert quantity >= 0, f"Amount {quantity} must be greater than 0"

        #assign to self object
        self.id = id
        self.name = name 
        self.price = float(price)
        self.quantity = int(quantity)

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

        id = input('Enter product id \n')
        file_data = json.load(file)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                print("Product Id already exists, please enter another ID")
                create_product(filename = products_data)
                break
        else:
            name = input('Enter product name \n')
            quantity = int(input('Enter product quantity \n'))
            price = float(input('Enter product price \n'))

            product = Product(id,name,price,quantity)
                        
            file_data["products"].append(product.__dict__) 
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

            print("Product successfully added")
    

def delete_product(filename = products_data):
    id = input('Enter id of customer to delete \n')

    with open(filename,'r+') as file:
        file_data = json.load(file)

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                del file_data["products"][i]
                # # Sets file's current position at offset.
                file.seek(0)
                # # convert back to json.
                with open(filename,'w') as file:
                    json.dump(file_data, file, indent = 4)
                    print("Product successfully deleted")
                    break
        else:
            print("Product Id does not exist, enter a valid ID")
            delete_product(filename = products_data)
        
        
        

def update_product(filename = products_data):
    
    with open(filename,'r+') as file:
        file_data = json.load(file)

        id = input('Enter id to update \n' )

        for i in range(len(file_data["products"])):
            if file_data["products"][i]["id"] == id:
                name = input('Enter new name \n')
                quantity = int(input('Enter new quantity \n'))
                price = float(input('Enter new price \n'))

                product = Product(id,name,price,quantity)

                file_data["products"].append(product.__dict__) 

                    # # Sets file's current position at offset.
                file.seek(0)
                 # # convert back to json.
                with open(filename,'w') as file:
                    json.dump(file_data, file, indent = 4)
                    print("Product successfully updated")
                    break
                
        else:
            print("Product Id does not exist, please enter a valid ID")
            update_product(filename=products_data)
            
                
        

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


