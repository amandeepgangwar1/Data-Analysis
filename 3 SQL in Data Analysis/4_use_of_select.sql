-- SELECT * FROM orders WHERE discount_percent < 20;

-- SELECT * FROM orders WHERE delivery_date = NULL;   ====>>>> -- use IS NULL in place of ( = NULL ) given below:-
-- SELECT * FROM orders WHERE delivery_date IS NULL;

-- SELECT customer_name, city, quantity FROM orders WHERE discount_percent < 20;

-- SELECT * FROM orders WHERE city = 'Delhi' AND order_status = 'Delivered';

SELECT * FROM orders WHERE city = 'Delhi' OR order_status = 'Delivered';