# Customer and product management software
A program to keep track of your customers, products and print invoices in pdf format.
## Description
The program stores customers, products, invoices in a sqlite3 database and can print PDF invoices. 
## Prerequisites 
python 3.8 or newer. Link for [python](https://www.python.org/downloads/)
## Installation
    git clone https://github.com/Robinborg/invoice_program
    cd invoice_program
    python3 -m pip install -r requirements.txt
    
## About
The program uses Reportlab to sketch the layout for the pdf. 

Version used in program: 3.6.2

Link for [reportlab](https://www.reportlab.com)

The program uses sqlalchemy to create the object-relational mappings("ORMs"), schemas and connection to the database. 

Version used in program: 1.4.27

Link for [sqlalchemy](https://www.sqlalchemy.org)

## Overview of the program folder:
```
├── img -> contains images for the README.md
├── src -> main project directory, contains main.py
│   ├── cli -> command line interface
│   ├── handlers -> sqlalchemy handlers
│   │
│   ├── interface -> menus and eventloops for navigating the program 
│   │ 
│   ├── models -> __init__ contains the engine and setup for sqlalchemy, schemas are in the folder 
│   │ 
│   └── utils -> various helper functions for the program 
│   
│
└── tests -> Unittesting for interface and models/handlers
```
## Use
The program uses an event loop to navigate the server and for creating the invoices.

By running:

    python main.py 
The program will start the prompts in your terminal.

<img src= "https://github.com/Robinborg/invoice_program/blob/main/img/Screenshot%202022-01-06%20at%2014.59.17.png?raw=true" width="300" height="200"/>

## Example PDF invoice

<img src= "https://github.com/Robinborg/images/blob/main/Screenshot%202021-11-12%20at%2017.42.41.png?raw=true" width="300" height="500"/>

