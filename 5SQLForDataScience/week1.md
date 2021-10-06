# Week 1 Basic SQL
## Welcome
- top three skill for data scientist
- used to communicate with databases
- advantages
    - boost professional profile
    - understanding of relational databases
    
## Intro
- Language used for relational databases
- Structured query language
- Data is facts that can be words, numbers or even pictures. Needs to be secure
- Database is a repository of data. Provides data functionality
- Tabular form == relational
- Database management system - software to manage database (DBMS, RDBMS for relational)
    - MySQL, Oracle, IBM DB2
    
- Basic commands include insert, select, update, delete

## SELECT Statement
- Retrieve rows from table
- It's a data manipulation language statement (DML)
- Example: SELECT * from Book
- Specify columns for subset: SELECT book_id, title FROM Book
- Restrict result set with WHERE clause
    - requires a predicate to valuate to True, False or Unknown
    - WHERE book_id = "B1"
    
## COUNT, DISTINCT, LIMIT
- COUNT(): retrieve number of rows that matches sql criteria
- DISTINCT: remove duplicate values from result set
- LIMIT: restricting number of rows retrieved from database


## INSERT Statement
- Adding rows to a table
- INSERT INTO table_name (column_names) VALUES (row_values)
- Can insert multiple rows: VALUES (values_1), (values_2)

## UPDATE and DELETE Statements
- Alter data with UPDATE
- UPDATE table_name SET column=value WHERE condition
- Remove rows with DELETE
- DELETE FROM table_name WHERE condition
- 