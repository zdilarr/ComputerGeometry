-- MySQL dump 10.13  Distrib 5.6.34, for Win64 (x86_64)
--
-- Host: localhost    Database: triangulation
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
-- Table structure for table `diagonal`
--

DROP TABLE IF EXISTS `diagonal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagonal` (
  `diagonal_id` int(11) NOT NULL,
  `triangulation_id` int(11) DEFAULT NULL,
  `starting_point_id` int(11) DEFAULT NULL,
  `ending_point_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`diagonal_id`),
  KEY `starting_point_id_idx` (`starting_point_id`),
  KEY `ending_point_id_idx` (`ending_point_id`),
  KEY `triangulation_id` (`triangulation_id`),
  CONSTRAINT `ending_point_id` FOREIGN KEY (`ending_point_id`) REFERENCES `point` (point_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `starting_point_id` FOREIGN KEY (`starting_point_id`) REFERENCES `point` (point_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `triangulation_id` FOREIGN KEY (`triangulation_id`) REFERENCES `triangulation` (`triangulation_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagonal`
--

LOCK TABLES `diagonal` WRITE;
/*!40000 ALTER TABLE `diagonal` DISABLE KEYS */;
/*!40000 ALTER TABLE `diagonal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `point`
--

DROP TABLE IF EXISTS `point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `point` (
  point_id int(11) NOT NULL,
  `x_coordinate` double DEFAULT NULL,
  `y_coordinate` double DEFAULT NULL,
  PRIMARY KEY (point_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `point`
--

LOCK TABLES `point` WRITE;
/*!40000 ALTER TABLE `point` DISABLE KEYS */;
/*!40000 ALTER TABLE `point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triangulation`
--

DROP TABLE IF EXISTS `triangulation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triangulation` (
  `triangulation_id` int(11) NOT NULL,
  PRIMARY KEY (`triangulation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triangulation`
--

LOCK TABLES `triangulation` WRITE;
/*!40000 ALTER TABLE `triangulation` DISABLE KEYS */;
/*!40000 ALTER TABLE `triangulation` ENABLE KEYS */;
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
