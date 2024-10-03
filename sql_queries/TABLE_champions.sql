CREATE DATABASE TFT_POOL;

USE TFT_POOL;

CREATE TABLE champion (
  `id` INT PRIMARY KEY,
  `character_name` VARCHAR(255),
  `data` JSON
)

CREATE TABLE item (
  `id` INT PRIMARY KEY,
  `item_name` VARCHAR(255),
  `data` JSON
)