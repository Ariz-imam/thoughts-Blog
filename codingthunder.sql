-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 09, 2022 at 10:40 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `id` int(11) NOT NULL,
  `ans_of` int(11) NOT NULL,
  `ans` longtext NOT NULL,
  `post_by` int(11) NOT NULL,
  `post_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `ans_of`, `ans`, `post_by`, `post_on`) VALUES
(15, 1, '<p><strong>We could add margin from all direction as well as from any specific direction:</strong></p><ol><li><strong>From all direction&nbsp;</strong></li></ol><ul><li><strong>m-1, m-2, m-3, m-4 or m-auto, mx-auto</strong></li></ul><ol><li><strong>From specific direction</strong></li></ol><ul><li><strong>mt-1, mt-2 …so on till mt-5 </strong>For margin from top</li><li><strong>mb-1, mb-2, …..so on till mb-5 </strong>For margin from bottom</li><li><strong>ml-1, ml-2 …. so on till ml-5 </strong>For margin from left</li><li><strong>mr-1, mr-2, ….so on till mr-5 </strong>For margin from right</li></ul>', 4, '2021-12-06'),
(33, 17, '<p>You should learn github from code with harry youtube channel.</p>', 4, '2022-03-08');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(24, 'Faisal Azmi', '08271406688', 'kuch v', '2022-02-20 23:18:07', 'faisalprofessional1@gmail.com'),
(25, 'Faisal Azmi', '08271406688', 'Ajax request check.', '2022-02-20 23:34:13', 'faisalprofessional1@gmail.com'),
(26, 'Faisal Azmi', '08271406688', 'kuch v', '2022-02-20 23:37:19', 'faisalprofessional1@gmail.com'),
(27, 'Faisal Azmi', '08271406688', 'Ajax Check up', '2022-02-20 23:43:08', 'faisalprofessional1@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `ques_title` varchar(255) NOT NULL,
  `ques_desc` varchar(500) NOT NULL,
  `post_on` date DEFAULT NULL,
  `post_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `ques_title`, `ques_desc`, `post_on`, `post_by`) VALUES
(1, 'Web Development', '<p>What is the class to add margin through bootstrap?</p>', '2021-12-05', 4),
(9, 'Travelling ', '<p>What is the most beautiful place to visit in winter in New York??</p>', '2021-12-09', 4),
(12, 'Cricket game', 'Who is the captain of Pakistan team?? and how many world cups are being won by pakistan team??', '2021-12-09', 4),
(13, 'Study', '<p>How to practice for coding interviews? What subjects are necessary??</p>', '2022-01-02', 4),
(17, 'Learning', '<p>How to learn github in 1 week?</p>', '2022-03-08', 12);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `fullname` varchar(255) NOT NULL,
  `phone` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `profession` varchar(255) NOT NULL,
  `city` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `gender` varchar(255) NOT NULL,
  `pic` longblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `fullname`, `phone`, `email`, `pass`, `profession`, `city`, `country`, `gender`, `pic`) VALUES
(4, 'Faisal Azmi', 2147483647, 'faisalprofessional1@gmail.com', '$5$rounds=535000$N0QMx7LygBcBpeBe$xxQZz6E6E.y6IploQhVIRiJPSOXLF.0upYhFnAAif/B', 'Student', 'Patna', 'India', 'male', NULL),
(12, 'Ariz Imam', 2147483647, 'ariz.imam585@gmail.com', '$5$rounds=535000$eVT5sjhxqZgNGHmO$ylMkxYXoUxbcCs0Vni5mTkTtbpiu1DS8uvEPtwl5f9C', 'student', NULL, NULL, 'male', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ans_of` (`ans_of`),
  ADD KEY `post_by` (`post_by`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `post_by` (`post_by`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answers`
--
ALTER TABLE `answers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`ans_of`) REFERENCES `questions` (`id`),
  ADD CONSTRAINT `answers_ibfk_2` FOREIGN KEY (`post_by`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`post_by`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
