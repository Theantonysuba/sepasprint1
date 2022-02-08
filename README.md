# CUSTOMER PRODUCT SYSTEM
## Command Line Driven Point of Sale Terminal
### Introduction
The customer product system is based on customers, products and purchases made by customers. The program starts with a menu, gets customers' choices and processes them. The program helps in managing customer and product data in the system. It enables customers to buy certain products in case there are enough items from that product in the system. 

Customer and product data is entered interactively by the user through a keyboard. For customers: id, name and address is entered. Customer IDs are unique and cannot be repeated. For products: id, name, amount and quantity is entered. Product Ids are unique too and can also not be repeated. 

For a purchase, customer_id, product_id and amount of product will be needed. If the amount is larger than the amount available in the system the product will not be sold. If the system has enough from the given product, the purchase will be completed by decreasing the amount in the system. 

## Languages and tools
* Editor
* Python

## Clone Project
git clone https://github.com/Theantonysuba/sepasprint1.git

## Run
python3 __main__.py

## Concepts
+ Python Programming Fundamentals
+ Object Oriented Programming
+ Core python data structures
+ Algorithms
+ Git Fundamentals

## Project Functionalities
The __main__.py file consists of the main menu where the user chooses the operations they want to perform. These are:
- Customer Operations
- Product Operations
- Purchase Operations

## 1. CUSTOMER OPERATIONS
The customer.py file describes customer operations which are:
* Customer submenu which allows users to select an operation to handle
* Insert customer which allows users to create new customers and save in the customers.txt file
* Delete customer that allows users to remove customer details from the customers.txt file
* Update customer that allows users to edit customer details from the customers.txt file
* List customers that allows users to see details of all existing customers.
* Search customers that allows users to search for particular customer(s) from customers.txt file

## 2. PRODUCT OPERATIONS
The product.py file describes product operations which are:
* Product submenu which allows users to select an operation to handle
* Insert product which allows users to create new products and save in the products.txt file
* Delete product that allows users to remove product details from the product.txt file
* Update product that allows users to edit product details from the product.txt file
* List products that allows users to see details of all existing products.
* Search products that allows users to search for particular product(s) from products.txt file

## 3. PURCHASE OPERATIONS
The purchase.py file describes product operations which are:
* Purchases submenu which allows users to select an operation to handle.
* Make purchase operation which prompts the user to enter customer id and product id in order to make a purchase. The purchase details are stored in the purchase.txt file.
* Search purchase which allows users to search for purchases made using customer name or product name.
* List purchases which lists all purchases made.








