# Week 2 Relational Database Concepts
## Concepts
- Relational model is most used
- Allows for data independence
- Stored in tables
- Entity Relationship Model
    - tool to design relational databases
    - ER diagrams, entity == square, attributes == circles
    
- Entities become tables
- Attributes translated to columns
- Primary and foreign keys
    - Primary uniquely identifies row
    - Foreign are primaries from other tables (to define relationships)
    
## How to create database instance on cloud
- Built and access through a cloud platform
- Some advantages: ease of use, scalability, disaster recovery
- Examples
    - IBM Db2
    - Oracle Database Cloud Service
    - Microsoft Azure SQL Database
    - Amazon Relational Database Services
    
- Database as a Service provide access without hardware and software setup
- Creating instance on IBM Db2 on Cloud (handled with included lab)

## Types of SQL Statements (DDL vs DML)
- DDL: data definition language, used to define, change or drop data
    - CREATE, ALTER, TRUNCATE, DROP
    
- DML: data manipulation language, read and modify data
    - CRUD operations
    - INSERT, SELECT, UPDATE, DELETE
    
## CREATE Table Statement
- CREATE TABLE table_name (
    column_name datatype optional_params,
    column_name datatype optional_params
  )
  
## ALTER, DROP and TRUNCATE Tables
- ALTER: add or remove columns, modify data types, add or remove keys, add or remove constraints
    - ALTER TABLE table_name ADD COLUMN column_name datatype
    - SET DATA TYPE datatype
    - DROP COLUMN column_name
    
- DROP TABLE table_name: to delete table
- TRUNCATE TABLE table_name IMMEDIATE: to delete all rows in table

## 