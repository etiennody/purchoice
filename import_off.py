#! usr/bin/python3
# code: utf-8

"""Download data from Open Food Facts API."""

import json

import requests

from src.purchoice.constants import CATEGORY_SELECTED
from src.purchoice.purchoice_database import PurchoiceDatabase


class ImportOff:
    """ImportOff class downloads data from Open Food Facts API."""
    def __init__(self, db):
        self.url = "https://fr.openfoodfacts.org//cgi/search.pl?"
        self.db = db

    def get_url_params(self, category):
        """get_urls_params helps to define more precisely
        the request to Open Food Facts API.

        Arguments:
            category {string} -- a name of category.

        Returns:
            dictionnary -- contains parameters to complete
            the request to Open Food Facts API.
        """
        return {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "sort_by": "unique_scans_n",
            "page_size": 500,
            "json": 1,
        }

    def get_off(self, category):
        """get_off method makes a request to the web page of Open Food Facts,
        and load data in json if the return status code is successful.

        Arguments:
            category {string} -- a category name.

        Returns:
            dictionnary -- Deserialize an bytearray instance containing
            a JSON document to a Python object as early as products.
        """
        response = requests.get(self.url, params=self.get_url_params(category))
        if response.status_code == 200:
            return json.loads(response.content)["products"]

    def import_by_category(self, category):
        """import_by_category method try to insert
        products, categories, brands and stores data
        for each product by category in the database.

        Arguments:
            category {string} -- a category name.
        """
        products = self.get_off(category)
        products = products if isinstance(products, list) else products.items()

        print("Importation des données en cours. Patientez...")

        for product in products:
            try:
                p = self.db.add_product(product)
                for category in product.get("categories").split(","):
                    c = self.db.add_category(category)
                    p.categories.append(c)
                for brand in product.get("brands").split(","):
                    b = self.db.add_brand(brand)
                    p.brands.append(b)
                for store in product.get("stores").split(","):
                    s = self.db.add_store(store)
                    p.stores.append(s)
            except Exception:
                pass


if __name__ == "__main__":
    db = PurchoiceDatabase()
    db.truncate_tables()
    import_off = ImportOff(db)
    for category in CATEGORY_SELECTED:
        import_off.import_by_category(category)
    print("Merci d'avoir patienté. Vous pouvez lancer l'application !")
