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
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `emp_id` varchar(11) GENERATED ALWAYS AS (upper(concat(substr(`first_name`,1,1),substr(`birth_date`,3),substr(`last_name`,1,2)))) STORED NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `birth_date` date NOT NULL,
  `pass` varchar(20) NOT NULL,
  `designation_role_id` varchar(10) NOT NULL,
  PRIMARY KEY (`emp_id`),
  KEY `fk_staff_designation_idx` (`designation_role_id`),
  CONSTRAINT `fk_staff_designation_idx` FOREIGN KEY (`designation_role_id`) REFERENCES `designation` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` (`first_name`, `last_name`, `birth_date`, `pass`, `designation_role_id`) VALUES ,'Andy','Bernard','1972-03-28','nard@dog','SA'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),'Dwight','Schrutte','1966-01-20','bears_beet','ARM'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),'Dwight','Schrutte','1966-01-20','bears_beet','ARM'),'Jim','Halpert','1979-10-20','jello_stuff','SA'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),'Dwight','Schrutte','1966-01-20','bears_beet','ARM'),'Jim','Halpert','1979-10-20','jello_stuff','SA'),'Kevin','Malone','1970-12-24','cookies','AC'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),'Dwight','Schrutte','1966-01-20','bears_beet','ARM'),'Jim','Halpert','1979-10-20','jello_stuff','SA'),'Kevin','Malone','1970-12-24','cookies','AC'),'Michael','Scott','1962-08-16','ryan_howard','RM'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),'Dwight','Schrutte','1966-01-20','bears_beet','ARM'),'Jim','Halpert','1979-10-20','jello_stuff','SA'),'Kevin','Malone','1970-12-24','cookies','AC'),'Michael','Scott','1962-08-16','ryan_howard','RM'),'Oscar','Martinez','1974-09-02','oscar_456','AC'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),'Dwight','Schrutte','1966-01-20','bears_beet','ARM'),'Jim','Halpert','1979-10-20','jello_stuff','SA'),'Kevin','Malone','1970-12-24','cookies','AC'),'Michael','Scott','1962-08-16','ryan_howard','RM'),'Oscar','Martinez','1974-09-02','oscar_456','AC'),'Pam','Bessly','1974-03-07','receptionist101','ADM'),,'Andy','Bernard','1972-03-28','nard@dog','SA'),'Angela','Martin','1975-06-15','bandit_jesus','AC'),'Creed','Bratton','1958-10-16','cartwheeler','QA'),'Dwight','Schrutte','1966-01-20','bears_beet','ARM'),'Jim','Halpert','1979-10-20','jello_stuff','SA'),'Kevin','Malone','1970-12-24','cookies','AC'),'Michael','Scott','1962-08-16','ryan_howard','RM'),'Oscar','Martinez','1974-09-02','oscar_456','AC'),'Pam','Bessly','1974-03-07','receptionist101','ADM'),'Toby','Flenderson','1967-02-22','pamhearttoby','HR');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
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
