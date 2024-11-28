-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN userID INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT SUM(score*weight)/SUM(weight) FROM corrections WHERE user_id = userID)
	WHERE id = userID;
END $$
DELIMITER ;
