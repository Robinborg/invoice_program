# logistics

##Invoice.py
Holds the general layout for the pdf.
Takes as input the Table for products and customer details.

##working_data.py
Retrieves the data from the sqlite database with the help of sqlalchemy.
Outputs the products the user specifys as a table.

##main.py
Takes the users input to retrieve, print or modify information from invoice.py and/or working_data.py.

