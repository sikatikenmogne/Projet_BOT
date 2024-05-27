DELIMITER //

CREATE PROCEDURE AddProduit(
    IN pNom VARCHAR(100),
    IN pDescription TEXT,
    IN pPrix FLOAT,
    IN pCategorie VARCHAR(50),
    IN pDisponibilite BOOLEAN
)
BEGIN
    INSERT INTO Produit (Nom, Description, Prix, Categorie, Disponibilite)
    VALUES (pNom, pDescription, pPrix, pCategorie, pDisponibilite);
END //

DELIMITER //

CREATE PROCEDURE AddReservation(
    IN pUtilisateurId INT,
    IN pDateReservation DATE,
    IN pHeureReservation TIME,
    IN pNombrePersonnes INT,
    IN pStatutReservation VARCHAR(50)
)
BEGIN
    INSERT INTO Reservation (IdentifiantUtilisateur, DateReservation, HeureReservation, NombrePersonnes, StatutReservation)
    VALUES (pUtilisateurId, pDateReservation, pHeureReservation, pNombrePersonnes, pStatutReservation);
END //


DELIMITER //

CREATE PROCEDURE AddCommande(
    IN pUtilisateurId INT,
    IN pDateCommande DATETIME,
    IN pStatutCommande VARCHAR(50)
)
BEGIN
    INSERT INTO Commande (IdentifiantUtilisateur, DateCommande, StatutCommande)
    VALUES (pUtilisateurId, pDateCommande, pStatutCommande);
END //


DELIMITER //

CREATE PROCEDURE AddUtilisateur(
    IN pNom VARCHAR(100),
    IN pEmail VARCHAR(100),
    IN pMotDePasse VARCHAR(100)
)
BEGIN
    INSERT INTO Utilisateur (Nom, Email, MotDePasse)
    VALUES (pNom, pEmail, pMotDePasse);
END //

DELIMITER //

CREATE PROCEDURE AddLigneCommande(
    IN pCommandeId INT,
    IN pDatecommande DATE,
    IN pHeurecommande TIME,
    IN pUtilisateurId INT,

)
BEGIN
    INSERT INTO LigneCommande (IdentifiantCommande,datecommande,heurecommande,UtilisateurId )
    VALUES (pCommandeId,pDatecommande,pHeurecommande,pUtilisateurId);
END //