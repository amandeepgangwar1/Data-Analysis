CREATE TABLE worker (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(150) UNIQUE,
    name VARCHAR(100) NOT NULL
);


INSERT INTO worker (email, name)
VALUES ('amit@company.com', 'Amit Sharma'),
	   ('subham@company.com', 'Subham Sharma'),
       ('ritu@company.com', 'Ritu Sharma');
       
SELECT * FROM worker;