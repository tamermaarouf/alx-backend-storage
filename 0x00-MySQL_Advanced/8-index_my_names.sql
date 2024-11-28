DELIMITER $$
DROP INDEX idx_name_first on names;
CREATE INDEX idx_name_first
ON names(name(1));
DELIMITER ;
