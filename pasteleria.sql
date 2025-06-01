-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: pasteleriasolyluna
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `idCategorias` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` text,
  PRIMARY KEY (`idCategorias`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (34,'Pasteles','Productos horneados grandes, ideales para celebraciones.'),(35,'Repostería Individual','Porciones pequeñas como cupcakes, brownies o mini pays.'),(36,'Bebidas','Jugos, aguas frescas o bebidas embotelladas.'),(37,'Gelatinas y Flanes','Postres fríos como flanes, gelatinas decoradas o napolitanas.');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idClientes` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idClientes`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (14,'Daniela Lopez','9611112012','danilop@gamil.com'),(15,'Jhoana Rincon','9611110202','jhovisr@gmail.com'),(16,'Carlos Gomez','9611110203','carlosgmz@gmail.com'),(17,'Timothy Dominguez','9611110204','timdom@gmail.com'),(19,'Elizabeth Granados','9615854251','elig@gmail.com');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalleventa`
--

DROP TABLE IF EXISTS `detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalleventa` (
  `idDetalleVenta` int NOT NULL AUTO_INCREMENT,
  `idProductos` int DEFAULT NULL,
  `idVentas` int DEFAULT NULL,
  `cantidad` int NOT NULL,
  `precioUnitario` decimal(10,2) NOT NULL,
  PRIMARY KEY (`idDetalleVenta`),
  KEY `idProductos` (`idProductos`),
  KEY `idVentas` (`idVentas`),
  CONSTRAINT `detalleventa_ibfk_1` FOREIGN KEY (`idProductos`) REFERENCES `productos` (`idProductos`),
  CONSTRAINT `detalleventa_ibfk_2` FOREIGN KEY (`idVentas`) REFERENCES `ventas` (`idVentas`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalleventa`
--

LOCK TABLES `detalleventa` WRITE;
/*!40000 ALTER TABLE `detalleventa` DISABLE KEYS */;
INSERT INTO `detalleventa` VALUES (1,9,2,1,110.00),(2,7,3,1,18.00),(3,7,3,1,18.00),(4,1,3,1,120.00),(5,8,3,1,150.00),(6,3,4,5,35.00),(7,11,4,1,30.00),(8,9,8,3,110.00),(9,7,8,3,150.00),(10,8,9,4,150.00),(11,10,13,1,45.00),(12,12,14,1,140.00),(13,20,15,2,35.00),(14,20,15,4,35.00),(15,8,16,1,150.00);
/*!40000 ALTER TABLE `detalleventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `idEmpleados` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `puesto` varchar(45) DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `usuario` varchar(45) DEFAULT NULL,
  `contrasena` varchar(45) DEFAULT NULL,
  `idSucursales` int DEFAULT NULL,
  PRIMARY KEY (`idEmpleados`),
  UNIQUE KEY `usuario` (`usuario`),
  KEY `idSucursales` (`idSucursales`),
  CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`idSucursales`) REFERENCES `sucursales` (`idSucursales`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (1,'Angy Cruz','Cajera',10000.00,'9611111225','AngyC','123456',NULL),(2,'Mariana Torres','Cajera',1500.00,'9612345678','marianat','cajera123',NULL),(3,'Andrés López','Repostero',9500.00,'9623456789','andresl','pastelero456',NULL),(4,'Celeste Rivas','Administradora',11000.00,'9634567890','celester','admin789',NULL),(5,'Scarlet Constantino','Pastelera',15000.00,'9612558152','ScarletC','123456',NULL);
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos`
--

DROP TABLE IF EXISTS `pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagos` (
  `idPagos` int NOT NULL AUTO_INCREMENT,
  `montoPago` decimal(10,2) NOT NULL,
  `fechaPago` datetime NOT NULL,
  `metodoPago` varchar(45) DEFAULT NULL,
  `idVentas` int DEFAULT NULL,
  PRIMARY KEY (`idPagos`),
  KEY `idVentas` (`idVentas`),
  CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`idVentas`) REFERENCES `ventas` (`idVentas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos`
--

LOCK TABLES `pagos` WRITE;
/*!40000 ALTER TABLE `pagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `idProductos` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` text,
  `precio` decimal(10,2) NOT NULL,
  `stock` int NOT NULL,
  `fechaVencimiento` date DEFAULT NULL,
  `unidadMedida` varchar(45) DEFAULT NULL,
  `idCategorias` int DEFAULT NULL,
  `idProveedores` int DEFAULT NULL,
  `idUnidades` int DEFAULT NULL,
  `codigoBarras` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idProductos`),
  KEY `idCategorias` (`idCategorias`),
  KEY `idProveedores` (`idProveedores`),
  KEY `idUnidades` (`idUnidades`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`idCategorias`) REFERENCES `categorias` (`idCategorias`),
  CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`idProveedores`) REFERENCES `proveedores` (`idProveedores`),
  CONSTRAINT `productos_ibfk_3` FOREIGN KEY (`idUnidades`) REFERENCES `unidades` (`idUnidades`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Pastel de Fresa',NULL,120.00,10,NULL,NULL,NULL,NULL,NULL,'7501001111222'),(2,'Flan Napolitano',NULL,90.00,20,NULL,NULL,NULL,NULL,NULL,'7501001111333'),(3,'Cupcake Vainilla',NULL,35.00,30,NULL,NULL,NULL,NULL,NULL,'7501001111444'),(5,'Pastel de Chocolate',NULL,130.00,12,NULL,NULL,NULL,NULL,NULL,'7501001111555'),(6,'Brownie de Chocolate',NULL,25.00,50,NULL,NULL,NULL,NULL,NULL,'7501001111555'),(7,'Galletas de Avena',NULL,18.00,60,NULL,NULL,NULL,NULL,NULL,'7501001111666'),(8,'Cheesecake de Zarzamora',NULL,150.00,15,NULL,NULL,NULL,NULL,NULL,'7501001111777'),(9,'Chocoflan',NULL,110.00,20,NULL,NULL,NULL,NULL,NULL,'7501001111888'),(10,'Panqué de Limón',NULL,45.00,35,NULL,NULL,NULL,NULL,NULL,'7501001111999'),(11,'Mini Donas Glaseadas',NULL,30.00,40,NULL,NULL,NULL,NULL,NULL,'7501001112000'),(12,'Pastel Tres Leches',NULL,140.00,12,NULL,NULL,NULL,NULL,NULL,'7501001112111'),(13,'Empanada de Piña',NULL,20.00,45,NULL,NULL,NULL,NULL,NULL,'7501001112222'),(14,'Bollito de Vainilla',NULL,22.00,55,NULL,NULL,NULL,NULL,NULL,'7501001112333'),(15,'Muffin de Plátano',NULL,28.00,38,NULL,NULL,NULL,NULL,NULL,'7501001112444'),(16,'Gelatina de fresa 125g',NULL,12.00,50,NULL,NULL,NULL,NULL,NULL,'7501005001001'),(17,'Flan napolitano 140g',NULL,15.00,40,NULL,NULL,NULL,NULL,NULL,'7501005001002'),(18,'Refresco Cola 600ml',NULL,18.00,60,NULL,NULL,NULL,NULL,NULL,'7501005001003'),(19,'Agua mineral natural 1L',NULL,14.00,70,NULL,NULL,NULL,NULL,NULL,'7501005001004'),(20,'Gelatina surtida 6 pack',NULL,35.00,30,NULL,NULL,NULL,NULL,NULL,'7501005001005'),(21,'Gelatina Limón 250g',NULL,20.00,30,NULL,NULL,NULL,NULL,NULL,'7501000000013');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `idProveedores` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `correoElectronico` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idProveedores`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (26,'Hanna Montes','96111106','Col 23 de Mayo Calle Misol-Ha Num98','hannamon@gmail.com'),(27,'Mia Estrada','96111108','Col Paraiso II  Calle Rio Cantela Num14','miaestrada@gmail.com'),(28,'Eugenio Molina','96111109','Col Albania Alta  Calle Rio Las Palmas Num71','eugeniomol@gmail.com'),(29,'Cristel Barrientos','9615467598','Avenida Central Poniente 123, Colonia Centro','crisb@gmail.com');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sucursales`
--

DROP TABLE IF EXISTS `sucursales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sucursales` (
  `idSucursales` int NOT NULL AUTO_INCREMENT,
  `nombreSucursal` varchar(100) DEFAULT 'Sucursal Default',
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `correoElectronico` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idSucursales`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sucursales`
--

LOCK TABLES `sucursales` WRITE;
/*!40000 ALTER TABLE `sucursales` DISABLE KEYS */;
INSERT INTO `sucursales` VALUES (4,'Sucursal Default','Av. Central Norte #1025, Tuxtla Gutiérrez, Chiapas','9611234567','central@pasteleriasolyluna.com'),(5,'Sucursal Default','Calle 20 Poniente #45, Colonia Las Granjas, Tuxtla Gutiérrez, Chiapas','9617654321','granjas@pasteleriasolyluna.com'),(6,'Sucursal Default','Boulevard Belisario Domínguez #800, Plaza Crystal, Tuxtla Gutiérrez, Chiapas','9618880001','plazacrystal@pasteleriasolyluna.com'),(7,'Sucursal Default','1a Oriente Norte #350, Centro, San Cristóbal de las Casas, Chiapas','9671010101','sclc@pasteleriasolyluna.com'),(8,'Sucursal Default','Carretera Internacional Km 5, Tapachula, Chiapas','9622223333','tapachula@pasteleriasolyluna.com');
/*!40000 ALTER TABLE `sucursales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidades`
--

DROP TABLE IF EXISTS `unidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidades` (
  `idUnidades` int NOT NULL AUTO_INCREMENT,
  `nombreUnidad` varchar(45) NOT NULL,
  PRIMARY KEY (`idUnidades`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidades`
--

LOCK TABLES `unidades` WRITE;
/*!40000 ALTER TABLE `unidades` DISABLE KEYS */;
INSERT INTO `unidades` VALUES (16,'Rebanada'),(17,'Pieza'),(18,'Caja'),(19,'Docena'),(20,'Media docena'),(21,'Kilogramo');
/*!40000 ALTER TABLE `unidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `idVentas` int NOT NULL AUTO_INCREMENT,
  `fechaVenta` date NOT NULL,
  `montoTotal` decimal(10,2) NOT NULL,
  `metodoPago` varchar(45) DEFAULT NULL,
  `idClientes` int DEFAULT NULL,
  `idEmpleados` int DEFAULT NULL,
  PRIMARY KEY (`idVentas`),
  KEY `idClientes` (`idClientes`),
  KEY `idEmpleados` (`idEmpleados`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`idClientes`) REFERENCES `clientes` (`idClientes`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`idEmpleados`) REFERENCES `empleados` (`idEmpleados`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (2,'2025-05-28',110.00,'Tarjeta',15,1),(3,'2025-05-29',306.00,'Efectivo',16,3),(4,'2025-05-31',205.00,'Tarjeta',15,3),(8,'2025-05-31',330.00,'Tarjeta',15,2),(9,'2025-05-31',600.00,'Tarjeta',15,3),(13,'2025-05-31',45.00,'Efectivo',16,3),(14,'2025-05-31',140.00,'Tarjeta',17,3),(15,'2025-05-31',70.00,'Transferencia',15,2),(16,'2025-05-31',150.00,'Tarjeta',14,3);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-01  0:05:59
