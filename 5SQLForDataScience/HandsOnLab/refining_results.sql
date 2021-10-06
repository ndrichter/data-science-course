-- Exercise 1: String Patterns --
-- Question 1 --
select *
from employees
where address like '%Elgin,IL%';

-- Question 2 --
select *
from employees
where b_date like '197%';

-- Question 3 --
select *
from employees
where dep_id = 5
and salary between 60000 and 70000;

-- Exercise 2: Sorting --
-- Question 1 --
select *
from employees
order by dep_id;

-- Question 2 --
select *
from employees
order by dep_id desc, l_name desc;

-- Question 3 --
select *
from employees e join departments d on e.dep_id = d.dept_id_dep
order by d.dep_name desc, e.l_name desc;

-- Exercise 3: Grouping --
-- Question 1 --
select dep_id, count(f_name)
from employees
group by dep_id;

-- Question 2 --
select dep_id, count(f_name), avg(salary)
from employees
group by dep_id;

-- Question 3 --
select dep_id, count(f_name) as NUM_EMPLOYEES, avg(salary) as AVG_SALARY
from employees
group by dep_id;

-- Question 4 --
select dep_id, count(f_name) as NUM_EMPLOYEES, avg(salary) as AVG_SALARY
from employees
group by dep_id
order by AVG_SALARY;

-- Question 5 --
select dep_id, count(f_name) as NUM_EMPLOYEES, avg(salary) as AVG_SALARY
from employees
group by dep_id
having count(f_name) < 4
order by AVG_SALARY;
