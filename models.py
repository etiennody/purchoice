#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Enum, Integer, String, Text, ForeignKey

# Construct a base class for declarative class definitions
Base = declarative_base()

# Create an association for category and product in a ManyToMany relationship
cat_prod_asso_table = Table(
    "cat_prod_asso",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("category.category_id")),
    Column("product_id", Integer, ForeignKey("product.product_id")),
)

# Create an association for brand and product in a ManyToMany relationship
brand_prod_asso_table = Table(
    "brand_prod_asso",
    Base.metadata,
    Column("brand_id", Integer, ForeignKey("brand.brand_id")),
    Column("product_id", Integer, ForeignKey("product.product_id")),
)


# Details about category table to which is mapping
class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(100))


# Details about store table to which is mapping
class Store(Base):
    __tablename__ = "store"
    store_id = Column(Integer, primary_key=True)
    store_name = Column(String(100))
    product_stores = relationship(
        "ProductStore",
        backref="store_product_store"
    )


# Details about brand table to which is mapping
class Brand(Base):
    __tablename__ = "brand"
    brand_id = Column(Integer, primary_key=True)
    brand_name = Column(String(100))


# Details about product table to which is mapping
class Product(Base):
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    generic_name = Column(Text())
    url = Column(String(500))
    nutrition_grade_fr = Column(Enum("a", "b", "c", "d", "e"))
    ingredients_text_fr = Column(Text())
    additives_n = Column(Integer)
    categories = relationship(
        "Category",
        secondary="cat_prod_asso",
        backref=backref("prod_categories", lazy="dynamic")
    )
    brands = relationship(
        "Brand",
        secondary="brand_prod_asso",
        backref=backref("prod_brands", lazy="dynamic")
    )
    product_stores = relationship(
        "ProductStore",
        backref="product_product_store"
    )


# Details about product_store table to which is mapping
class ProductStore(Base):
    __tablename__ = "product_store"
    product_store_id = Column(Integer, primary_key=True)
    store_product_store_id = Column(Integer, ForeignKey("store.store_id"))
    product_product_store_id = Column(
        Integer,
        ForeignKey("product.product_id")
    )


# Details about favorite table to which is mapping
# class Favorite(Base):
#     __tablename__ = "favorite"
#     favorite_id = Column(Integer, primary_key=True)
#     product_id = Column(Integer, ForeignKey("product.product_id"))
#     product_substitut_id = Column(Integer, ForeignKey("product_store.product_store_id"))
#     product = relationship("Product", backref="favorites")
#     product_substitut = relationship("Product", backref="favorite_substituts")
