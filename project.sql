CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
);

INSERT INTO Students VALUES (1, 'Aman', 85);
INSERT INTO Students VALUES (2, 'Riya', 90);
INSERT INTO Students VALUES (3, 'Rahul', 78);

SELECT * FROM Students;

SELECT * FROM Students WHERE marks > 80;

SELECT AVG(marks) AS average_marks FROM Students;
