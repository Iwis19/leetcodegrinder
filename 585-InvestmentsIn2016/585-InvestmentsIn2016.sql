-- Write your PostgreSQL query statement below

-- needed tons of help with syntax, but had the right idea with subqueries and noted the syntax down!

WITH duplicate_tiv2015 AS (  -- nondistinct tiv_2015 value
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
), distinct_lat_lon AS (   -- distinct lat, lon
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)

SELECT SUM(tiv_2016)::NUMERIC(10,2) AS tiv_2016
FROM Insurance
WHERE (lat, lon) IN (SELECT lat, lon FROM distinct_lat_lon)
AND tiv_2015 IN (SELECT tiv_2015 FROM duplicate_tiv2015);
