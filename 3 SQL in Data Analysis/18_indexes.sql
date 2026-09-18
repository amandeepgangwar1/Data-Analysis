USE ecom;

DROP TABLE IF EXISTS purchase_orders;

CREATE TABLE purchase_orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price_per_unit DECIMAL(10,2),
    discount_percent INT,
    order_date DATE,
    delivery_date DATE,
    payment_mode VARCHAR(30),
    order_status VARCHAR(30),
    rating INT
);

-- Drop procedure if exists
DROP PROCEDURE IF EXISTS insert_bulk_purchase_orders;

DELIMITER $$

CREATE PROCEDURE insert_bulk_purchase_orders()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE ord_date DATE;

    WHILE i <= 10000 DO

        -- Generate order date first
        SET ord_date = DATE_ADD('2025-01-01', INTERVAL FLOOR(RAND()*60) DAY);

        INSERT INTO purchase_orders
        (customer_name, city, product, category, quantity, price_per_unit, discount_percent, order_date, delivery_date, payment_mode, order_status, rating)
        VALUES (
            CONCAT('Customer_', i),

            ELT(FLOOR(1 + (RAND()*8)), 'Delhi','Mumbai','Pune','Chennai','Kolkata','Hyderabad','Surat','Bangalore'),

            ELT(FLOOR(1 + (RAND()*6)), 'Laptop','Phone','Chair','Bottle','Keyboard','Table'),

            ELT(FLOOR(1 + (RAND()*5)), 'Electronics','Furniture','Kitchen','Fitness','Stationery'),

            FLOOR(1 + (RAND()*5)),

            FLOOR(500 + (RAND()*50000)),

            FLOOR(RAND()*30),

            ord_date,

            -- Delivery date ALWAYS after order date ✅
            DATE_ADD(ord_date, INTERVAL FLOOR(1 + (RAND()*10)) DAY),

            ELT(FLOOR(1 + (RAND()*4)), 'UPI','Cash','Credit Card','Debit Card'),

            ELT(FLOOR(1 + (RAND()*3)), 'Delivered','Pending','Cancelled'),

            FLOOR(1 + (RAND()*5))
        );

        SET i = i + 1;

    END WHILE;
END$$

DELIMITER ;

-- Call procedure
CALL insert_bulk_purchase_orders();

----------------------------------------------------
-- CREATE INDEX
----------------------------------------------------

CREATE INDEX idx_orders_city_status
ON purchase_orders (city, order_status);

----------------------------------------------------
-- TEST QUERY
----------------------------------------------------

SELECT * 
FROM purchase_orders 
WHERE city = 'Delhi' AND order_status = 'Delivered';



SELECT COUNT(*) AS total_rows 
FROM purchase_orders;