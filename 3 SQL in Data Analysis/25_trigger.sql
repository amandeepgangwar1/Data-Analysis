USE ecom;

-- Step 1: Create cancellation log table
CREATE TABLE IF NOT EXISTS order_cancellations (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    cancelled_on DATETIME,
    reason VARCHAR(100)
);

-- Step 2: Drop trigger if already exists
DROP TRIGGER IF EXISTS trg_log_order_cancel;

-- Step 3: Create trigger
DELIMITER //

CREATE TRIGGER trg_log_order_cancel
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NEW.order_status = 'Cancelled'
       AND OLD.order_status <> 'Cancelled' THEN

        INSERT INTO order_cancellations
        (order_id, cancelled_on, reason)
        VALUES
        (NEW.order_id, NOW(), 'Order cancelled by user');

    END IF;
END //

DELIMITER ;

-- Step 4: Reset order (important for testing)
UPDATE orders
SET order_status = 'Pending'
WHERE order_id = 2;

-- Step 5: Now cancel (trigger will fire)
UPDATE orders
SET order_status = 'Cancelled'
WHERE order_id = 2;

-- Step 6: Check results
SELECT * FROM order_cancellations;
SELECT * FROM orders;