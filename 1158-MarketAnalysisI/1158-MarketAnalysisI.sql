-- Write your PostgreSQL query statement below

-- for each user, find: join date, # of orders in 2019
-- ignore items table & fav brand

/*
minimal help, a bit of syntax :)

initial submission was 300 ms slower than currently, because i used full outer join. it was very expensive and unnecessary here since the db engine
has to account for null filled rows, track unmatched left row, right row, etc. left join is much simpler as db knows to keep the entirety of Users

but im happy abt th eprogress
*/

WITH buyer_2019 AS (
    SELECT buyer_id, COUNT(*) AS orders_in_2019
    FROM Orders
    WHERE order_date BETWEEN '2019-01-01' AND '2019-12-31'
    GROUP BY buyer_id
)

SELECT u.user_id AS buyer_id, u.join_date, COALESCE(b.orders_in_2019, 0) AS orders_in_2019
FROM Users u 
LEFT JOIN buyer_2019 b 
ON u.user_id = b.buyer_id;

1
