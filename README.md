# Customer and products management software
I was working in a supplychain company and they were looking for a simple software to keep track of products, customers and invoices. I decided this was something I could build, modify and scale at the will of the company.

Below I have written the components that are a part of this software.

## Invoice.py
Holds the general layout for the pdf

Takes as input the Table for products and customer details

## working_data.py
Retrieves the data from the sqlite database with the help of sqlalchemy

Outputs the products the user specifys as a table

## main.py
Takes the users input to retrieve, print or modify information from invoice.py and/or working_data.py

