-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 14 Cze 2021, 15:42
-- Wersja serwera: 10.4.19-MariaDB
-- Wersja PHP: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `projekt`
--
CREATE DATABASE IF NOT EXISTS `projekt` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `projekt`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `ogloszenia`
--

CREATE TABLE `ogloszenia` (
  `ID_ogloszenia` int(11) NOT NULL,
  `ID_hydraulika` int(11) NOT NULL,
  `Nazwa_ogloszenia` varchar(45) NOT NULL,
  `Tresc` varchar(250) NOT NULL,
  `Promowanie` bit(1) NOT NULL,
  `data_wystawienia_ogloszenia` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `ogloszenia`
--

INSERT INTO `ogloszenia` (`ID_ogloszenia`, `ID_hydraulika`, `Nazwa_ogloszenia`, `Tresc`, `Promowanie`, `data_wystawienia_ogloszenia`) VALUES
(1, 1, 'Hydraulik1', 'Wykonuję usługi hydrauliczne dla firm i osób prywatnych w lokalach mieszkalnych oraz biurowych biur. Wszystkie prace robię według potrzeb klienta. Zapraszam do kontaktu', b'1', '2021-06-07'),
(2, 2, 'Hydraulik2', 'Usługi hydrauliczne wszelkiego rodzaju', b'0', '2021-06-07'),
(3, 3, 'Hydraulik3', 'Korzystając z moich usług, masz pewność, że nic Cię nie zaskoczy. Możesz ufać moim umiejętnościom, doświadczeniu i rzetelności. Żadnych ukrytych kosztów.', b'0', '2021-06-07'),
(4, 4, 'Hydraulik4', 'Podejmę sie mniejszych oraz tych większych usterek.Gwarancja najwyzszej jakosci uslug jest specjalistyczny sprzet, oraz wieloletnia praktyka.', b'0', '2021-06-07'),
(5, 5, 'Hydraulik5', 'Witam, oferuję prace z zakresu instalacji wodno-kanalizacyjnej, instalacji centralnego ogrzewania, instalacji gazowych, instalacji wodomierzy. Na wszelkie pytania odpowiem telefonicznie.', b'1', '2021-06-07'),
(6, 6, 'Hydraulik6', 'Wykonujemy usługi hydrauliczne drobne i kompleksowe usługi oraz różnego rodzaju przeróbki i usuwanie awarii.', b'0', '2021-06-14'),
(7, 7, 'HydraulikSzczecin', 'Zapraszam', b'1', '2021-06-14');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `ogloszenia`
--
ALTER TABLE `ogloszenia`
  ADD PRIMARY KEY (`ID_ogloszenia`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
