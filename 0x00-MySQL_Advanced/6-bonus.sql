DELIMITER $$

CREATE PROCEDURE IF NOT EXISTS AddBonus (IN userID INT, IN project_name VARCHAR(255), IN scoreID INT)
BEGIN
    DECLARE project_id INT;
    -- SET @project_id = (SELECT '1' FROM projects WHERE projects.name=project_name);
    IF EXISTS (SELECT '#' FROM projects WHERE projects.name=project_name INTO projectID)
        BEGIN
            INSERT INTO corrections (user_id, project_id, score) VALUES (userID, projectID, scoreID);
        END
    ELSE
        SELECT 'NOT FOUND';
    END IF;
END$$
DELIMITER ;
