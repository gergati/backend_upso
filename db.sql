CREATE DATABASE IF NOT EXISTS AdminTotal;
USE AdminTotal;
-- Crear la tabla Usuario
CREATE TABLE Usuario (
    usuario_id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    dni INT(8) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefono INT(12) NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) -- Persona o Empresa
);

INSERT INTO Usuario VALUES
(1,'German', 'Gatica', 38563735, 'german@gmail.com',2915051269, 'password1212', 'Megatone'),
(2,'Carlos','Berger', 20765432,'berger@gmail.com', 291345678,'password1212', 'Lucaioli');


-- Crear la tabla Cliente
CREATE TABLE Cliente (
    cliente_id INT PRIMARY KEY,
    usuario_id INT,
    apellido VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    dni INT(8) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefono INT(12) NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    fechaNac DATETIME NOT NULL,
    PRIMARY KEY (cliente_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id)
);

INSERT INTO Cliente VALUES 
(1,1,'Perez','Joaquin',34567564,'perez@gmail.com',2915107678, 'perez123','2/9/1969'),
(2,2,'Solis','Eduardo',12327523,'solis@gmail.com',2915107678,'solis123','1972/11/03' ),
(3,1,'Nieto','Jorge',34234809,'nieto@gmail.com',2915107678,'nieto123','1972/10/04'),
(4,2,'Hernandez','Johanna', 34234809,'hernandez@gmail.com',2915107678,'hernandez123','1952/04/03',),
(5,1,'Romero','Manuel Alberto',34567342,'romero@gmail.com',2915107678,'romero123','1969/12/04'),
(6,2,'Garcia','Roxana',34345564,'garcia@gmail.com',2915107678,'garcia123','1970/04/04'),
(7,1,'Castro','Alfredo',34565674,'castro@gmail.com',2915107678,'castro123','1980/09/02'),
(8,2,'Peña','Verenice',34567589,'peña@gmail.com',2915107678,'peña123','1978/03/17'),
(9,1,'Martinez','Evelyn',34556764,'martinez@gmail.com',2915107678,'martinez123','1972/08/14'),
(10,2,'Siguenza','Eduardo',21467564,'siguenza@gmail.com',2915107678,'siguenza123','1975/10/09'),
(11,1,'Duran','Martin',34562364,'duran@gmail.com',2915107678,'duran123','1972/03/04'),
(12,2,'Perez','Jose',34563352,'perez@gmail.com',2915107678,'perez123','1972/06/03'),
(13,1,'Marillan','Sandra',67557564,'marillan@gmail.com',2915107678,'marillan123','1968/04/03'),
(14,2,'Cuestas','Maria',34567564,'cuestas@gmail.com',2915107678,'cuestas123','1972/09/14');


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
(1, 1, 'Heladera','Drean', 571.699,1,'HELADERA CICLICA DREAN 314L GRIS ALUM'),
(2, 2, 'Notebook','Acer',998.090,1,'Notebook Acer Nitro 5-AN515-57-52NY 15.6"8/256Gb Ssd'),
(3, 1, 'Lavarropas','Drean',543.199,1,'Lavarropas Drean Next 7.10 ECO Carga Frontal 7KG'),
(4, 2, 'Televisor', 'LG',793.499,1,'Smart Tv LG 70 UQ8050 4k BT hdr usb'),
(5, 1, 'Cafetera', 'Nespresso',129.709,1,'Cafetera Nespresso Cafetera Essenza Mini Black C30-Ar-Bk-Ne'),
(6, 2, 'Televisor','Philips', 390.999,1,'Smart Tv Philips A.V. 55 Pud7406/77 4K Hdr Usb Hdmi'),
(7, 1, 'Aire Acondicionado', 'Hisense',1, 689.999,'Aire Acondicionado Hisense Split 3300W F/C"A++" Inver.');

-- Crear la tabla Servicio
CREATE TABLE Servicio (
    servicio_id INT AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    nombreServicio VARCHAR(255) NOT NULL,
    PRIMARY KEY (servicio_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id)
);
INSERT INTO Servicio VALUES
(1,1,'Venta de artefactos electronicos'),
(2,2,'Ventas de materia prima');

-- Crear la tabla Factura
CREATE TABLE Factura (
    factura_id INT AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    cliente_id INT NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (factura_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);
INSERT INTO Factura VALUES
(1, 1, 1, '22/11/2023', 800.000),
(2, 2, 4, '18/10/2023', 650.000),
(3, 1, 6, '02/09/2023', 200.000),
(4, 2, 10, '01/01/2023', 190.000),
(5, 1, 8, '29/04/2023', 200.000);

-- Para manejar la relación entre Factura y Producto/Servicio, podrías crear tablas intermedias (si es una relación muchos a muchos)
-- o simplemente agregar claves foráneas a las tablas Producto y Servicio si es una relación uno a muchos.

-- Ejemplo de tabla intermedia para relación muchos a muchos entre Factura y Producto
CREATE TABLE FacturaProducto (
    factura_id INT NOT NULL AUTO_INCREMENT,
    producto_id INT NOT NULL,
    cantidad INT(50) NOT NULL,
    PRIMARY KEY (factura_id, producto_id),
    FOREIGN KEY (factura_id) REFERENCES Factura(factura_id),
    FOREIGN KEY (producto_id) REFERENCES Producto(producto_id)
);

INSERT INTO FacturaProducto VALUES
(1,4,1);

-- Ejemplo de tabla intermedia para relación muchos a muchos entre Factura y Servicio
CREATE TABLE FacturaServicio (
    facturaServicio_id INT NOT NULL AUTO_INCREMENT,
    servicio_id INT NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY (facturaServicio_id, servicio_id),
    FOREIGN KEY (facturaServicio_id) REFERENCES Factura(factura_id),
    FOREIGN KEY (servicio_id) REFERENCES Servicio(servicio_id)
);

INSERT INTO FacturaServicio VALUES
(1,2,1);

