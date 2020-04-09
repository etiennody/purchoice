#! usr/bin/python3
# code: utf-8

"""Download data from Open Food Facts API."""

import requests
import json

from build_database import BuildDatabase


class ImportOff:
    """ImportOff class download all the data from OpenFood Facts API"""

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org//cgi/search.pl?"
        self.params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": "desserts_de_riz",
            "json": 1,
        }
        self.db = BuildDatabase()

    def get_off(self):
        self.r = requests.get(self.url, params=self.params)

    def transform_data(self):
        """Transform the json file in dict."""
        self.data = json.loads(self.r)

    def _gen_product(self):
        for item in self.data["products"]:
            self.product_name = item["product_name_fr"]
            self.generic_name = item["generic_name"]
            self.url = item["url"]
            self.nutrition_grade_fr = item["nutrition_grade_fr"]
            self.ingredients_text_with_allergens = item[
                "ingredients_text_with_allergens"
            ]
            self.traces = item["traces"]
            self.additives_n = item["additives_n"]
            self.ingredients_from_palm_oil_n = item[
                "ingredients_from_palm_oil_n"
            ]

    def _gen_store(self):
        for item in self.data["products"]:
            self.store_name = item["stores"]

    def _gen_category(self):
        for item in self.data["products"]:
            self.category_name = item["categories"]

    def _gen_brand(self):
        for item in self.data["products"]:
            self.brand_name = item["brands"]

    def import_products(self):
        self.products = list(self._gen_product())
        self.db.add_product(self.products)

    def import_categories(self):
        self.categories = list(self._gen_category())
        self.db.add_category(self.categories)

    def import_brands(self):
        self.brands = list(self._gen_brand())
        self.db.add_brand(self.brands)

    def import_stores(self):
        self.stores = list(self._gen_store)
        self.db.add_store(self.stores)

    def import_by_category(self):
        self.get_off()
        self.transform_data()
        self.import_brands()
        self.import_categories()
        self.import_products()
        self.import_stores()


def main(self):
    self.db.truncate_tables()
    self.import_off = ImportOff()
    self.import_off(self.import_by_category)


if __name__ == "__main__":
    main(self=main)
