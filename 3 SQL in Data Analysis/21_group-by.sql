USE ecom;

SELECT city, COUNT(*) AS total_orders
FROM orders
GROUP BY city;

SELECT category, COUNT(*) AS total_orders
FROM orders
GROUP BY category;


SELECT category, COUNT(*) AS total_orders, SUM(quantity * price_per_unit) AS total_sales
FROM orders
GROUP BY category;

SELECT city, AVG(price_per_unit) AS avg_price
FROM orders
GROUP BY city;

SELECT city, order_status, COUNT(*) AS count 
FROM orders
GROUP BY city, order_status;


-- HAVING CLAUSE:- To filter when there is GROUP BY...

SELECT city, order_status, COUNT(*) AS count 
FROM orders
GROUP BY city, order_status
HAVING city IN ("Delhi", "Mumbai");


SELECT city, order_status, COUNT(*) AS count 
FROM orders
GROUP BY city, order_status
ORDER BY count;