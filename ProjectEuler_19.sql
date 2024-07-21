-- Project Euler 19
-- https://projecteuler.net/problem=19
-- How many Sundays fell on the first of the month between 1901-01-01 & 2000-12-31?
USE master
GO

DECLARE @DATE DATE = '1901-01-01'

DROP TABLE IF EXISTS #Results;
CREATE TABLE #Results (SUNDAY_MONTH_STARTS DATE)

WHILE @DATE <= '2000-12-31'
BEGIN
	IF DATENAME(DW, @DATE) = 'Sunday'
		INSERT INTO 
			#Results
		VALUES
			(@DATE)
	SET @DATE = DATEADD(MONTH, 1, @DATE)
END

SELECT 
	COUNT(*)
FROM
	#Results