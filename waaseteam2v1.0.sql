-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema waaseteam2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema waaseteam2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `waaseteam2` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema waaseteam2
-- -----------------------------------------------------
USE `waaseteam2` ;

-- -----------------------------------------------------
-- Table `waaseteam2`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `waaseteam2`.`user` ;

CREATE TABLE IF NOT EXISTS `waaseteam2`.`user` (
  `username` VARCHAR(16) NOT NULL,
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(256) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`));


-- -----------------------------------------------------
-- Table `waaseteam2`.`user_profiles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `waaseteam2`.`user_profiles` ;

CREATE TABLE IF NOT EXISTS `waaseteam2`.`user_profiles` (
  `user_id` INT NOT NULL,
  `language_id` INT NOT NULL,
  PRIMARY KEY (`language_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `waaseteam2`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `waaseteam2`.`languages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `waaseteam2`.`languages` ;

CREATE TABLE IF NOT EXISTS `waaseteam2`.`languages` (
  `language_id` INT NOT NULL,
  `character` VARCHAR(1) NULL,
  `led_number` INT NULL,
  INDEX `language_id_idx` (`language_id` ASC) VISIBLE,
  CONSTRAINT `language_id`
    FOREIGN KEY (`language_id`)
    REFERENCES `waaseteam2`.`user_profiles` (`language_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
