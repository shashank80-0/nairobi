CREATE DATABASE  IF NOT EXISTS `new_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `new_db`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: new_db
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `attribute`
--

DROP TABLE IF EXISTS `attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attribute` (
  `attributecol` int NOT NULL AUTO_INCREMENT,
  `staff_emp_id` varchar(11) NOT NULL,
  `technology_skill_id` varchar(2) NOT NULL,
  PRIMARY KEY (`attributecol`),
  KEY `fk_attributes_staff_idx` (`staff_emp_id`),
  KEY `fk_attribute_technology_idx` (`technology_skill_id`),
  CONSTRAINT `fk_attribute_technology` FOREIGN KEY (`technology_skill_id`) REFERENCES `technology` (`skill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attribute`
--

LOCK TABLES `attribute` WRITE;
/*!40000 ALTER TABLE `attribute` DISABLE KEYS */;
INSERT INTO `attribute` VALUES (1,'D66-01-20SC','JV'),(2,'D66-01-20SC','PY'),(3,'D66-01-20SC','MG'),(4,'D66-01-20SC','JS'),(5,'D66-01-20SC','AD'),(6,'J79-10-20HA','CS'),(7,'J79-10-20HA','HT'),(8,'J79-10-20HA','DB'),(9,'J79-10-20HA','JS'),(10,'J79-10-20HA','SQ'),(11,'M62-08-16SC','SV'),(12,'M62-08-16SC','MG'),(13,'M62-08-16SC','PY'),(14,'M62-08-16SC','JV'),(15,'P74-03-07BE','JV'),(16,'P74-03-07BE','MG'),(17,'P74-03-07BE','JS'),(18,'P74-03-07BE','CS'),(19,'T67-02-22FL','SV'),(20,'T67-02-22FL','DB'),(21,'T67-02-22FL','HT');
/*!40000 ALTER TABLE `attribute` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-03 14:02:01
