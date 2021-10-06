# Week 5 Working With Real Databases (Assignment Prep)
## Working with Real World Datasets
- many are in csv files
- use double quotes to specify mixed case column names
- spaces default to underscores when loading data
- can use \ to split queries into multiple lines, or use sql magic (%%sql)
- use LIMIT to get sample of data

## Getting Table and Column Details
- DB2: SYSCAT.TABLES (select * from syscat.tables where tabschema = 'your_schema')
- Columns: select * from syscat.columns where tabname = 'your_table'