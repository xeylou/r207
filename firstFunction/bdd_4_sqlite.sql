-- SQL pour les tables Fournisseur, Produit et Stock

BEGIN TRANSACTION;



DROP TABLE IF EXISTS etudiant;

CREATE TABLE etudiant
  (idEtud	INTEGER	PRIMARY KEY,
   nomEtud	TEXT		NOT NULL
  );

INSERT INTO etudiant VALUES(1,'Alice');
INSERT INTO etudiant VALUES(2,'Bob');
INSERT INTO etudiant VALUES(4,'Charlie');
INSERT INTO etudiant VALUES(5,'David');
INSERT INTO etudiant VALUES(6,'Elsa');
INSERT INTO etudiant VALUES(7,'Frank');
INSERT INTO etudiant VALUES(8,'Gary');
INSERT INTO etudiant VALUES(9,'Henry');
INSERT INTO etudiant VALUES(10,'Indiana');
INSERT INTO etudiant VALUES(11,'Joe');
INSERT INTO etudiant VALUES(12,'Kylie');
INSERT INTO etudiant VALUES(13,'Luke');
INSERT INTO etudiant VALUES(14,'Mike');



DROP TABLE IF EXISTS cours;

CREATE TABLE cours
  (idCours	INTEGER	PRIMARY KEY,
   nomCours	TEXT		NOT NULL
  );

INSERT INTO cours VALUES(1,'informatique');
INSERT INTO cours VALUES(2,'mathématiques');
INSERT INTO cours VALUES(3,'réseaux');
INSERT INTO cours VALUES(4,'anglais');



DROP TABLE IF EXISTS absence;

CREATE TABLE absence
  (idCours	INTEGER	NOT NULL,
   idEtud	INTEGER	NOT NULL,
   dateAbsence	TEXT		NOT NULL,
   PRIMARY KEY (idCours,idEtud,dateAbsence)
  );

INSERT INTO absence VALUES(1,2,'2022-02-14');
INSERT INTO absence VALUES(1,6,'2022-02-14');
INSERT INTO absence VALUES(1,10,'2022-02-14');
INSERT INTO absence VALUES(2,2,'2022-02-16');
INSERT INTO absence VALUES(2,13,'2022-02-16');
INSERT INTO absence VALUES(2,8,'2022-02-14');
INSERT INTO absence VALUES(2,5,'2022-02-18');
INSERT INTO absence VALUES(4,2,'2022-02-17');
INSERT INTO absence VALUES(4,7,'2022-02-17');
INSERT INTO absence VALUES(4,12,'2022-02-17');
INSERT INTO absence VALUES(4,6,'2022-02-14');
INSERT INTO absence VALUES(4,11,'2022-02-17');
INSERT INTO absence VALUES(3,2,'2022-02-15');
INSERT INTO absence VALUES(3,6,'2022-02-15');



COMMIT;

