#! usr/bin/python3
# coding: utf-8

from models import Base, Category, Store, Brand, Product, ProductStore, Favorite
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Script shell python to create database with mysql and its user
# os.system("mysql -u ${PURCHOICE_DBUSER} -p < purchoice_db.sql")


class BuildDatabase:
    """
    Class to manage and communicate with the database.
    It use connexion, insert, select, delete statement.
    """

    def __init__(self):
        self._db_url = environ.get("PURCHOICE_DBURL")
        self.session = self._create_session()

    def _create_session(self):
        self.engine = create_engine(self._db_url, echo=True)
        Base.metadata.create_all(self.engine)
        self.create_session = sessionmaker(bind=self.engine)
        return self.create_session()

    def truncate_tables(self):
        self.session.query(Category).delete()
        self.session.query(Store).delete()
        self.session.query(Brand).delete()
        self.session.query(Product).delete()
        self.session.query(ProductStore).delete()
        self.session.query(Favorite).delete()
        self.session.commit()

    def add_product(self, products):
        for pr in products:
            self.session.add(
                Product(
                    product_name=pr.product_name,
                    generic_name=pr.generic_name,
                    url=pr.url,
                    nutrition_grade_fr=pr.nutrition_grade_fr,
                    ingredients_text_with_allergens=pr.ingredients_text_with_allergens,
                    traces=pr.traces,
                    additives=pr.additives,
                    ingredients_from_palm_oil_n=pr.ingredients_from_palm_oil_n,
                )
            )
        self.session.commit()

    def add_category(self, categories):
        for cat in categories:
            self.session.add(Category(category_name=cat.category_name))
        self.session.commit()

    def add_brand(self, brands):
        for br in brands:
            self.session.add(Brand(brand_name=br.brand_name))
        self.session.commit()
