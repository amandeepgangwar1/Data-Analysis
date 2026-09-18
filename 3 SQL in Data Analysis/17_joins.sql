USE ecom;
UPDATE orders SET seller_id = NULL WHERE order_id IN (1, 4, 9);
UPDATE orders SET seller_id = 2 WHERE order_id IN (2, 3, 7, 8, 10, 11, 12);
UPDATE orders SET seller_id = 99 WHERE order_id IN (2, 7);
SELECT * FROM orders;

INSERT INTO sellers VALUES 
	(1, "Dawn", "Delhi"), 
    (2, "Dawn Electronics", "Banglore"), 
    (3, "Night Electronics", "Mumbai"), 
    (4, "Night Electronics 2", "Kolkata");


    
--     -- INNER JOIN
-- SELECT 
-- o.order_id, o.product, o.city AS customer_city,
-- s.seller_name
-- FROM orders o
-- INNER JOIN sellers s
-- ON o.seller_id = s.seller_id

-- SELECT * FROM sellers;


-- LEFT JOIN

-- SELECT 
-- o.order_id, o.product, o.city AS customer_city,
-- s.seller_name
-- FROM orders o
-- LEFT JOIN sellers s
-- ON o.seller_id = s.seller_id




-- RIGHT JOIN

SELECT 
o.order_id, o.product, o.city AS customer_city,
s.seller_name
FROM orders o
RIGHT JOIN sellers s
ON o.seller_id = s.seller_id