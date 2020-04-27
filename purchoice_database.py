#! usr/bin/python3
# coding: utf-8

from models import Base
from models import Category, Store, Brand, Product
from os import environ
from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
# from constants import CATEGORY_SELECTED
# from sqlalchemy.sql import exists, func


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

    def get_or_create(self, model, **kwargs):
        """
        get_or_create method is for looking up an object,
        giving a set of parameters, creating one if necessary.
        """
        instance = self.session.query(model).filter_by(**kwargs).first()

        if not instance:
            instance = model(**kwargs)
            self.session.add(instance)

        return instance

    def truncate_tables(self):
        """
        Delete all the records in the tables
        so that we can start later from a clean database
        """
        self.session.query(Category).delete()
        self.session.query(Store).delete()
        self.session.query(Brand).delete()
        self.session.query(Product).delete()
        self.session.commit()

    def get_all_products(self):
        """This method can access all products object from database
        In this way, we can extract only 10 products randomly
        """
        return self.session.query(Product).join(Category.category_name).all()

    def get_healthy_products(self):
        """Extract products object from database
        We found healthy products where nutrition grade is upper than B
        """
        return self.session.query(Product). \
            filter(Product.nutrition_grade_fr == "a"). \
            filter(Product.additives_n == 0). \
            order_by(desc(Product.nutrition_grade_fr)). \
            order_by(asc(Product.additives_n)).limit(15)

    def add_product(self, product_dict):
        """Insert product and commit the record in database"""
        product = Product(
            product_name=product_dict.get("product_name"),
            generic_name=product_dict.get("generic_name"),
            url=product_dict.get("url"),
            nutrition_grade_fr=product_dict.get("nutrition_grade_fr"),
            ingredients_text_fr=product_dict.get("ingredients_text"),
            additives_n=product_dict.get("additives_n")
            )
        self.session.add(product)
        self.session.commit()
        return product

    def get_categories(self):
        """Extract a list of categories object"""
        return self.session.query(Category).limit(10)

    def get_product_by_category(self, category_id):
        category = self.session.query(Category). \
            filter(Category.category_id == category_id).one()
        return category.products

    def add_category(self, category):
        """Insert category and commit the record in database"""
        c = self.get_or_create(
            Category,
            category_name=category.strip().upper()
            )
        self.session.commit()
        return c

    def get_brands(self):
        """Extract brand object"""
        return self.session.query(Brand).all()

    def add_brand(self, brands):
        """Insert brand and commit the record in database"""
        b = self.get_or_create(
            Brand,
            brand_name=brands
        )
        self.session.commit()
        return b

    def get_stores(self):
        """Extract store object"""
        return self.session.query(Store).all()

    def add_store(self, stores):
        """Insert store and commit the record in database"""
        s = self.get_or_create(
            Store,
            store_name=stores.strip().upper()
        )
        self.session.commit()
        return s

    # def saved_products(self):
    #     """saved_prducts method store alternatives products"""
    #     print(
    #         "Page de sauvegarde des substituts en cours de construction"
    #     )
