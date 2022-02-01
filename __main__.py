
import customers
import products
import purchases


def main():
    
    while True:
        user_input = input( "Enter 1 for customers\n"
                            "Enter 2 for products\n"
                            "Enter 3 for purchases\n"
                            "Enter 0 to quit\n")
        
        if int(user_input) == 1:
            customers.customers_menu()
        elif int(user_input) == 2:
            products.products_menu()
        elif int(user_input) == 3:
            purchases.purchases_menu()
        elif user_input.lower() == "exit":
            break
        

if __name__ == "__main__":
    main()
