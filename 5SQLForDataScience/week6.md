# Week 6 Advanced SQL
## Views
- Alternate way to represent data of a table
- Show selection of data, or combine more than one table into a view
- CREATE OR REPLACE VIEW view_name (column_alias) AS SELECT column FROM table
    - REPLACE is used to update the view
    
- DROP VIEW to remove

## Stored Procedures
- Set of SQL stored and executed on the database server
- Can be written in many languages
- Accept params
- Reduction in network traffic, improved performance, reusable code, increased security
- CREATE PROCEDURE
- CALL procedure_name

## ACID Transactions
- Transaction must complete fully successfully, or not all 
- Atomic, Consistent, Isolated, Durable
- BEGIN (implicit), COMMIT, ROLLBACK if fail
- Can be issued by other languages, like Python

## JOIN Statements
- Combines two or more tables based on a relationship
- Relationship based on primary and foreign keys to join on
- Different types of joins:
  - Inner, Outer (Left, Full, Right)
  
- Inner is most common, displays matches only
- Using an alias to define the tables
- Outer joins return rows that do not have match between joins
- Left outer join: All left table and matching rows from right table
  - LEFT JOIN
  
- Right outer join: All left table and matching rows from left table
  - RIGHT JOIN
  
- Full outer join: return rows from both tables, matching and non matching
  - FULL JOIN