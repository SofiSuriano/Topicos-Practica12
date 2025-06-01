SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `pasteleriasolyluna`;
CREATE SCHEMA IF NOT EXISTS `pasteleriasolyluna` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `pasteleriasolyluna`;

CREATE TABLE IF NOT EXISTS `categorias` (
  `idCategorias` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`idCategorias`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `clientes` (
  `idClientes` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(10) NULL DEFAULT NULL,
  `correo` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idClientes`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `proveedores` (
  `idProveedores` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(10) NULL DEFAULT NULL,
  `direccion` VARCHAR(100) NULL DEFAULT NULL,
  `correoElectronico` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idProveedores`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `unidades` (
  `idUnidades` INT NOT NULL AUTO_INCREMENT,
  `nombreUnidad` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUnidades`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `productos` (
  `idProductos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` TEXT NULL DEFAULT NULL,
  `precio` DECIMAL(10,2) NOT NULL,
  `stock` INT NOT NULL,
  `fechaVencimiento` DATE NULL DEFAULT NULL,
  `unidadMedida` VARCHAR(45) NULL DEFAULT NULL,
  `idCategorias` INT NULL DEFAULT NULL,
  `idProveedores` INT NULL DEFAULT NULL,
  `idUnidades` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idProductos`),
  INDEX `idCategorias` (`idCategorias`),
  INDEX `idProveedores` (`idProveedores`),
  INDEX `idUnidades` (`idUnidades`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`idCategorias`) REFERENCES `categorias` (`idCategorias`),
  CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`idProveedores`) REFERENCES `proveedores` (`idProveedores`),
  CONSTRAINT `productos_ibfk_3` FOREIGN KEY (`idUnidades`) REFERENCES `unidades` (`idUnidades`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `sucursales` (
  `idSucursales` INT NOT NULL AUTO_INCREMENT,
  `nombreSucursal` VARCHAR(100) NULL DEFAULT 'Sucursal Default',
  `direccion` VARCHAR(100) NULL DEFAULT NULL,
  `telefono` VARCHAR(10) NULL DEFAULT NULL,
  `correoElectronico` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idSucursales`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `empleados` (
  `idEmpleados` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `puesto` VARCHAR(45) NULL DEFAULT NULL,
  `salario` DECIMAL(10,2) NULL DEFAULT NULL,
  `telefono` VARCHAR(10) NULL DEFAULT NULL,
  `usuario` VARCHAR(45) NULL DEFAULT NULL,
  `contrasena` VARCHAR(45) NULL DEFAULT NULL,
  `idSucursales` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idEmpleados`),
  UNIQUE INDEX `usuario` (`usuario`),
  INDEX `idSucursales` (`idSucursales`),
  CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`idSucursales`) REFERENCES `sucursales` (`idSucursales`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `ventas` (
  `idVentas` INT NOT NULL AUTO_INCREMENT,
  `fechaVenta` DATE NOT NULL,
  `montoTotal` DECIMAL(10,2) NOT NULL,
  `metodoPago` VARCHAR(45) NULL DEFAULT NULL,
  `idClientes` INT NULL DEFAULT NULL,
  `idEmpleados` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idVentas`),
  INDEX `idClientes` (`idClientes`),
  INDEX `idEmpleados` (`idEmpleados`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`idClientes`) REFERENCES `clientes` (`idClientes`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`idEmpleados`) REFERENCES `empleados` (`idEmpleados`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `detalleventa` (
  `idDetalleVenta` INT NOT NULL AUTO_INCREMENT,
  `idProductos` INT NULL DEFAULT NULL,
  `idVentas` INT NULL DEFAULT NULL,
  `cantidad` INT NOT NULL,
  `precioUnitario` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idDetalleVenta`),
  INDEX `idProductos` (`idProductos`),
  INDEX `idVentas` (`idVentas`),
  CONSTRAINT `detalleventa_ibfk_1` FOREIGN KEY (`idProductos`) REFERENCES `productos` (`idProductos`),
  CONSTRAINT `detalleventa_ibfk_2` FOREIGN KEY (`idVentas`) REFERENCES `ventas` (`idVentas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `pagos` (
  `idPagos` INT NOT NULL AUTO_INCREMENT,
  `montoPago` DECIMAL(10,2) NOT NULL,
  `fechaPago` DATETIME NOT NULL,
  `metodoPago` VARCHAR(45) NULL DEFAULT NULL,
  `idVentas` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idPagos`),
  INDEX `idVentas` (`idVentas`),
  CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`idVentas`) REFERENCES `ventas` (`idVentas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
