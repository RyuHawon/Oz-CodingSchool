CREATE DATABASE PetHotel;
USE PetHotel;

CREATE TABLE PetOwners (
	ownerID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    contact VARCHAR(30) NOT NULL
);

CREATE TABLE Pets(
	petID INT AUTO_INCREMENT PRIMARY KEY,
    ownerID INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    species VARCHAR(255),
    breed VARCHAR(255),
    FOREIGN KEY (ownerID) REFERENCES PetOwners(ownerID)
);

CREATE TABLE Rooms(
	roomID INT AUTO_INCREMENT PRIMARY KEY,
    roomNumber INT NOT NULL,
    roomType ENUM('Standard', 'Deluxe', 'Suite'),
    pricePerNight DECIMAL(15, 2) NOT NULL
);

CREATE TABLE Reservations(
	reservationID INT AUTO_INCREMENT PRIMARY KEY,
    petID INT NOT NULL,
    roomID INT NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    FOREIGN KEY (petID) REFERENCES Pets(petID),
    FOREIGN KEY (roomID) REFERENCES Rooms(roomID)
);

CREATE TABLE Services(
	serviceID INT AUTO_INCREMENT PRIMARY KEY,
    reservationID INT NOT NULL,
    serviceName VARCHAR(255) NOT NULL,
    servicePrice DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (reservationID) REFERENCES Reservations(reservationID)
);







