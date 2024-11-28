-- Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or
-- returns 0 if the second number is equal to 0.

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT DETERMINISTIC
BEGIN 
DECLARE result INT;
SET result = 0;
IF b = 0 THEN
return result;
ELSE
SET result = a / b;
END IF;
return result;
END $$
DELIMITER ;
