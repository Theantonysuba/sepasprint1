
import json

customers_data = "customers.json"

def load_customers(filename = customers_data):

    with open(filename,'r+') as file:
        file_data = json.load(file)
        for i in file_data['customers']:
            print(i)

def create_customer(filename = customers_data):
    id = input('Enter your id ')
    name = input('Enter your name ')
    address = input('Enter your address ')

    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["customers"].append({
        "id": id,
        "name": name,
        "address": address}) 
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def delete_customer(filename = customers_data):
    id = input('Enter id of customer to delete')

    with open(filename,'r+') as file:
        file_data = json.load(file)

        for i in range(len(file_data["customers"])):
            if file_data["customers"][i]["id"] == id:
                del file_data["customers"][i]
                break
        
        # # Sets file's current position at offset.
        file.seek(0)
        # # convert back to json.
        with open(filename,'w') as file:
            json.dump(file_data, file, indent = 4)

def update_customer(filename = customers_data):
    id = input('Enter id to update')
    name = input('Enter new name ')
    address = input('Enter new address ')

    with open(filename,'r+') as file:
        file_data = json.load(file)

        for i in range(len(file_data["customers"])):
            if file_data["customers"][i]["id"] == id:
                file_data["customers"][i]["name"] = name
                file_data["customers"][i]["address"] = address
               
        
        # # Sets file's current position at offset.
        file.seek(0)
        # # convert back to json.
        with open(filename,'w') as file:
            json.dump(file_data, file, indent = 4)



    







