-- MySQL dump 10.13  Distrib 5.6.34, for Win64 (x86_64)
--
-- Host: localhost    Database: Triangulacije
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dijagonala`
--

DROP TABLE IF EXISTS `dijagonala`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dijagonala` (
  `ID_Dijagonale` int(11) NOT NULL,
  `ID_Triangulacije` int(11) DEFAULT NULL,
  `ID_Pocetne_Tocke` int(11) DEFAULT NULL,
  `ID_Krajnje_Tocke` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_Dijagonale`),
  KEY `ID_Pocetne_Tocke_idx` (`ID_Pocetne_Tocke`),
  KEY `ID_Krajnje_Tocke_idx` (`ID_Krajnje_Tocke`),
  KEY `ID_Triangulacije` (`ID_Triangulacije`),
  CONSTRAINT `ID_Krajnje_Tocke` FOREIGN KEY (`ID_Krajnje_Tocke`) REFERENCES `tocka` (`ID_Tocke`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ID_Pocetne_Tocke` FOREIGN KEY (`ID_Pocetne_Tocke`) REFERENCES `tocka` (`ID_Tocke`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ID_Triangulacije` FOREIGN KEY (`ID_Triangulacije`) REFERENCES `triangulacija` (`ID_Triangulacije`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dijagonala`
--

LOCK TABLES `dijagonala` WRITE;
/*!40000 ALTER TABLE `dijagonala` DISABLE KEYS */;
/*!40000 ALTER TABLE `dijagonala` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tocka`
--

DROP TABLE IF EXISTS `tocka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tocka` (
  `ID_Tocke` int(11) NOT NULL,
  `x_koordinata` double DEFAULT NULL,
  `y_koordinata` double DEFAULT NULL,
  PRIMARY KEY (`ID_Tocke`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tocka`
--

LOCK TABLES `tocka` WRITE;
/*!40000 ALTER TABLE `tocka` DISABLE KEYS */;
/*!40000 ALTER TABLE `tocka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triangulacija`
--

DROP TABLE IF EXISTS `triangulacija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triangulacija` (
  `ID_Triangulacije` int(11) NOT NULL,
  PRIMARY KEY (`ID_Triangulacije`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triangulacija`
--

LOCK TABLES `triangulacija` WRITE;
/*!40000 ALTER TABLE `triangulacija` DISABLE KEYS */;
/*!40000 ALTER TABLE `triangulacija` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-21 21:48:02
