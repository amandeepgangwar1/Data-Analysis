-- CREATE TABLE employees(
-- emp_id INT PRIMARY KEY AUTO_INCREMENT,
-- email VARCHAR(150) UNIQUE,
-- name VARCHAR(100) NOT NULL
-- );

-- INSERT INTO employees (email, name)
-- VALUES ('amit@gmail.com', 'Amit Kumar'),
-- -- ('amit@gmail.com', 'Amit Kumar'),
-- -- ('samit@gmail.com', NULL),                       Not possible
-- ('amita@gmail.com', 'Amit Kumar');


CREATE TABLE employee (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(150) UNIQUE,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18),
    department VARCHAR(50) DEFAULT 'General',
    salary DECIMAL(10,2) CHECK (salary > 0),
    joining_date DATE DEFAULT (CURRENT_DATE)
);

INSERT INTO employee (email, name, age, salary)
-- VALUES ('rahul@company.com', 'Rahul Khan', 16, 30000); -- DOESNOT RUN BECAUSE AGE IS LESS THAN 18.... 
VALUES ('rahul@company.com', 'Rahul Khan', 26, 30000),
       ('pooja@company.com', 'Pooja Nair', 16, 50000);    -- NOT RUN... 

SELECT * FROM employee;

ALTER TABLE employee
ADD CONSTRAINT age_unique UNIQUE(age);

INSERT INTO employee (email, name, age, salary)
VALUES ('rahul1@company.com', 'Rahuls Khan', 26, 30000);