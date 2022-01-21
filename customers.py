
import json

customers_data = "customers.json"

def customers_menu():
    while True:
        user_input = input("Enter 1 to load customer data\n"
                           "Enter 2 to insert a new customer\n"
                           "Enter 3 to delete a customer\n"
                           "Enter 4 to update a customer\n"
                           "Enter 5 to list all customers\n"
                           "Enter 6 to list a customer's details\n"
                           "Enter 'exit' to quit\n")

        if int(user_input) == 1:
            load_customer()
        elif int(user_input) == 2:
            create_customer()
        elif int(user_input) == 3:
            delete_customer()
        elif int(user_input) == 4:
            update_customer()
        elif int(user_input) == 5:
            list_customers()
        elif user_input.lower() == "exit":
            break


def load_customer(filename = customers_data):

    while True:
        user_input = input('Enter id of customer to view or "exit" to go back to main menu \n')

        if user_input.lower() == "exit":
            break
        else:
            with open(filename,'r+') as file:
                file_data = json.load(file)
                for i in range(len(file_data["customers"])):
                    if file_data["customers"][i]["id"] == user_input:
                        print( file_data["customers"][i])
                        break
                else:
                     print("No customer with the given id found")
        
                        
                                                
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

def list_customers(filename = customers_data):

    with open(filename,'r+') as file:
        file_data = json.load(file)
        for i in file_data['customers']:
            print(i)







    







