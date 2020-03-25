#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Enum, Integer, String

# Engine configuration to connect database with PyMySQL
engine = create_engine(
    "mysql+pymysql:purbeurre/purbeurre@localhost/purchoice", echo=True
)

# Construct a base class for declarative class definitions
Base = declarative_base()


# Details about category table to which is mapping
class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    category_name = Column(String(100))

    def __repr__(self):
        return "<Category(category_name='%s')>" % (self.category_name)


# Details about store table to which is mapping
class Store(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True)
    store_name = Column(String(100))

    def __repr__(self):
        return "<Store(store_name='%s')>" % (self.store_name)


# Details about brand table to which is mapping
class Brand(Base):
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True)
    brand_name = Column(String(100))

    def __repr__(self):
        return "<Brand(brand_name='%s')>" % (self.brand_name)


# Details about product table to which is mapping
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    description = Column(String(1000))
    url = Column(String(500))
    nutrition_grade_fr = Column(Enum)
    ingredients_text = Column(String(1000))
    additives = Column(String())
    ingredients_from_palm_oil_n = Column(Integer)
    traces = Column(String(100))

    def __repr__(self):
        return (
            "<Product(product_name='%s', description='%s', url='%s', nutrition_grade_fr='%s', ingredients_text='%s', additives='%s', ingredients_from_palm_oil_n='%s', traces='%s')>"
            % (
                self.product_name,
                self.description,
                self.url,
                self.nutrition_grade_fr,
                self.ingredients_text,
                self.additives,
                self.ingredients_from_palm_oil_n,
                self.traces,
            )
        )


# Details about product_store table to which is mapping
class ProductStore(Base):
    __tablename__ = "product_store"

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer)
    product_store_id = Column(Integer)

    def __repr__(self):
        return "<ProductStore(store_id='%s', product_store_id='%s')>" % (
            self.store_id,
            self.product_store_id,
        )


# Details about favorite table to which is mapping
class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    product_substitut_id = Column(Integer)

    def __repr__(self):
        return "<Favorite(product_id='%s', product_substitut_id='%s')>" % (
            self.product_id,
            self.product_substitut_id,
        )
