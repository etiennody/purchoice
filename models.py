#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Enum, Integer, String, ForeignKey

# Engine configuration to connect database with PyMySQL
engine = create_engine(
    "mysql+pymysql://purbeurre:purbeurre@localhost/purchoice", echo=True
)

# Construct a base class for declarative class definitions
Base = declarative_base()

# Create an association for category and product in a ManyToMany relationship
cat_prod_asso_table = Table(
    "cat_prod_asso",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("category.id")),
    Column("product_id", Integer, ForeignKey("product.id")),
)

# Create an association for brand and product in a ManyToMany relationship
brand_prod_asso_table = Table(
    "brand_prod_asso",
    Base.metadata,
    Column("brand_id", Integer, ForeignKey("brand.id")),
    Column("product_id", Integer, ForeignKey("product.id")),
)


# Details about category table to which is mapping
class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(100))


# Details about store table to which is mapping
class Store(Base):
    __tablename__ = "store"
    id = Column(Integer, primary_key=True)
    store_name = Column(String(100))


# Details about brand table to which is mapping
class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, primary_key=True)
    brand_name = Column(String(100))


# Details about product table to which is mapping
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    description = Column(String(1000))
    url = Column(String(500))
    nutrition_grade_fr = Column(Enum("A", "B", "C", "D", "E"))
    ingredients_text = Column(String(1000))
    additives = Column(String(500))
    ingredients_from_palm_oil_n = Column(Integer)
    traces = Column(String(100))
    categories = relationship("Category", secondary="cat_prod_asso", backref="products")
    brands = relationship("Brand", secondary="brand_prod_asso", backref="products")


# Details about product_store table to which is mapping
class ProductStore(Base):
    __tablename__ = "product_store"
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("store.id"))
    product_store_id = Column(Integer, ForeignKey("product.id"))
    store = relationship("Store", backref="product_stores")
    product_store = relationship("Product", backref="products")


# Details about favorite table to which is mapping
class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    product_substitut_id = Column(Integer, ForeignKey("product_store.id"))
    product = relationship("Product", backref="favorites")
    product_substitut = relationship("Product", backref="favorite_substituts")


# Create a schema using metadata to issue CREATE TABLE statements
Base.metadata.create_all(engine)
