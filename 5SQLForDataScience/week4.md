# Week 4 Accessing Databases Using Python
## How To Overview
- Python has a Database API module
- Typically, the flow is user <> Notebook <> DBMS through SQL API
- Each database system has its own SQL API library

## Writing Code Using DB-API
- Python's standard API for accessing relational databases
- Benefits:
    - easy to implement
    - consistency
    - portable across databases
    
- Concepts
    - Connection objects: manage connections and transactions
    - Cursor objects: queries, get results
    
- Connection methods examples
    - .cursor()
    - .commit()
    - .rollback()
    - .close()
    
- Cursor method examples
    - .execute()
    - .fetchone()
    - .fetchall()
    - .nextset()
    
- Writing the code
    - create connection object
    - create cursor object 
    - run queries with cursor
    - free resources with close
    
## Connecting to a database using ibm_db API
- Properties of connection credentials: driver, database, host, port, protocol, user ID, password
- Always close the connection at the end to free up resources

## Creating Tables, Loading Data and Querying Data
- .exec_immediate(): params are connection, statement, options
- .fetch_both(): pass in statement param
- using Pandas: .read_sql()

## Analyzing Data with Python
- Use dataframe .describe() to learn about your data, provides summary statistics
- Examples with seaborn package for visualizations
  - Scatter and box plots
