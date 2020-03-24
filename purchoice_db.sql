--
-- Database structure of purchoice
--
DROP DATABASE IF EXISTS purchoice;
CREATE DATABASE purchoice;
USE purchoice;


--
-- Table structure for table category
--
CREATE TABLE category (
    id INT AUTO_INCREMENT NOT NULL,
    category_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE UNIQUE INDEX category_idx
ON category
( category_name ASC );

--
-- Table structure for table store
--
CREATE TABLE store (
    id INT AUTO_INCREMENT NOT NULL,
    store_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE UNIQUE INDEX store_idx
ON store
( store_name ASC );


--
-- Table structure for table brand
--
CREATE TABLE brand (
    id INT AUTO_INCREMENT NOT NULL,
    brand_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE UNIQUE INDEX brand_idx
ON brand
( brand_name ASC );


--
-- Table structure for table product
--
CREATE TABLE product (
    id INT AUTO_INCREMENT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description VARCHAR(1000) NOT NULL,
    url VARCHAR(500) NOT NULL,
    nutrition_grade_fr ENUM NOT NULL,
    ingredients_text VARCHAR(1000) NOT NULL,
    additives VARCHAR NOT NULL,
    ingredients_from_palm_oil_n INT NOT NULL,
    traces VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE INDEX product_idx
ON product
( product_name ASC );


--
-- Table structure for table product-store
--
CREATE TABLE product_store (
    id INT AUTO_INCREMENT NOT NULL,
    store_id INT NOT NULL,
    product_store_id INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table favorite
--
CREATE TABLE favorite (
    id INT AUTO_INCREMENT NOT NULL,
    product_id INT NOT NULL,
    product_substitut_id INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE INDEX favorite_idx
ON favorite
( product_substitut_id ASC );

--
-- Link category table with product table
--
ALTER TABLE product ADD CONSTRAINT category_product_fk
FOREIGN KEY (id)
REFERENCES category (id)
ON DELETE SET NULL;

--
-- Link store table with product_store table
--
ALTER TABLE product_store ADD CONSTRAINT store_product_store_fk
FOREIGN KEY (store_id)
REFERENCES store (id)
ON DELETE SET NULL;

--
-- Link brand table with product table
--
ALTER TABLE product ADD CONSTRAINT brand_product_fk
FOREIGN KEY (id)
REFERENCES brand (id)
ON DELETE SET NULL;

--
-- Link product table with favorite table
--
ALTER TABLE favorite ADD CONSTRAINT product_favorite_substitut_fk
FOREIGN KEY (product_substitut_id)
REFERENCES product (id)
ON DELETE SET NULL;

--
-- Link product table with product_store table
--
ALTER TABLE product_store ADD CONSTRAINT product_product_store_fk
FOREIGN KEY (product_store_id)
REFERENCES product (id)
ON DELETE SET NULL;

--
-- Link product table with favorite table
--
ALTER TABLE favorite ADD CONSTRAINT product_favorite_fk
FOREIGN KEY (product_id)
REFERENCES product (id)
ON DELETE SET NULL;
