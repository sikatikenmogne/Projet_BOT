CREATE TABLE Utilisateur (
    IdentifiantUtilisateur INT PRIMARY KEY AUTO_INCREMENT,
    Nom VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    MotDePasse VARCHAR(100) NOT NULL
);

CREATE TABLE Produit (
    IdentifiantProduit INT PRIMARY KEY AUTO_INCREMENT,
    Nom VARCHAR(100) NOT NULL,
    Description TEXT,
    Prix FLOAT NOT NULL,
    Categorie VARCHAR(50),
    Disponibilite BOOLEAN NOT NULL
);

CREATE TABLE Commande (
    IdentifiantCommande INT PRIMARY KEY AUTO_INCREMENT,
    IdentifiantUtilisateur INT,
    DateCommande DATETIME NOT NULL,
    StatutCommande VARCHAR(50),
    FOREIGN KEY (IdentifiantUtilisateur) REFERENCES Utilisateur(IdentifiantUtilisateur)
);


CREATE TABLE LigneCommande (
    IdentifiantLigneCommande INT PRIMARY KEY AUTO_INCREMENT,
    IdentifiantCommande INT,
    IdentifiantProduit INT,
    Quantite INT NOT NULL,
    FOREIGN KEY (IdentifiantCommande) REFERENCES Commande(IdentifiantCommande),
    FOREIGN KEY (IdentifiantProduit) REFERENCES Produit(IdentifiantProduit)
);

CREATE TABLE Reservation (
    IdentifiantReservation INT PRIMARY KEY AUTO_INCREMENT,
    IdentifiantUtilisateur INT,
    DateReservation DATE NOT NULL,
    HeureReservation TIME NOT NULL,
    NombrePersonnes INT NOT NULL,
    StatutReservation VARCHAR(50),
    FOREIGN KEY (IdentifiantUtilisateur) REFERENCES Utilisateur(IdentifiantUtilisateur)
);
