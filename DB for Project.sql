#Creating database to use in Project

create table handbag (
	id int NOT NULL auto_increment,
	designer varchar(250),
	handbag varchar(250),
    price int,
	PRIMARY KEY(id)
);

insert into handbag (designer, handbag,price) values ('Louis Vuitton','Alma bag', 1025); 
insert into handbag (designer, handbag,price) values ('Gucci','Quilted shoulder bag', 10000); 
insert into handbag (designer, handbag,price) values ('Balenciaga','City bag', 2200); 
insert into handbag (designer, handbag,price) values ('Dior','Sadle bag', 2800); 