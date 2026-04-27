# Write your MySQL query statement below

-- i think i am too attached to inner join because i just used it in the previous problem i already know im gonna start thinking about left join in my next one i need to be more familiarized

SELECT name as Customers
FROM Customers
LEFT JOIN Orders
ON Customers.id = Orders.customerId
WHERE Orders.customerId IS NULL;
