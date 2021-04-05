'''Logistics program and invoicing program'''
#Make database
#Make structure
#Add products
#Track the products
#Make invoice layout
#Synchronize invoice numbering
import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
        )
    except Error as err:
        print(f"Error: ' {err}'")
    return connection

pw = 'cdcaf56efWSm2!'
#connection = create_server_connection("localhost", "robin", pw)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

#create_database_query="CREATE DATABASE test_python ;"

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MYSQL Database connection successful")
    except Error as err:
        print(f"Error : '{err}'")
    return connection


create_customer_table = """
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  COMPANY VARCHAR(40) NOT NULL,
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
  """
connection = create_db_connection("localhost", "robin", pw, "test_python")
execute_query(connection, create_customer_table)

