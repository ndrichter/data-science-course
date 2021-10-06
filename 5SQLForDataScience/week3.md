# Week 3 Intermediate SQL
## Using String Patterns and Ranges
- using LIKE and string patterns: WHERE firstname LIKE 'R%'
    - % is a wildcard character
    
- using a range: WHERE pages BETWEEN 290 and 300
- using a set of values: WHERE country IN ('AS', 'BZ')

## Sorting Result Sets
- ORDER BY clause
    - ORDER BY column_name
    - can use DESC or ASC
    - can specify column sequence number instead of column name
    
## Grouping Result Sets
- DISTINCT to eliminate duplicates in result set
- GROUP BY clause
    - group results into subsets
    - SELECT country, COUNT(country) as Count from Author group by country
    
- HAVING
    - restrict result set when using the group by clause
    - HAVING count(country) > 4
    
## Built-in Database Functions
- Aggregate or column functions
    - SUM, MIN, MAX, AVG etc.
    
- Mathematical operations can be performed between two columns
- SCALAR AND STRING functions
  - ROUND, LENGTH, UCASE, LCASE
  - UCASE and LCASE useful for where clauses
  
## Date and Time Built In Functions
- DBs typically have special data types for dates and times
- DATE, TIME, TIMESTAMP
- Some examples:
  - Day(): extract day from date, can be used in where clause
  - Can perform date or time arithmetic (some_column date + 3 days)
  - CURRENT_DATE, CURRENT_TIME
  
## Sub Queries and Nested Selects
- Query inside another query
- Use sub queries to evaluate aggregate functions (like AVG)
- Can substitute column name with a subquery to create a column expression
- Substitute table name with a sub query to created derived table or table expression

## Working with Multiple Tables
- Use sub queries, implicit JOIN, and JOIN operators
- implicit JOIN
  - full join: cartesian join, select * from employees, departments
  - select * from employees e , departments d where e.dep_id = d.dept_id_dep