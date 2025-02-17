/**
 * Getting Started With SQL and BigQueery
 */
SELECT * FROM `bigquery-public-data.chicago_crime.INFORMATION_SCHEMA.TABLES`;

-- Mostrar todos los datos de la tabla 'crime' del dataset 'chicago_crime'
SELECT * FROM `bigquery-public-data.chicago_crime.crime`;

-- Resumen de crímenes por año
SELECT YEAR, COUNT(1) AS CUENTA FROM `bigquery-public-data.chicago_crime.crime`
GROUP BY YEAR 
ORDER BY YEAR DESC
;

/**
 * Select, From and Where
 */
SELECT DISTINCT country FROM `bigquery-public-data.openaq.global_air_quality` 
WHERE unit = 'ppm';

-- All rows with value = 0
SELECT * FROM `bigquery-public-data.openaq.global_air_quality` 
WHERE value = 0;


/**
 * Group by, Having and Count
 * */
SELECT FULL_TABLE.BY AS author, COUNT(1) AS NumPost FROM `bigquery-public-data.hacker_news.full` AS FULL_TABLE
GROUP BY 1
HAVING COUNT(1) > 10000;

-- COUNT DELETED
SELECT COUNT(1) AS NumDeleted FROM `bigquery-public-data.hacker_news.full` AS FULL_TABLE
WHERE deleted;

/**
 * Order by
 * */
SELECT country_name, avg(value) AS avg_ed_spending_pct
FROM `bigquery-public-data.world_bank_intl_education.international_education`
WHERE indicator_code = 'SE.XPD.TOTL.GD.ZS' AND year BETWEEN 2010 AND 2017
GROUP BY country_name
ORDER BY avg_ed_spending_pct DESC ;

-- All codes with almost 175 rows in 2016
SELECT indicator_code, indicator_name, COUNT(1) AS num_rows 
FROM `bigquery-public-data.world_bank_intl_education.international_education`
WHERE year = 2016
GROUP BY indicator_code, indicator_name
HAVING COUNT(1) >= 175 
ORDER BY num_rows DESC ;

/**
 * As and With
 * */
SELECT EXTRACT(YEAR FROM trip_start_timestamp) AS year, COUNT(1) AS num_trips
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
GROUP BY year;

-- group by month
SELECT EXTRACT(MONTH FROM trip_start_timestamp) AS month, COUNT(1) AS num_trips
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE EXTRACT(YEAR FROM trip_start_timestamp) = 2016
GROUP BY month
ORDER BY month;

-- group by hour
WITH RelevantRides AS (
	SELECT
		trip_start_timestamp,
		trip_miles,
		trip_seconds
	FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
	WHERE 
		trip_start_timestamp > '2016-01-01' AND trip_start_timestamp < '2016-04-01'
		AND trip_seconds > 0
		AND trip_miles > 0
)
SELECT
	EXTRACT(HOUR FROM trip_start_timestamp) AS hour_of_day,
	COUNT(1) AS num_trips,
	(3600 * SUM(trip_miles) / SUM(trip_seconds)) AS avg_mph
FROM RelevantRides
GROUP BY hour_of_day
ORDER BY hour_of_day;

/**
 * Joining Data
 * */
SELECT * FROM `bigquery-public-data.stackoverflow.posts_questions`
WHERE tags LIKE '%bigquery%';

-- First join
SELECT answers.id, answers.body, answers.owner_user_id
FROM `bigquery-public-data.stackoverflow.posts_questions` AS questions
INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS answers ON questions.id = answers.parent_id
WHERE questions.tags LIKE '%bigquery%';

-- Number of answers by user
SELECT answers.owner_user_id AS user_id, COUNT(1) AS number_of_answers
FROM `bigquery-public-data.stackoverflow.posts_questions` AS questions
INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS answers ON questions.id = answers.parent_id
WHERE questions.tags LIKE '%bigquery%'
GROUP BY answers.owner_user_id
HAVING COUNT(1) > 0
ORDER BY answers.owner_user_id
