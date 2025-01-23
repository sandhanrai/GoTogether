CREATE TABLE Shuttle (
    shuttle_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_number VARCHAR(255) UNIQUE NOT NULL,
    capacity INT NOT NULL
);

CREATE TABLE Schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    route VARCHAR(255) NOT NULL,
    shuttle_id INT,
    time_slot DATETIME NOT NULL,
    FOREIGN KEY (shuttle_id) REFERENCES Shuttle(shuttle_id)
);
