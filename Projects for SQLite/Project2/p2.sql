CREATE TABLE IF NOT EXISTS Gamer(
      USERNAME TEXT PRIMARY KEY,
      ID TEXT,
      HOURS_PLAYED TEXT,
      MONEY_SPENT REAL
);

INSERT INTO Gamer(USERNAME, ID, HOURS_PLAYED, MONEY_SPENT) VALUES
      ('Wowzers', '45', '3', 20.00),
      ('Junkoosters', '78', '2', 10.00),
      ('Exquisteors', '51', '5', 12.32),
      ('Grinders', '90' , '4', 10.00),
      ('Polisters', '87', '1', 5.23);

SELECT * FROM Gamer;
SELECT * FROM Gamer WHERE ID = '90' AND HOURS_PLAYED = '4'; 

SELECT USERNAME, MONEY_SPENT
     FROM Gamer
     WHERE MONEY_SPENT = 
      (SELECT MIN(MONEY_SPENT) FROM Gamer);

SELECT USERNAME, MONEY_SPENT
     FROM Gamer
     WHERE MONEY_SPENT = 
      (SELECT MAX(MONEY_SPENT) FROM Gamer);