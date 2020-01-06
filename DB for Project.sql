#creating database to use in Project

create table handbag (
	id int NOT NULL auto_increment,
	designer varchar(250),
	handbag varchar(250),
    price int,
	PRIMARY KEY(id)
);

