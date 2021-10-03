-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2019 at 07:33 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ganesh`
--

-- --------------------------------------------------------

--
-- Table structure for table `wow`
--

CREATE TABLE `wow` (
  `Customer_name` varchar(100) NOT NULL,
  `Customer_number` varchar(100) NOT NULL,
  `Order_details` varchar(1000) NOT NULL,
  `Total` varchar(100) NOT NULL,
  `Date` varchar(100) NOT NULL,
  `Time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wow`
--

INSERT INTO `wow` (`Customer_name`, `Customer_number`, `Order_details`, `Total`, `Date`, `Time`) VALUES
('ganesh', '7896541230', '{Burger X} 1 = 99\n{Pizza X} 1 = 149\n{Water X} 1 = 20\n{SoftDrink X} 1 = 40\n\nTOTAL= 308\n', '308', '', '0'),
('ganesh', '7894563210', '{Burger X} 1 = 99\n{Fries X} 1 = 55\n{SoftDrink X} 2 = 80\n\nTOTAL= 234\n', '234', '', '0'),
('tanvi', '1234567920', '{Fries X} 1 = 55\n{Pizza X} 1 = 149\n{SoftDrink X} 1 = 40\n\nTOTAL= 244\n', '244', 'Fri,Dec-20-19', '11:52:12'),
('neeraj', '9969321588', '{Burger X} 3 = 297\n{Water X} 1 = 20\n{SoftDrink X} 1 = 40\n\nTOTAL= 357\n', '357', 'Fri,Dec-20-19', '11:54:49'),
('akanksha', '7418529630', '{Burger X} 1 = 99\n{Pizza X} 1 = 149\n{Water X} 1 = 20\n{SoftDrink X} 1 = 40\n\nTOTAL= 308\n', '308', 'Fri,Dec-20-19', '11:56:15'),
('tr', '7415236900', '{Fries X} 1 = 55\n{Water X} 1 = 20\n{SoftDrink X} 1 = 40\n\nTOTAL= 115\n', '115', 'Fri,Dec-20-19', '12:01:22');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
