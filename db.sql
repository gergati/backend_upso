CREATE DATABASE IF NOT EXISTS NicoAdministraciones;
USE NicoAdministraciones;
-- Crear la tabla Usuario
CREATE TABLE Usuario (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    dni INT(8) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefono INT(12) NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) -- Monotributista o Responsable Inscripto
);

INSERT INTO Usuario VALUES
(1,'German', 'Gatica', 38563735, 'german@gmail.com',2915051269, 'password1212', 'Responsable Inscripto'),
(2,'Carlos','Berger', 20765432,'berger@gmail.com', 291345678,'password1212', 'D'),
(3,'Pablo', 'Granados', 32560216, 'pablo@gmail.com',2915051269, 'password1212', 'B');

-- Crear la tabla Cliente
CREATE TABLE Cliente (
    cliente_id INT NOT NULL AUTO_INCREMENT,
    usuario_id INT,
    apellido VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    dni INT(8) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefono INT(12) NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    fechaNac DATE NOT NULL,
    PRIMARY KEY (cliente_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id)
);

INSERT INTO Cliente VALUES 
(1,1,'Perez','Joaquin',34567564,'perez@gmail.com',2915107678, 'perez123','1969-02-09'),
(2,2,'Solis','Eduardo',12327523,'solis@gmail.com',2915107678,'solis123','1972-11-03'),
(3,1,'Nieto','Jorge',34234809,'nieto@gmail.com',2915107678,'nieto123','1972-10-04'),
(4,2,'Hernandez','Johanna', 34234809,'hernandez@gmail.com',2915107678,'hernandez123','1952-04-03'),
(5,1,'Romero','Manuel Alberto',34567342,'romero@gmail.com',2915107678,'romero123','1969-12-04'),
(6,2,'Garcia','Roxana',34345564,'garcia@gmail.com',2915107678,'garcia123','1970-04-04'),
(7,1,'Castro','Alfredo',34565674,'castro@gmail.com',2915107678,'castro123','1980-09-02'),
(8,2,'Peña','Verenice',34567589,'peña@gmail.com',2915107678,'peña123','1978-03-17'),
(9,1,'Martinez','Evelyn',34556764,'martinez@gmail.com',2915107678,'martinez123','1972-08-14'),
(10,2,'Siguenza','Eduardo',21467564,'siguenza@gmail.com',2915107678,'siguenza123','1975-10-09'),
(11,1,'Duran','Martin',34562364,'duran@gmail.com',2915107678,'duran123','1972-03-04'),
(12,2,'Perez','Jose',34563352,'perez@gmail.com',2915107678,'perez123','1972-06-03'),
(13,1,'Marillan','Sandra',67557564,'marillan@gmail.com',2915107678,'marillan123','1968-04-03'),
(14,2,'Cuestas','Maria',34567564,'cuestas@gmail.com',2915107678,'cuestas123','1972-09-14');


-- Crear la tabla Producto
CREATE TABLE Producto (
    producto_id INT AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    nombreProd VARCHAR(255) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad INT(10) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    PRIMARY KEY (producto_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id)
);
INSERT INTO Producto VALUES 
(1, 1, 'Heladera','Drean', 571.699,1,'ciclica 314L GRIS ALUM'),
(2, 2, 'Notebook','Acer',998.090,1,'Nitro 5-AN515-57-52NY 15.6"8/256Gb Ssd'),
(3, 1, 'Lavarropas','Drean',543.199,1,'Next 7.10 ECO Carga Frontal 7KG'),
(4, 2, 'Televisor', 'LG',793.499,1,'70 UQ8050 4k BT hdr usb'),
(5, 1, 'Cafetera', 'Nespresso',129.709,1,'Essenza Mini Black C30-Ar-Bk-Ne'),
(6, 2, 'Televisor','Philips', 390.999,1,'Smart Tv A.V. 55 Pud7406/77 4K Hdr Usb Hdmi'),
(7, 1, 'Aire Acondicionado', 'Hisense', 689.999,1,'Split 3300W F/C"A++" Inver.'),
(8, 2, 'Celular','Motorola', 138.699,1,'Moto G72 Azul Niagara 6/128Gb 6.55"'),
(9, 1, 'Lavarropas','Enova',346.399,1,'6kg Ewmf-6 Blanco "A"'),
(10, 2, 'Estufa Eléctrica','Liliana',10.637,1,'CV026 Vertical 2Velas 1200W'),
(11, 1, 'Conjunto Sommier', 'King Koil',385.997,1,'XL 140x190');

CREATE TABLE FacturaProducto (
    facturaProd_id INT NOT NULL AUTO_INCREMENT,
    producto_id INT NOT NULL,
    usuario_id INT NOT NULL,
    PRIMARY KEY (facturaProd_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (producto_id) REFERENCES Producto(producto_id)
);

INSERT INTO FacturaProducto VALUES
(1,4,1),
(2,2,2),
(3,6,1);


-- Crear la tabla Servicio
CREATE TABLE Servicio (
    servicio_id INT NOT NULL AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    cliente_id INT NOT NULL,
    nombreServicio VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    PRIMARY KEY (servicio_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);
INSERT INTO Servicio VALUES
(1,3,'Pintura total de la casa', '2022-11-29', '13:25:07',),
(2,3,'Cambio memoria ram 8gb', '2023-10-09', '17:15:07'),
(3,3,'Corte de pasto', '2018-07-22', '10:25:07'),
(4,3,'Limpieza de pileta', '2023-04-12', '09:00:00');


CREATE TABLE FacturaServicio (
    facturaServicio_id INT NOT NULL AUTO_INCREMENT,
    servicio_id INT NOT NULL,
    PRIMARY KEY (facturaServicio_id),
    FOREIGN KEY (servicio_id) REFERENCES Servicio(servicio_id)
);

INSERT INTO FacturaServicio VALUES
(1,1);