CREATE DATABASE IF NOT EXISTS GearWiki;
USE GearWiki;

CREATE TABLE `users` (
    `user_id` INT NOT NULL AUTO_INCREMENT,
    `user_name` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `signup_date` DATE NOT NULL,
    `base_atk` INT DEFAULT NULL,
    `base_def` INT DEFAULT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `sets` (
    `set_id` INT NOT NULL AUTO_INCREMENT,
    `set_name` VARCHAR(50) NOT NULL,
    `effect` VARCHAR(50) DEFAULT NULL,
    PRIMARY KEY (`set_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `items` (
    `item_id` INT NOT NULL AUTO_INCREMENT,
    `item_name` VARCHAR(255) DEFAULT NULL,
    `item_img` VARCHAR(255) DEFAULT NULL,
    `parts` ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    `item_def` INT NOT NULL,
    `item_atk` INT NOT NULL,
    `set_id` INT DEFAULT NULL,
    PRIMARY KEY (`item_id`),
    CONSTRAINT `fk_items_sets` FOREIGN KEY (`set_id`) REFERENCES `sets` (`set_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `preset_list` (
    `presetList_id` INT NOT NULL AUTO_INCREMENT,
    `preset_id` INT DEFAULT NULL,
    `user_id` INT DEFAULT NULL,
    `preset_name` VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (`presetList_id`),
    CONSTRAINT `fk_presetlist_preset` FOREIGN KEY (`preset_id`) REFERENCES `preset` (`preset_id`) ON DELETE CASCADE,
    CONSTRAINT `fk_presetlist_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `preset` (
    `preset_id` INT NOT NULL AUTO_INCREMENT,
    `item_id` INT DEFAULT NULL,
    `preset_name` VARCHAR(100) DEFAULT NULL,
    `parts` ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    PRIMARY KEY (`preset_id`),
    CONSTRAINT `fk_preset_items` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

