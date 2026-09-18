USE ecom;

DELIMITER //            
 -- To change the symbol which helps to end line...

CREATE PROCEDURE get_delivered_orders()
BEGIN
	SELECT * FROM orders
    WHERE order_status = 'Delivered';
    SELECT * FROM employees;
END //

DELIMITER ;


CALL get_delivered_orders();


DELIMITER //

CREATE PROCEDURE get_ordered_by_city(IN city_name VARCHAR(50))
BEGIN
	SELECT * FROM orders
    WHERE city = city_name;
END //
DELIMITER ;

CALL get_ordered_by_city('Delhi');

CALL get_ordered_by_city('Mumbai');