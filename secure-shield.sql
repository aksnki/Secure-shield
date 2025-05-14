/*
SQLyog Community v13.3.0 (64 bit)
MySQL - 5.6.12-log : Database - threat_dectection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`threat_dectection` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `threat_dectection`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add login',7,'add_login'),
(26,'Can change login',7,'change_login'),
(27,'Can delete login',7,'delete_login'),
(28,'Can view login',7,'view_login'),
(29,'Can add user',8,'add_user'),
(30,'Can change user',8,'change_user'),
(31,'Can delete user',8,'delete_user'),
(32,'Can view user',8,'view_user'),
(33,'Can add review',9,'add_review'),
(34,'Can change review',9,'change_review'),
(35,'Can delete review',9,'delete_review'),
(36,'Can view review',9,'view_review'),
(37,'Can add report',10,'add_report'),
(38,'Can change report',10,'change_report'),
(39,'Can delete report',10,'delete_report'),
(40,'Can view report',10,'view_report'),
(41,'Can add complaint',11,'add_complaint'),
(42,'Can change complaint',11,'change_complaint'),
(43,'Can delete complaint',11,'delete_complaint'),
(44,'Can view complaint',11,'view_complaint');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(11,'myapp','complaint'),
(7,'myapp','login'),
(10,'myapp','report'),
(9,'myapp','review'),
(8,'myapp','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2025-01-23 19:50:44.002169'),
(2,'auth','0001_initial','2025-01-23 19:50:44.152169'),
(3,'admin','0001_initial','2025-01-23 19:50:44.484172'),
(4,'admin','0002_logentry_remove_auto_add','2025-01-23 19:50:44.559170'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-01-23 19:50:44.567180'),
(6,'contenttypes','0002_remove_content_type_name','2025-01-23 19:50:44.641181'),
(7,'auth','0002_alter_permission_name_max_length','2025-01-23 19:50:44.678171'),
(8,'auth','0003_alter_user_email_max_length','2025-01-23 19:50:44.721181'),
(9,'auth','0004_alter_user_username_opts','2025-01-23 19:50:44.730181'),
(10,'auth','0005_alter_user_last_login_null','2025-01-23 19:50:44.769170'),
(11,'auth','0006_require_contenttypes_0002','2025-01-23 19:50:44.774167'),
(12,'auth','0007_alter_validators_add_error_messages','2025-01-23 19:50:44.781167'),
(13,'auth','0008_alter_user_username_max_length','2025-01-23 19:50:44.818174'),
(14,'auth','0009_alter_user_last_name_max_length','2025-01-23 19:50:44.867170'),
(15,'auth','0010_alter_group_name_max_length','2025-01-23 19:50:44.909173'),
(16,'auth','0011_update_proxy_permissions','2025-01-23 19:50:44.918181'),
(17,'myapp','0001_initial','2025-01-23 19:50:45.041180'),
(18,'sessions','0001_initial','2025-01-23 19:50:45.195170'),
(19,'myapp','0002_auto_20250506_1057','2025-05-06 05:33:56.273970');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('awzrmkmdpteibznt9ly157wy8f09gbhq','YTg1ZDgxMzMxNzk0MmU3N2RlNmZkMmNiYmQ1YThkY2YwZWM1NGNmODp7ImxpZCI6OH0=','2025-05-20 06:58:51.817274'),
('f55z0e6wy3eibfv9n4ikgthuc5pu70hf','YTg1ZDgxMzMxNzk0MmU3N2RlNmZkMmNiYmQ1YThkY2YwZWM1NGNmODp7ImxpZCI6OH0=','2025-05-22 03:51:00.002743'),
('fepw6yb1pjuaengp8vulrvx2omdbp1ua','M2ZlMDcyZmVlYTNmNzU0NmI2MDEwYTZkNjQ5NmI2YWMxNWI2ZWRjYTp7ImxpZCI6NX0=','2025-04-01 06:27:22.905258'),
('uwxgjvpvqevjo22wndbdfp20mxgbydu2','M2ZlMDcyZmVlYTNmNzU0NmI2MDEwYTZkNjQ5NmI2YWMxNWI2ZWRjYTp7ImxpZCI6NX0=','2025-03-13 05:15:17.488466'),
('vg4vnxli3ob8h0b2lsfmhz8wrcnprvuz','ZWEzMDQ2YTRhMzUzODZiOTA0Nzc3MDRiZDNmZWYzY2M4ZWQwNzJjYTp7ImxpZCI6N30=','2025-04-24 06:10:30.939356'),
('xbg346p2ve90df9ia1ixjfz6lp0gnw0c','M2ZlMDcyZmVlYTNmNzU0NmI2MDEwYTZkNjQ5NmI2YWMxNWI2ZWRjYTp7ImxpZCI6NX0=','2025-02-20 08:01:53.722167');

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `complaint` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_USER_id_21ed0b20_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_complaint_USER_id_21ed0b20_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_complaint` */

