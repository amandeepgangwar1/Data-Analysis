USE ecom;
SELECT * FROM order_details;

-- SELECT AVG(price_per_unit) FROM order_details;
SELECT * FROM order_details
WHERE price_per_unit > (
		SELECT AVG(price_per_unit) FROM order_details
	);
    
SELECT * FROM order_details
WHERE city IN (
		SELECT city FROM order_details WHERE category = "Electronics"
	);
    
    
    
    
SELECT order_id, customer_name, price_per_unit,
(SELECT AVG (price_per_unit) FROM orders) AS average FROM orders;

SELECT *,
(SELECT AVG (price_per_unit) FROM orders) AS average FROM orders;


SELECT * FROM orders o
WHERE EXISTS (
	SELECT 1
    FROM orders
    WHERE city = o.city
		AND category = "Furniture"
);