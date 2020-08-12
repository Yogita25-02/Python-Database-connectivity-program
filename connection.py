import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='ecommerce',
                                         port='3306',
                                         user='root',
                                         password='root')
    print(connection)

    cursor = connection.cursor();
    #cursor.execute("CREATE DATABASE ecommerce;")
    #print("Database created successfully")

    #cursor.execute("show table;")
    #database_list=cursor.fetchall()
    #print(database_list)

    #cursor.execute("use ecommerce;")
    #cursor.execute("CREATE TABLE ecomm(ecomid int,ecomname varchar(30))")
    #print("Table created successfully")
    #print("---------------------------")
    #cursor.execute("SHOW tables")
    #table_list=cursor.fetchall()

    #for table in table_list:
     #   print(table_list)

    #  query = "INSERT INTO `ecommerce`.`ecom`(`ecomid`,`ecomname`) VALUES (%s,%s)"
    #values = (111, "Flipkart")
    #cursor.execute(query, values)
    #connection.commit()

    #print(cursor.rowcount,"record inserted")


    # values = [
    #    (222,'Amazon'),
    #    (333,'Myntra'),

    #]

    ## executing the query with values - multiple entries
    #cursor.executemany(query, values)
    ## to make final output we have to run the 'commit()' method of the database object
    #connection.commit()

    #print(cursor.rowcount, "record inserted")

    # query = "SELECT * FROM `ecom`.`emplo`;"
    query = "Select ecomname  from ecommerce.ecom ORDER BY ECOMNAME DESC"
    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        print(record)

    """if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        cursor = connection.cursor()
        cursor.execute("select database();")

        record = cursor.fetchone()
        print("You're connected to database: ", record)

    """




except Error as e:

    print("Error while connecting to MySQL.", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
