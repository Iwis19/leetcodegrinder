-- Write your PostgreSQL query statement below
/*
1. new syntax. added to my notes
2. NO BRACKETS ON CASE!
3. need to keep in touch with sql or else i will forget.

query: a query is something that is sent to the database. a query can be one that modifies value, or one that requests and returns value.
update itself does not return values from the database, it modifies values.
*/
UPDATE salary
SET sex = 
CASE 
WHEN sex = 'm' THEN 'f' 
ELSE 'm'
END;
