
import json

customers_data = "customers.txt"

class Customer:
    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address

def customers_menu():
    while True:
        user_input = input(
                           "Enter 1 to insert a new customer\n"
                           "Enter 2 to delete a customer\n"
                           "Enter 3 to update a customer\n"
                           "Enter 4 to list all customers\n"
                           "Enter 5 to search for customer\n"
                           "Enter 0 to quit\n")

        if int(user_input) == 1:
            create_customer()
        elif int(user_input) == 2:
            delete_customer()
        elif int(user_input) == 3:
            update_customer()
        elif int(user_input) == 4:
            list_customers()
        elif int(user_input) == 5:
            search_customer()
        elif int(user_input) == 0:
            break
                      
                                                
def create_customer(filename = customers_data):
    

    with open(filename,'r+') as file:

        id = input('Enter user id ')
        file_data = json.load(file)

        for i in range(len(file_data["customers"])):
            if file_data["customers"][i]["id"] == id:
                print("User Id already exists, please enter another ID")
                create_customer(filename = customers_data)
                break
        else:
            name = input('Enter user name \n')

            address = input('Enter user address \n')

            customer = Customer(id,name,address)
                        
            file_data["customers"].append(customer.__dict__) 
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

            print("User successfully added")

def delete_customer(filename = customers_data):
    

    with open(filename,'r+') as file:

        id = input('Enter id of customer to delete \n' )
        file_data = json.load(file)

        for i in range(len(file_data["customers"])):
            if file_data["customers"][i]["id"] == id:
                del file_data["customers"][i]

                # # Sets file's current position at offset.
                file.seek(0)
                # # convert back to json.
                with open(filename,'w') as file:
                    json.dump(file_data, file, indent = 4)
                    print("User successfully deleted")
                    break
        else:
            print("User Id does not exist, enter a valid ID")
            delete_customer(filename = customers_data)

        

        
        
        

def update_customer(filename = customers_data):
    

    with open(filename,'r+') as file:
        file_data = json.load(file)

        id = input('Enter id to update \n')

        for i in range(len(file_data["customers"])):
            
            if file_data["customers"][i]["id"] == id:
                name = input('Enter new name \n ')
                address = input('Enter new address \n')

                file_data["customers"][i]["name"] = name
                file_data["customers"][i]["address"] = address


                # # Sets file's current position at offset.
                file.seek(0)
                # # convert back to json.
                with open(filename,'w') as file:
                    json.dump(file_data, file, indent = 4)
                    print("User successfully updated")
                    break
                
                
        else:
            print("User Id does not exist, please enter a valid ID")
            update_customer(filename = customers_data)
               
        
        

def list_customers(filename = customers_data):

    with open(filename,'r+') as file:
        file_data = json.load(file)
        for i in file_data['customers']:
            print(i)

def search_customer(filename = customers_data):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        search = input("Enter search item \n")
        for i in range(len(file_data["customers"])):
            if file_data["customers"][i]["name"][:len(search)].lower() == search.lower():
                print(file_data["customers"][i])



   






    







