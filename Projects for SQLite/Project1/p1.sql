CREATE TABLE IF NOT EXISTS School(
   CLASSROOM TEXT PRIMARY KEY,
   STUDENT TEXT,
   STUDENT_ID TEXT,
   STUDENT_FEE INTEGER
);

INSERT INTO School(CLASSROOM, STUDENT, STUDENT_ID, STUDENT_FEE) VALUES
      ('5B', 'John Smark', '5831', 2000),
      ('7A', 'Williams Creak', '5412', 2090),
      ('1C', 'Mark Robs', '1578', 999),
      ('8M', 'Christopher Silver', '4313', 1943),
      ('9N', 'Howler', '1221', 2432);

SELECT * FROM School