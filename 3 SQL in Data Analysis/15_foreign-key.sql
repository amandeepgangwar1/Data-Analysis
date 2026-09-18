CREATE TABLE sellers (
    seller_id INT PRIMARY KEY AUTO_INCREMENT,
    seller_name VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(50)
);
INSERT INTO sellers (seller_name, city)
VALUES ('TechWorld', 'Delhi'),
	   ('TechWorld2', 'Banglore');

SELECT * FROM sellers;



ALTER TABLE orders
ADD COLUMN seller_id INT;
SELECT * FROM orders;

INSERT INTO orders (seller_id, product, quantity, price_per_unit)
VALUES (2, 'Lamp', 13, 5000);
SELECT * FROM orders;



ALTER TABLE orders
ADD CONSTRAINT fk_orders_seller
FOREIGN KEY (seller_id)
REFERENCES sellers(seller_id);
SELECT * FROM orders;