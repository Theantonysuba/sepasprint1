
import customers


def main():
    
    while True:
        user_input = input("Enter 1 to load customer data\n"
                        "Enter 2 to insert a new customer\n"
                            "Enter 3 to delete a customer\n"
                                "Enter 4 to update a customer\n"
                                    "Enter 5 to load product data\n"
                                        "Enter 6 to insert a new product\n"
                                            "Enter 7 to delete a product\n"
                                                "Enter 8 to update product data\n"
                                                    "Enter 9 to purchase\n"
                                                        "Enter 10 to search for a product\n"
                                                            "Enter 11 to list all customers\n"
                                                                "Enter 12 to list all products\n"
                                                                    "Enter 13 to list a customer's details\n"
                                                                        "Enter 14 to quit\n")
        
        if int(user_input) == 1:
            print("These are the customers data")
        elif int(user_input) == 2:
            customers.create_customer()
        elif int(user_input) == 14:
            break
        else:
            print("Enter a valid choice")

if __name__ == "__main__":
    main()
