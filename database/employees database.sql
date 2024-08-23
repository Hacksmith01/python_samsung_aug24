show databases;
create database  employee;
use employee;
create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);
show tables;
select * from employees;
INSERT INTO employees (name, designation, technology, phone_num, commission, salary, years_of_exp) VALUES
('Alice Johnson', 'Software Engineer', 'Java', 1234567890, 5000, 75000.00, 5),
('Bob Smith', 'Project Manager', 'Python', 2345678901, NULL, 85000.00, 8),
('Carol Davis', 'UX Designer', 'JavaScript', 3456789012, 3000, NULL, 4),
('David Wilson', 'QA Engineer', 'Selenium', 4567890123, 2000, 65000.00, 6),
('Emma Brown', 'Database Administrator', 'SQL', 5678901234, NULL, 72000.00, 7),
('Frank Moore', 'DevOps Engineer', 'AWS', 6789012345, 4000, NULL, 3),
('Grace Taylor', 'System Analyst', 'Java', 7890123456, NULL, 68000.00, 6),
('Hannah Lee', 'Network Engineer', 'Cisco', 8901234567, 2500, 70000.00, 5),
('Ian White', 'Business Analyst', 'Tableau', 9012345678, NULL, 55000.00, 2),
('Judy Harris', 'Security Specialist', 'Cybersecurity', 1234567899, 6000, 78000.00, 9);

-- updating salary and technology they worked for
update employees set salary = 100000 , technology = 'Cybersaftey' where id = 10; 
update employees set years_of_exp=5 where id = 7; 

-- alter table (meta data) employees add constraint not null to years_of_exp
alter table employees modify years_of_exp int not null;

-- alter table employees change thw datatype of phone_num from int to str
alter table employees modify phone_num varchar(10);

-- delete the employees who have the designation System Analyst
delete from employees where designation='System Analyst';

-- delete the employee with a specific id
delete from employees where id=2;
select * from employees;

-- search for a person with specific id
select * from employees where id = 10;

-- search for a person with specific designation
select * from employees where designation = 'Business Analyst';

select * from employees;
update employees set id auto_increment=1 where ;

-- (group by)print the average salaries of employees with diffrent disignations
select designation,avg(salary) from employees group by avg;
