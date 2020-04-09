#! usr/bin/python3
# coding: utf-8

from models import Base
from models import Category, Store, Brand, Product, ProductStore
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Script shell python to create database with mysql and its user
# os.system("mysql -u ${PURCHOICE_DBUSER} -p < purchoice_db.sql")


class BuildDatabase:
    """
    BuildDatabase Class manages and communicates with the database.
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
        self.engine = create_engine(self._db_url, echo=True)
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

    def get_product(self):
        """Extract product object"""
        return self.session.query(Product)

    def add_product(self, products):
        """Insert product and commit the record in database"""
        for pr in products:
            self.session.add(
                Product(
                    product_name=pr.product_name,
                    generic_name=pr.generic_name,
                    url=pr.url,
                    nutrition_grade_fr=pr.nutrition_grade_fr,
                    ingredients_text_with_allergens=pr.ingredients_text_with_allergens,
                    traces=pr.traces,
                    additives_n=pr.additives_n,
                    ingredients_from_palm_oil_n=pr.ingredients_from_palm_oil_n,
                )
            )
        self.session.commit()

    def get_category(self):
        """Extract category object"""
        return self.session.query(Category).all()

    def add_category(self, categories):
        """Insert category and commit the record in database"""
        for cat in categories:
            self.session.add(Category(category_name=cat.category_name))
        self.session.commit()

    def get_brand(self):
        """Extract brand object"""
        return self.session.query(Brand).all()

    def add_brand(self, brands):
        """Insert brand and commit the record in database"""
        for br in brands:
            self.session.add(Brand(brand_name=br.brand_name))
        self.session.commit()

    def get_store(self):
        """Extract store object"""
        return self.session.query(Store).all()

    def add_store(self, stores):
        """Insert store and commit the record in database"""
        for st in stores:
            self.session.add(Store(store_name=st.store_name))
        self.session.commit()
