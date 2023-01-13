-- create a table called users
-- having a default colum country which can be US, CO, TN

CREATE TABLE IF NOT EXISTS `users`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`email` VARCHAR(255) UNIQUE NOT NULL,
	`name` VARCHAR(255),
	`country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT('US'),
	PRIMARY KEY(id));
