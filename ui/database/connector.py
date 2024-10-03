import mysql.connector

mydb = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

mycursor = mydb.cursor()


# Call the stored procedure
mycursor.callproc("your_stored_procedure_name", (arg1, arg2))

# Fetch the results
results = mycursor.fetchall()

print(results)

mydb.close()