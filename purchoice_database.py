#! usr/bin/python3
# coding: utf-8

from models import Base
from models import Category, Store, Brand, Product, ProductStore
from os import environ
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker


class PurchoiceDatabase:
    """
    PurchoiceDatabase Class manages and communicates with the database.
    It uses connexion, insert, select, delete sql statements.
    """

    def __init__(self):
        self._db_url = environ.get("PURCHOICE_DBURL")
        self.session = self._create_session()

    def _create_session(self):
        """
        This method a SQLAlchemy Engine that will interact with the database,
        a SQLAlchemy ORM session factory bound to this engine,
        and a base class from models definitions.
        """
        self.engine = create_engine(self._db_url, echo=False)
        # create all tables
        Base.metadata.create_all(self.engine)
        # create a Session
        self.create_session = sessionmaker(bind=self.engine)
        return self.create_session()

    def truncate_tables(self):
        """
        Delete all the records in the tables
        so that we can start later from a clean database
        """
        self.session.query(Category).delete()
        self.session.query(Store).delete()
        self.session.query(Brand).delete()
        self.session.query(Product).delete()
        self.session.query(ProductStore).delete()
        self.session.commit()

    def get_products(self):
        """This method can access all products object from database
        In this way, we can extract only 10 products randomly
        """
        return self.session.query(Product).limit(10)

    def get_healthy_products(self):
        """Extract products object from database
        We found healthy products where nutrtion grade is upper than B
        """
        return self.session.query(Product). \
            filter(Product.nutrition_grade_fr <= "b"). \
            order_by(desc(
                (Product.nutrition_grade_fr) and (Product.additives_n)
                )
            ). \
            limit(10)

    def add_product(self, product):
        """Insert product and commit the record in database"""
        self.session.add(
            Product(
                product_name=product.get("product_name"),
                generic_name=product.get("generic_name"),
                url=product.get("url"),
                nutrition_grade_fr=product.get("nutrition_grade_fr"),
                ingredients_text_fr=product.get("ingredients_text"),
                additives_n=product.get("additives_n"),
            )
        )
        self.session.commit()

    def get_categories(self):
        """Extract category object"""
        return self.session.query(Category).all()

    def add_category(self, category):
        """Insert category and commit the record in database"""
        self.session.add(Category(category_name=category))
        self.session.commit()

    def get_brands(self):
        """Extract brand object"""
        return self.session.query(Brand).all()

    def add_brand(self, brands):
        """Insert brand and commit the record in database"""
        self.session.add(Brand(brand_name=brands))
        self.session.commit()

    def get_stores(self):
        """Extract store object"""
        return self.session.query(Store).all()

    def add_store(self, stores):
        """Insert store and commit the record in database"""
        self.session.add(Store(store_name=stores))
        self.session.commit()
