-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER $$
CREATE TRIGGER resets_valid_email
AFTER UPDATE
ON users FOR EACH ROW
BEGIN
	set users.valid_email = 1 - users.valid_email;
	WHERE user.email = NEW.email;
END$$
DELIMITER ;
