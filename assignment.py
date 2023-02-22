# Q1. What is a database? Differentiate between SQL and NoSQL databases.

    # Database is organized collection of data
    # SQL	                                                                                    NoSQL
    # RELATIONAL DATABASE MANAGEMENT SYSTEM (RDBMS)              	      Non-relational or distributed database system.
    # These databases have fixed or static or predefined schema	          They have dynamic schema
    # These databases are not suited for hierarchical data storage.	      These databases are best suited for hierarchical data storage.
    # These databases are best suited for complex queries	              These databases are not so good for complex queries
    # Vertically Scalable	                                              Horizontally scalable
    # Follows ACID property	                                              Follows CAP(consistency, availability, partition tolerance)
    # Examples: MySQL, PostgreSQL, Oracle, MS-SQL Server, etc	          Examples: MongoDB, GraphQL, HBase, Neo4j, Cassandra, etc

# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
    # DDL or Data Definition Language actually consists of the SQL commands that can 
    # be used to define the database schema. It simply deals with descriptions of the database schema 
    # and is used to create and modify the structure of database objects in the database. 
    # DDL is a set of SQL commands used to create, modify, and delete database structures but not data. 
    # These commands are normally not used by a general user, who should be accessing the database via an application.
    # List of DDL commands: 
    # CREATE: This command is used to create the database or its objects (like table, index, 
    # function, views, store procedure, and triggers).

    # DROP: This command is used to delete objects from the database.

    # ALTER: This is used to alter the structure of the database.

    # TRUNCATE: This is used to remove all records from a table, including all spaces allocated for the records are removed.

# Create a database
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)
print(mydb)
my_cursor=mydb.cursor()
my_cursor.execute("create database if not exists data_base")
mydb.close()

# Create a table

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)
print(mydb)
my_cursor=mydb.cursor()
my_cursor.execute("create table if not exists data_base.table1 (c1 int, c2 varchar(40))")
mydb.close()

# alter 

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)
print(mydb)
my_cursor=mydb.cursor()
my_cursor.execute("alter table data_base.table1 add (c5 char(30))")
mydb.close()

# Truncate
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)
print(mydb)
my_cursor=mydb.cursor()
my_cursor.execute("Truncate table data_base.table1")
mydb.close()

# drop
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)
print(mydb)
my_cursor=mydb.cursor()
my_cursor.execute("Drop table data_base.table1")
mydb.close()

                
#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

    #The SQL commands that deals with the manipulation of data present in the 
    # database belong to DML or Data Manipulation Language and this includes most of the SQL statements.
    #  It is the component of the SQL statement that controls access to data and to the database.
    # Basically, DCL statements are grouped with DML statements.
    # List of DML commands:
    # INSERT : It is used to insert data into a table.
    # UPDATE: It is used to update existing data within a table.
    # DELETE : It is used to delete records from a database table.

#Table is created
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
print(mydb)
my_cursor=mydb.cursor()
my_cursor.execute('CREATE TABLE if not exists data_base.table2 (c1 int, c2 varchar(40)) ')
mydb.close()

#INSERT DATA Into table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
print(mydb),
my_cursor=mydb.cursor()
my_cursor.execute('insert into data_base.table2 values(1224, "PWSKILLS")')
my_cursor.execute('insert into data_base.table2 values(2005, "DATA SCIENCE")')
mydb.close()

#update
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
print(mydb),
my_cursor=mydb.cursor()
my_cursor.execute('UPDATE data_base.table2 SET c2 = "SKILLS" WHERE c2 = "PWSKILLS"')
mydb.close()

#delete
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
print(mydb),
my_cursor=mydb.cursor()
my_cursor.execute('DELETE from data_base.table2 WHERE c2 = "PWSKILLS"')
mydb.close()

#Q4. What is DQL? Explain SELECT with an example.
    #DQL statements are used for performing queries on the data within schema objects
    # Select -- the result is compiled into a further temporary table, 
    # which is displayed or perhaps received by the program

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
print(mydb),
my_cursor=mydb.cursor()
my_cursor.execute('SELECT * FROM data_base.table2')
mydb.close()

#Q5. Explain Primary Key and Foreign Key.
    #Primary Key: A primary key is used to ensure that data in the specific column is unique.
    #  A column cannot have NULL values. It is either an existing table column or a column that 
    # is specifically generated by the database according to a defined sequence. 

    # Foreign Key: 
    # A foreign key is a column or group of columns in a relational database table that provides 
    # a link between data in two tables. It is a column (or columns) that references a column 
    # (most often the primary key) of another table. 

#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
    #Cursor() The cursor () method is used to create a cursor object, which is used to execute SQL queries. 
    #execute () method is used to execute an SQL query, 
    #fetchall () method is used to fetch all the rows of the result set
    
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
print(mydb),
my_cursor=mydb.cursor()
my_cursor.execute('SELECT * FROM data_base.table2')
mydb.close()

#Q7. Give the order of execution of SQL clauses in an SQL query.
    #FROM
    #   ON
    #   JOIN
    #   WHERE
    #   GROUP BY
    #   WITH CUBE or WITH ROLLUP
    #   HAVING
    #   SELECT
    #   DISTINCT
    #   ORDER BY
    #   TOP