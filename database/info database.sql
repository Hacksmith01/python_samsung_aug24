show databases;
-- lists the available databases
select database();
use sys;
create database mine;
use mine;
show tables;
drop database mine;
show databases;
create database info;
create table persons(id int primary key auto_increment, name varchar(20) not null ,location varchar(50), age int check(age>0));
use info;
create table persons(id int primary key auto_increment, name varchar(20) not null ,location varchar(50), age int check(age>0));
show tables;
select * from persons;
insert into persons(id,name,location,age) values(1,"tata","bangalore",100);
insert into persons(id,name,location,age) values(2,"ratan","mumbai",60);
insert into persons(id,name,location,age) values(3,"Alice","Los Angeles",50);
insert into persons(id,name,location,age) values(4,"Bob","Chicago",45);
insert into persons(id,name,location,age) values(5,"Michael",NULL,50);
insert into persons(id,name,location,age) values(6,"Michael",NULL,50);
insert into persons(id,name,location,age) values(7,"James",NULL,40);
insert into persons(id,name,location,age) values(8,"Sophia","Houston",NULL);
insert into persons(id,name,location,age) values(9,"Daniel",NULL,60);
insert into persons(id,name,location,age) values(10,"Olivia","Boston",NULL);
insert into persons(id,name,location,age) values(11,"David",NULL,55);
insert into persons(id,name,location,age) values(12,"Ava","Dallas",NULL);
insert into persons(id,name,location,age) values(13,"Liam","Seattle",28);
insert into persons(id,name,location,age) values(14,"Isabella",NULL,65);
insert into persons(id,name,location,age) values(15,"Ethan","Atlanta",NULL);
insert into persons(id,name,location,age) values(16,"Mia","Philadelphia",33);
insert into persons(id,name,location,age) values(17,"Noah",NULL,70);
insert into persons(id,name,location,age) values(18,"Lucas","Chicago",NULL);
select * from persons;
select name, location from persons;
select distinct location from persons;
select name from persons where age<40;
select * from persons where location = "bangalore";
select * from persons where age between 40 and 50;
select * from persons where age in(40,70,33);
select * from persons where name in("ratan","tata");
select * from persons where location = null;
select * from persons where location is null;
select * from persons where location = 'null';




