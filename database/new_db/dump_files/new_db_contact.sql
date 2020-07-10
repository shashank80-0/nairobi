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
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `staff_emp_id` varchar(11) NOT NULL,
  `phone_num` varchar(10) NOT NULL,
  `email_addr` varchar(45) NOT NULL,
  `home_addr` varchar(60) NOT NULL,
  `address_city_id` varchar(3) NOT NULL,
  PRIMARY KEY (`staff_emp_id`),
  UNIQUE KEY `phone_num` (`phone_num`),
  UNIQUE KEY `email_addr` (`email_addr`),
  UNIQUE KEY `home_addr` (`home_addr`),
  KEY `fk_contact_staff_idx` (`staff_emp_id`),
  KEY `fk_contact_address_idx` (`address_city_id`),
  CONSTRAINT `fk_contact_address` FOREIGN KEY (`address_city_id`) REFERENCES `address` (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES ('A75-06-15MA','9124568884','angela@dundermifflin.com','266/65 Humayun Nagar','HBD'),('C58-10-16BR','9897783384','creed@dundermifflin.com','Flat No. 435 Lotus Apartments, Arjun Nagar','AGR'),('D66-01-20SC','9634107618','dwight@dundermifflin.com','House 36A Sarita Vihar','DEL'),('J79-10-20HA','8696111347','jim@dundermifflin.com','Flat no 405 Emirates Apartments Khandari','AGR'),('M62-08-16SC','9691438810','micahel69@dundermifflin.com','B-4 Sector 47','HBD'),('P74-03-07BE','9897783380','pam@dundermifflin.com','Kholi No.420 Dharavi','MUB'),('T67-02-22FL','8882121297','toby@dundermifflin.com','Villa No. 3 Paramount Society Ashok Nagar','KOL');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
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
