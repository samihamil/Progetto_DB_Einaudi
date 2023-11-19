-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 19, 2023 at 12:59 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Table structure for table `dipendenti_sami_hamil`
--

CREATE TABLE `dipendenti_sami_hamil` (
  `id` int(11) AUTO_INCREMENT primary key,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `indirizzo` varchar(1024) NOT NULL,
  `telefono` bigint(10) NOT NULL,
  `posizione lavorativa` varchar(100) NOT NULL,
  `data di assunzione` date NOT NULL,
  `data_di_nascita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `dipendenti_sami_hamil`
--

/* DATI DI PROVA 
INSERT INTO `dipendenti_sami_hamil` (`id`, `nome`, `cognome`, `indirizzo`, `telefono`, `posizione lavorativa`, `data di assunzione`, `data_di_nascita`) VALUES
(3, 'Sami', 'Hamil', 'Liberazione', 3519431910, 'Manager', '2023-10-10', '2005-11-25'),
(45, 's', 'df', 'fds', 54, 'fsd', '2023-10-13', '2023-10-20'),
(132, 'harman', 'Singh', 'Aoo', 3334445551, 'Magazziniere', '2021-04-14', '2005-09-25'),
(0, 'Sandro', 'Pertini', 'Sandro Pertini', 455464, 'MAnager', '2001-12-25', '2001-12-25');*/

-- --------------------------------------------------------

--
-- Table structure for table `zone_di_lavoro_sami_hamil`
--

CREATE TABLE `zone_di_lavoro_sami_hamil` (
  `id_zona` int(11) AUTO_INCREMENT primary key,
  `nome_zona` varchar(100) NOT NULL,
  `numero_clienti` int(255) NOT NULL,
  `id_dipendenti` int(11) NOT NULL,
  `città` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `zone_di_lavoro_sami_hamil`
--

/* DATI DI PROVA
INSERT INTO `zone_di_lavoro_sami_hamil` (`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendenti`, `città`) VALUES
(0, 'Ma', 234, 35, 'dgsg'),
(12, '1215', 8554, 1, 'Reggiolo'); */

--
-- Indexes for dumped tables
--

--
-- Indexes for table `zone_di_lavoro_sami_hamil`
--

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
