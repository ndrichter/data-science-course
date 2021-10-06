-- Problem 1 --
-- create query that will fail on execution --
-- Invalid use of an aggregate function --
select *
from employees
where salary < avg(salary);

-- Problem 2 --
-- Working query from scenario above --
select *
from employees
where salary < (select avg(salary) from employees);

-- Problem 3 --
-- Query fails on execution --
-- not specified in the GROUP BY clause --
select emp_id, salary, max(salary) as max_salary
from employees;

-- Problem 4 --
-- Working query from above scenario --
select emp_id, salary, (select max(salary) from employees) as max_salary
from employees;

-- Problem 5 --
select *
from ( select EMP_ID, F_NAME, L_NAME, DEP_ID from employees) AS EMP4ALL;