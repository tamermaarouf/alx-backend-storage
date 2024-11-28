-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- Requirements:
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction


DELIMITER $$

DROP PROCEDURE IF EXISTS AddBonus $$
CREATE PROCEDURE AddBonus(IN userID INT, IN project_name VARCHAR(255), IN scoreID INT)
BEGIN
	DECLARE projectID INT;
	SELECT projects.id INTO projectID FROM projects WHERE projects.name=project_name;
	IF projectID > 0 THEN
		INSERT INTO corrections(user_id, project_id, score) VALUES (userID , projectID , scoreID );
	ELSE
		INSERT INTO projects (name) VALUES (project_name);
		SET @project_py = LAST_INSERT_ID();
		INSERT INTO corrections(user_id, project_id, score) VALUES (userID, @project_py,scoreID);
END IF;
END $$
DELIMITER ;
