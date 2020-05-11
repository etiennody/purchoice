#! usr/bin/python3
# coding: utf-8

from os import environ

from sqlalchemy import create_engine, literal, or_
from sqlalchemy.orm import sessionmaker

from src.purchoice.models import (Base, Brand, Category, Favorite, Product,
                                  Store, cat_prod_asso)


class PurchoiceDatabase:
    """PurchoiceDatabase Class manages and communicates with the database.
    It uses connexion, insert, select, delete sql statements.
    """
    def __init__(self):
        self._db_url = environ.get("PURCHOICE_DBURL")
        self.session = self._create_session()

    def _create_session(self):
        """This method a SQLAlchemy Engine that will interact with the database,
        a SQLAlchemy ORM session factory bound to this engine,
        and a base class from models definitions.

        Returns:
            sqlalchemy.orm.session.Session
            -- a new Session objects when called,
            creating them given the configurational arguments established here.
        """
        self.engine = create_engine(self._db_url, echo=False)
        # create all tables
        Base.metadata.create_all(self.engine)
        # create a Session
        self.create_session = sessionmaker(bind=self.engine, autoflush=False)
        return self.create_session()

    def get_or_create(self, model, **kwargs):
        """get_or_create method is for looking up an object,
        giving a set of parameters, creating one if necessary.

        Arguments:
            model {string} -- a table name to set.

        Returns:
            tuple -- a tuple of (object, created),
            where object is the retrieved or created object and
            created is a boolean specifying whether a new object was created.
        """
        instance = self.session.query(model).filter_by(**kwargs).first()
        if not instance:
            instance = model(**kwargs)
            self.session.add(instance)
        return instance

    def truncate_tables(self):
        """Delete all the records in the selected tables
        so that we can start later from a clean database.
        """
        self.session.query(Category).delete()
        self.session.query(Store).delete()
        self.session.query(Brand).delete()
        self.session.query(Product).delete()
        self.session.commit()

    def get_healthy_products(self, product):
        """Extract products object from database.
        We found healthy products where nutrition grade is higher than
        the searched product and where the number of additives is beneath too.

        Arguments:
            product {instance} -- refer to the Product model.

        Returns:
            src.purchoice.models.Product -- the first result of
            the Query or None if the result doesn’t contain any row.
        """
        category_ids = [c.category_id for c in product.categories]
        substitute = self.session.query(Product). \
            join(cat_prod_asso). \
            filter(cat_prod_asso.c.category_id.in_(category_ids)).\
            filter(Product.product_id != product.product_id). \
            filter(or_(
                Product.nutrition_grade_fr < product.nutrition_grade_fr,
                Product.additives_n < product.additives_n)). \
            order_by(Product.nutrition_grade_fr). \
            order_by(Product.additives_n)
        return substitute.first()

    def get_substitute_for_product(self, product_id):
        """Extract a substituted product from Favorite table.

        Arguments:
            product_id {integer} -- the product id of the substitute
            in Favorite model.

        Returns:
            instance -- get the substituted food when it has been saved.
        """
        substituted = self.session.query(literal(True)). \
            filter(Favorite.product_id == product_id)
        if substituted is None:
            return substituted

    def get_product_by_id(self, product_id):
        """Extract a food with its id.

        Arguments:
            product_id {integer} -- product id of the Product model.

        Returns:
            src.purchoice.models.Product -- product with a correct product id.
        """
        product = self.session.query(Product). \
            filter(Product.product_id == product_id).one()
        return product

    def add_product(self, product_dict):
        """Insert product and commit the record in database.

        Arguments:
            product_dict {dictionnary} -- keys and values of the products.

        Returns:
            instance -- a product with its all required arguments
            (product_name, generic_name, url, nutrition_grade_fr
            ingredients_text_fr, addidtives_n).
            Its state will be persisted to the database
            on the next flush operation.
        """
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
        """Extract a list of categories object.

        Returns:
            list -- contain category name and category id from the database.
        """
        return self.session.query(Category).all()

    def get_product_by_category(self, category_id):
        """Extract products from the list of category id selected.

        Arguments:
            category_id {integer} -- a category id from Category table.

        Returns:
            sqlalchemy.orm.dynamic.AppenderQuery
            -- A dynamic query on the category table that supports basic
            collection storage operations with products.
        """
        category = self.session.query(Category). \
            filter(Category.category_id == category_id).one()
        return category.products

    def add_category(self, category):
        """Insert category and commit the record in database

        Arguments:
            category {string} -- a category name.

        Returns:
            instance -- a category with its all required arguments
            with its category name.
            Its state will be persisted to the database
            on the next flush operation.
        """
        c = self.get_or_create(
            Category,
            category_name=category.strip().upper()
        )
        self.session.commit()
        return c

    def add_brand(self, brands):
        """Insert brand and commit the record in database

        Arguments:
            brands {string} -- a brand name.

        Returns:
            instance -- a brand with its all required arguments
            with its brand_name.
            Its state will be persisted to the database
            on the next flush operation.
        """
        b = self.get_or_create(
            Brand,
            brand_name=brands
        )
        self.session.commit()
        return b

    def add_store(self, stores):
        """Insert store and commit the record in database

        Arguments:
            stores {string} -- a store name.

        Returns:
            instance -- a store with its all required arguments
            with its store_name.
            Its state will be persisted to the database
            on the next flush operation.
        """
        s = self.get_or_create(
            Store,
            store_name=stores.strip().upper()
        )
        self.session.commit()
        return s

    def save_substitute(self, product, substitute):
        """Insert product_id and product_substitute_id
        and commit the record in database.

        Arguments:
            product {src.purchoice.models.Product}
            -- an instance of the selected product.
            substitute {src.purchoice.models.Product}
            -- an instance of the selected product as substitute.

        Returns:
            instance -- place the favorite object in Session.
            Its state will be persisted to the database
            on the next flush operation.
        """
        fav = Favorite(
            product_id=product.product_id,
            product_substitute_id=substitute.product_id
        )
        self.session.add(fav)
        self.session.commit()
        return fav

    def get_favorites(self):
        """get_favorites method extract a list of the Favorite table.

        Returns:
            list -- with favorite_id, product_id, product_substitute_id.
        """
        favorites = self.session.query(Favorite).all()
        return favorites
