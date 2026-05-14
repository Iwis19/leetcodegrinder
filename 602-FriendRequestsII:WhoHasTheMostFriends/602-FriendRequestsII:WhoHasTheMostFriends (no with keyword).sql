-- Write your PostgreSQL query statement below

SELECT id, freq AS num
FROM (
    SELECT id, COUNT(*) AS freq
    FROM (
        SELECT requester_id AS id
        FROM RequestAccepted
        UNION ALL
        SELECT accepter_id
        FROM RequestAccepted
    ) 
    GROUP BY id
) 
WHERE freq = ( -- checks if the frequency is equal to max freq
    SELECT MAX(freq) AS most_frequent
    FROM (
        SELECT COUNT(*) AS freq
        FROM (
            SELECT requester_id AS id
            FROM RequestAccepted
            UNION ALL
            SELECT accepter_id
            FROM RequestAccepted
        ) 
        GROUP BY id
    )
);



