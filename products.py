import json

products_data = "products.json"

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
    id = input('Enter product id ')
    name = input('Enter product name ')
    amount = input('Enter product amount ')
    price = input('Enter product price ')

    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["products"].append({
        "id": id,
        "name": name,
        "amount": amount,
        "price": price}) 
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

load_product()