insert  into `myapp_complaint`(`id`,`date`,`complaint`,`status`,`reply`,`USER_id`) values 
(1,'2025-02-04','','replied','nkndknmk kmkmekm',4),
(2,'2025-02-04','jkjdsjn nldsmlk','replied','knkcmsm',4),
(3,'2025-02-04','kjhknjj nk ','replied','bad user experience\r\n',4),
(4,'2025-04-10','hhjhhhj hhjhjhj','pending','pending',5),
(5,'2025-05-06','nice platform','replied','sorrry',6),
(6,'2025-05-07','facing some issues in mail spamming please resolve it','pending','pending',6);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin1234','admin'),
(2,'aks@gmail.com','Aks@123','user'),
(3,'aksnki@gmail.com','3751','user'),
(4,'bashjb@gmail.com','[\'textfield4\']','user'),
(5,'abc@gmail.com','Abc@1234','user'),
(6,'','',''),
(7,'abi@gmail.com','ab','user'),
(8,'athulv@gmail.com','Athul@123','user'),
(9,'athulv@gmail.cm','Amal@1234','user');

/*Table structure for table `myapp_report` */

DROP TABLE IF EXISTS `myapp_report`;

CREATE TABLE `myapp_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `content` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `result` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_report_USER_id_549bae6e_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_report_USER_id_549bae6e_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_report` */

/*Table structure for table `myapp_review` */

DROP TABLE IF EXISTS `myapp_review`;

CREATE TABLE `myapp_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `rating` varchar(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_review_USER_id_0e923f15_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_review_USER_id_0e923f15_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_review` */

insert  into `myapp_review`(`id`,`date`,`rating`,`review`,`USER_id`) values 
(4,'2025-05-05','<QueryDict: {\'csrfmiddlewaretoken\': [\'vJE88OvG9PJzCgGdWBcHHeYetV3JQYEnmZKmzGOdfC2XJtgWqmMxCotqIdXduG','nice platform',1),
(5,'2025-05-05','4','bhhkn jknujijoln ',5),
(6,'2025-05-05','4','asf nkl; jsnakM;DMASD;X,AMSMDK; DSA',4),
(7,'2025-05-05','2','nkdm;s knjsajcmaZS>msL>',4),
(8,'2025-05-06','4','very bad ',6);

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_no` varchar(100) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`username`,`email`,`phone_no`,`LOGIN_id`,`gender`,`place`) values 
(1,'akshay','aks@gmail.com','9994561238',2,'',''),
(2,'Varun.k','varunvkd@gmail.com','9994561238',3,'',''),
(3,'vishnu','bashjb@gmail.com','9994446111',4,'',''),
(4,'abc123','abc@gmail.com','9496502033',5,'',''),
(5,'abcg','abi@gmail.com','9994446111',7,'',''),
(6,'Athul v','athulv@gmail.com','5553334442',8,'Male','kozhikode'),
(7,'amal','athulv@gmail.cm','4422331155',9,'Female','kozhikode');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
