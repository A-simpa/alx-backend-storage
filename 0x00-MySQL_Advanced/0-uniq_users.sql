-- create a table called users
-- with an primary auto increment primary key id

CREATE TABLE IF NOT EXISTS `users`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`email` VARCHAR(255) UNIQUE NOT NULL,
	`name` VARCHAR(255),
	PRIMARY KEY(id));
