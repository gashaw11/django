-- Create a table
CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Grade CHAR(1)
);

-- Insert data into the table
INSERT INTO Students (ID, Name, Age, Grade) 
VALUES 
(1, 'Alice', 20, 'A'),
(2, 'Bob', 22, 'B'),
(3, 'Charlie', 21, 'C');

-- Retrieve all records
SELECT * FROM Students;
