-- Write your PostgreSQL query statement below

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (  -- checks how many distinct product keys there are from just this one customer
    SELECT COUNT(product_key) AS amount -- see if it equals to the total amt of product keys there are
    FROM Product
);
