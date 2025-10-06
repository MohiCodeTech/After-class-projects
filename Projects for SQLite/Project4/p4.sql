CREATE TABLE IF NOT EXISTS Student_records (
    NAME TEXT,
    AGE INTEGER,
    STUDENT_ID TEXT,
    GRADE TEXT,
    AVERAGE_MARKS REAL
);

INSERT INTO Student_records(NAME, AGE, STUDENT_ID, GRADE, AVERAGE_MARKS) VALUES
    ('John Mclarkey', 13, '5414', '8', 56.41),
    ('Moheathraam Uthayan', 14, '4210', '9', 80.49),
    ('Dexter Harris', 12, '3901', '7', 91.09),
    ('Jerris Danes', 13, '5910', '8', 40.59),
    ('Newan Methnauka', 15, '2091', '10', 61.97),
    ('Angelina Luke', 11, '4508', '6', 78.45),
    ('Moe Nick', 14, '4101', '9', 84.19);

SELECT GRADE, COUNT(*) AS 'No. of students in the grade'
FROM Student_records
GROUP BY GRADE
HAVING COUNT(*) > 1;

SELECT NAME AS 'Names in ascending order of average marks'
FROM Student_records
ORDER BY AVERAGE_MARKS;

SELECT NAME AS 'Names starting with the letter M'
FROM Student_records
WHERE NAME LIKE 'M%';

SELECT NAME AS 'Names in descending order of age'
FROM Student_records
ORDER BY AGE DESC;