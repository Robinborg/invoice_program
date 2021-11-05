# Customer and product management software
The supply chain company I was working for needed a software to handle products and customers. I saw my opportunity and built the program myself.


## Invoice.py
The invoice module contains the layout for the PDF and asks as input a product table and customer details. 
It saves PDFs in the working directory.

## working_data.py
The working data module contains the connection to the database and retrieves the information that the user specifies.
The program outputs product table and customer details.

## main.py
The main module combines the invoice module and working data module. The user can easily input commands to get information from working data module and save it to the invoice module, which prints the invoice as a PDF into the working directory.
