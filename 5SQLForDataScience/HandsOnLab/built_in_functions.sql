-- Exercise 1: create the pet rescue table and populate --

-- Drop the PETRESCUE table in case it exists
drop table PETRESCUE;
-- Create the PETRESCUE table
create table PETRESCUE (
	ID INTEGER NOT NULL,
	ANIMAL VARCHAR(20),
	QUANTITY INTEGER,
	COST DECIMAL(6,2),
	RESCUEDATE DATE,
	PRIMARY KEY (ID)
	);
-- Insert sample data into PETRESCUE table
insert into PETRESCUE values
	(1,'Cat',9,450.09,'2018-05-29'),
	(2,'Dog',3,666.66,'2018-06-01'),
	(3,'Dog',1,100.00,'2018-06-04'),
	(4,'Parrot',2,50.00,'2018-06-04'),
	(5,'Dog',1,75.75,'2018-06-10'),
	(6,'Hamster',6,60.60,'2018-06-11'),
	(7,'Cat',1,44.44,'2018-06-11'),
	(8,'Goldfish',24,48.48,'2018-06-14'),
	(9,'Dog',2,222.22,'2018-06-15')
;

-- Exercise 2: Aggregate Functions --
select sum(COST)
from PETRESCUE;

select sum(COST) as SUM_OF_COST
from PETRESCUE;

select max(quantity)
from petrescue;

select avg(cost)
from petrescue;

select avg(cost / quantity)
from petrescue
where animal = 'Dog';

-- Exercise 3: Scalar and String Functions
select round(cost)
from petrescue;

select length(animal)
from petrescue;

select ucase(animal)
from petrescue;

select distinct ucase(animal)
from petrescue;

select *
from petrescue
where lcase(animal) = 'cat';

-- Exercise 4: Date and Time Functions --
select day(rescuedate)
from petrescue
where lcase(animal) = 'cat';

select sum(quantity)
from petrescue
where month(rescuedate) = 5;

select sum(quantity)
from petrescue
where day(rescuedate) = 14;

select (rescuedate + 3 days)
from petrescue;

select current_date - rescuedate
from petrescue;

