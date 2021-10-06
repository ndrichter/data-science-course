-- Exercise 1: Access multiple tables with sub queries --
-- Problem 1 --
select * from employees
where JOB_ID IN (select JOB_IDENT from jobs);

-- Problem 2 --
select *
from employees
where JOB_ID IN (
	select JOB_IDENT
	from jobs
	where JOB_TITLE= 'Jr. Designer'
);

-- Problem 3 --
select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT
from jobs
where JOB_IDENT IN (
	select JOB_ID
	from employees
	where SALARY > 70000
);

-- Problem 4
select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT
from jobs
where JOB_IDENT IN (
	select JOB_ID
	from employees
	where YEAR(B_DATE)>1976
);

-- Problem 5 --
select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT
from jobs
where JOB_IDENT IN (
	select JOB_ID
	from employees
	where YEAR(B_DATE)>1976 and SEX='F'
);

-- Exercise 2: access multiple tables with implicit joins --
-- Problem 1 --
select *
from employees, jobs;

-- Problem 2 --
select *
from employees, jobs
where employees.JOB_ID = jobs.JOB_IDENT;

-- Problem 3 --
select *
from employees E, jobs J
where E.JOB_ID = J.JOB_IDENT;

-- Problem 4 --
select EMP_ID,F_NAME,L_NAME, JOB_TITLE
from employees E, jobs J
where E.JOB_ID = J.JOB_IDENT;

-- Problem 5 --
select E.EMP_ID,E.F_NAME,E.L_NAME, J.JOB_TITLE
from employees E, jobs J
where E.JOB_ID = J.JOB_IDENT;




