#!/usr/bin/python3
"""
MySQLServer.py - Creates the alx_book_store database in MySQL server
"""
import mysql.connector
from mysql.connector import Error


def create_database():
    """Creates the alx_book_store database if it doesn't exist"""
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Update with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            cursor.close()
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close the database connection
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
