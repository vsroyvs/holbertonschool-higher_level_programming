## SQL - More queries
# Learning Objectives
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION
Ex:


		CREATE TABLE shop (
		 article INT(4) UNSIGNED ZEROFILL DEFAULT '0000' NOT NULL,
		 dealer  CHAR(20)                 DEFAULT ''     NOT NULL,
		 price   DOUBLE(16,2)             DEFAULT '0.00' NOT NULL,
		 PRIMARY KEY(article, dealer));

		INSERT INTO shop VALUES
		(1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),(3,'C',1.69),
		(3,'D',1.25),(4,'D',19.95);
