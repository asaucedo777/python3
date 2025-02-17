/**
 * ADVANCED SQL
 * */

-- Joins and Unions
  SELECT q.id AS q_id,
      MIN(TIMESTAMP_DIFF(a.creation_date, q.creation_date, SECOND)) as time_to_answer
  FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
      INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
  		ON q.id = a.parent_id
  WHERE q.creation_date >= '2018-01-01' and q.creation_date < '2018-02-01'
  GROUP BY q_id
  ORDER BY time_to_answer;

-- Time to answer
 SELECT q.id AS q_id,
      MIN(TIMESTAMP_DIFF(a.creation_date, q.creation_date, SECOND)) as time_to_answer
  FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
  	LEFT JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
  		ON q.id = a.parent_id
  WHERE q.creation_date >= '2018-01-01' and q.creation_date < '2018-02-01'
  GROUP BY q_id
  HAVING MIN(TIMESTAMP_DIFF(a.creation_date, q.creation_date, SECOND)) > 0
  ORDER BY time_to_answer;

-- Initial answers and questions
SELECT q.owner_user_id AS owner_user_id,
    MIN(q.creation_date) AS q_creation_date,
    MIN(a.creation_date) AS a_creation_date
FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
	FULL JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
		ON q.owner_user_id = a.owner_user_id 
WHERE q.creation_date >= '2019-01-01' AND q.creation_date < '2019-02-01' 
	AND a.creation_date >= '2019-01-01' AND a.creation_date < '2019-02-01'
GROUP BY owner_user_id;

-- Users joined in January 2019 with first post
SELECT u.id AS id,
     MIN(q.creation_date) AS q_creation_date,
     MIN(a.creation_date) AS a_creation_date
 FROM `bigquery-public-data.stackoverflow.users` AS u
     LEFT JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
         ON u.id = a.owner_user_id
     LEFT JOIN `bigquery-public-data.stackoverflow.posts_questions` AS q
         ON q.owner_user_id = u.id
 WHERE u.creation_date >= '2019-01-01' and u.creation_date < '2019-02-01'
 GROUP BY id;
 
-- distinct users posted on January 1, 2019
SELECT DISTINCT owner_user_id FROM (
      SELECT q.owner_user_id 
      FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
      WHERE EXTRACT(DATE FROM q.creation_date) = '2019-01-01'
      UNION ALL
      SELECT a.owner_user_id
      FROM `bigquery-public-data.stackoverflow.posts_answers` AS a
      WHERE EXTRACT(DATE FROM a.creation_date) = '2019-01-01'
)


/**Analytics functions
 * */
WITH trips_by_day AS (
	SELECT
		DATE(trip_start_timestamp) AS trip_date,
		COUNT(*) as num_trips
	FROM
		`bigquery-public-data.chicago_taxi_trips.taxi_trips`
	WHERE
		trip_start_timestamp > '2016-01-01'
		AND trip_start_timestamp < '2016-04-01'
	GROUP BY
		trip_date
	ORDER BY
		trip_date
)
SELECT
	trip_date,
	AVG(num_trips) OVER (
		ORDER BY trip_date
        ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING
    ) AS avg_num_trips
FROM
	trips_by_day;
	
-- Trips by community area
SELECT pickup_community_area,
    trip_start_timestamp,
    trip_end_timestamp,
    RANK() OVER (
        PARTITION BY pickup_community_area
        ORDER BY trip_start_timestamp
    ) AS trip_number
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE DATE(trip_start_timestamp) = '2013-10-03';

-- Time elapsed between trips
SELECT taxi_id,
       trip_start_timestamp,
       trip_end_timestamp,
       TIMESTAMP_DIFF(
           trip_start_timestamp, 
           LAG(trip_end_timestamp) 
               OVER (
                    PARTITION BY taxi_id 
                    ORDER BY trip_end_timestamp), 
           MINUTE) as prev_break
   FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
   WHERE DATE(trip_start_timestamp) = '2013-10-03';
  

/** Nested and Repeated DATA
  */

 -- Most common committers
SELECT committer.name AS committer_name, COUNT(1) AS num_commits FROM `bigquery-public-data.github_repos.sample_commits`
WHERE EXTRACT(YEAR FROM committer.date) = 2016
GROUP BY committer.name
ORDER BY num_commits DESC;

-- Languages
SELECT *
FROM `bigquery-public-data.github_repos.languages`;

-- Most popular programming language
SELECT languages_list.name language_name, COUNT(1) AS num_repos
FROM `bigquery-public-data.github_repos.languages` AS languages, UNNEST(language) AS languages_list
GROUP BY languages_list.name
ORDER BY num_repos DESC;

-- Which languages are used in the repository with the most languages
WITH MostLanguagesRepo AS (
	SELECT languages.repo_name, COUNT(1) AS num_languages
	FROM `bigquery-public-data.github_repos.languages` AS languages, UNNEST(language) AS languages_list
	GROUP BY languages.repo_name
	ORDER BY num_languages DESC
	LIMIT 1
)
SELECT languages_list.name, languages_list.bytes
FROM MostLanguagesRepo
	INNER JOIN `bigquery-public-data.github_repos.languages` AS languages
		ON languages.repo_name = MostLanguagesRepo.repo_name, UNNEST(language) AS languages_list
WHERE languages.repo_name = MostLanguagesRepo.repo_name;


/** Writting Efficient Queries
 */
-- show_amount_of_data_scanned() shows the amount of data the query uses.
-- show_time_to_run() prints how long it takes for the query to execute.

