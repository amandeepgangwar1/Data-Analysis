SELECT * FROM order_details WHERE city IN ('Delhi', 'Mumbai', 'Banglore');

SELECT * FROM order_details WHERE city NOT IN ('Delhi', 'Mumbai', 'Banglore');

SELECT * FROM order_details WHERE payment_mode NOT IN ('Cash', 'UPI');




SELECT * FROM order_details WHERE price_per_unit BETWEEN 1000 AND 10000;

SELECT * FROM order_details WHERE price_per_unit NOT BETWEEN 1000 AND 10000;




SELECT * FROM order_details WHERE city LIKE "D%";

SELECT * FROM order_details WHERE city LIKE "%a";

SELECT * FROM order_details WHERE city LIKE "%bad";

SELECT * FROM order_details WHERE city LIKE "%b%";




SELECT * FROM order_details WHERE city LIKE "D_lhi";

SELECT * FROM order_details WHERE customer_name LIKE "Sar_ _li";




SELECT * FROM order_details WHERE category IN ('Electronics', 'Furniture') AND price_per_unit NOT BETWEEN 5000 AND 20000;