import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Student',
                                         port='3306',
                                         user='root',
                                         password='root')
    print(connection)
    cursor = connection.cursor();
    #cursor.execute("CREATE DATABASE Student;")
    #print("Database created successfully")

    #cursor.execute("SHOW tables;")
    #database_list=cursor.fetchall()
    #print(database_list)

    #cursor.execute("use Student;")
    #cursor.execute("CREATE TABLE StudentInfo(RollNo int,Name varchar(30),address varchar(30))")
    #print("Table created successfully")

    print("---------------------------")
    cursor.execute("SHOW tables")
    table_list=cursor.fetchall()

    for table in table_list:
      print(table_list)

    query = "INSERT INTO `Student`.`StudentInfo`(`RollNo`,`Name`,`address`) VALUES (%s,%s,%s)"
   # values = ( 1, "Yogita","Nashik")
    #cursor.execute(query, values)
    #connection.commit()

    values = [
        (2,'Amazon','pune'),
        (3,'Myntra','sinnar'),

    ]
    ## executing the query with values - multiple entries
    cursor.executemany(query, values)
    ## to make final output we have to run the 'commit()' method of the database object
    connection.commit()

    print(cursor.rowcount, "record inserted")





except Error as e:

    print("Error while connecting to MySQL.", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")



