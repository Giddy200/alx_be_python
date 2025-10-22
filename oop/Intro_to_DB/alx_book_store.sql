import mysql.connector
try:
# Connect to MySQL server
mydb = mysql.connector.connect(host="localhost",user="root",password="swankonit375$")
# Create cursor
mycursor = mydb.cursor()

# Create database if not exists
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
   # Close connection
       if 'mycursor' in locals():
            mycursor.close()
        mydb.close()  
        if 'mydb' in locals(): and mydb.is_connected():
            mydb.close()          