#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

# Construct a base class for declarative class definitions
Base = declarative_base()

# Create an association for category and product in a ManyToMany relationship
cat_prod_asso = Table(
    "cat_prod_asso",
    Base.metadata,
    Column(
        "category_id",
        Integer,
        ForeignKey("category.category_id", ondelete="CASCADE")
    ),
    Column(
        "product_id",
        Integer,
        ForeignKey("product.product_id", ondelete="CASCADE")),
)

# Create an association for brand and product in a ManyToMany relationship
brand_prod_asso = Table(
    "brand_prod_asso",
    Base.metadata,
    Column(
        "brand_id",
        Integer,
        ForeignKey("brand.brand_id", ondelete="CASCADE")
    ),
    Column(
        "product_id",
        Integer,
        ForeignKey("product.product_id", ondelete="CASCADE")
    ),
)

# Create an association for brand and product in a ManyToMany relationship
store_prod_asso = Table(
    "store_prod_asso",
    Base.metadata,
    Column(
        "store_id",
        Integer,
        ForeignKey("store.store_id", ondelete="CASCADE")
    ),
    Column(
        "product_id",
        Integer,
        ForeignKey("product.product_id", ondelete="CASCADE")
    ),
)


class Category(Base):
    """Details about category table to which is mapping"""
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True)
    category_name = Column(
        String(500), server_default="default"
    )

    def __repr__(self):
        return "<Category %r>" % self.category_name


class Store(Base):
    """Details about store table to which is mapping"""
    __tablename__ = "store"
    store_id = Column(Integer, primary_key=True)
    store_name = Column(
        String(100), server_default="default"
    )

    def __repr__(self):
        return self.store_name


class Brand(Base):
    """Details about brand table to which is mapping"""
    __tablename__ = "brand"
    brand_id = Column(Integer, primary_key=True)
    brand_name = Column(
        String(100), server_default="default"
    )

    def __repr__(self):
        return self.brand_name


class Product(Base):
    """Details about product table to which is mapping"""
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    generic_name = Column(Text())
    url = Column(String(500))
    nutrition_grade_fr = Column(
        Enum("a", "b", "c", "d", "e", name="nutrition_grades")
    )
    ingredients_text_fr = Column(Text())
    additives_n = Column(Integer)
    categories = relationship(
        "Category",
        secondary=cat_prod_asso,
        backref=backref("products", lazy="dynamic")
    )
    brands = relationship(
        "Brand",
        secondary=brand_prod_asso,
        backref=backref("products", lazy="dynamic")
    )
    stores = relationship(
        "Store",
        secondary=store_prod_asso,
        backref=backref("products", lazy="dynamic")
    )
    favorites = relationship(
        "Favorite",
        primaryjoin="and_(Product.product_id == Favorite.product_id, Product.product_id == Favorite.product_substitute_id)",
        backref=backref("products")
    )

    def __repr__(self):
        return self.product_name


class Favorite(Base):
    """Details about favorite table to which is mapping"""
    __tablename__ = "favorite"
    favorite_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.product_id"))
    product_substitute_id = Column(Integer, ForeignKey("product.product_id"))
