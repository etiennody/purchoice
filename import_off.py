#! usr/bin/python3
# code: utf-8

"""Download data from Open Food Facts API."""

import requests
import json

from constants import CATEGORY_SELECTED
from purchoice_database import PurchoiceDatabase


class ImportOff:
    """ImportOff class download all the data from OpenFood Facts API"""

    def __init__(self, category):
        self.url = "https://fr.openfoodfacts.org//cgi/search.pl?"
        self.params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "sort_by": "unique_scans_n",
            "page_size": 500,
            "json": 1,
        }
        self.db = PurchoiceDatabase()
        self.category = category

    def get_off(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            return json.loads(response.content)["products"]

    def import_by_category(self):

        products = self.get_off()
        try:
            for cat_instances in self.category.split(","):
                self.db.add_category(cat_instances)
                for product in products:
                    for store_instances in product.get("stores").split(","):
                        self.db.add_store(store_instances)
                    for brand_instances in product.get("brands").split(","):
                        self.db.add_brand(brand_instances)
                    self.db.add_product(product)
            self.db.add_category_by_product(product)

        except Exception:
            pass


if __name__ == "__main__":
    reset = PurchoiceDatabase()
    reset.truncate_tables()
    for category in CATEGORY_SELECTED:
        import_off = ImportOff(category)
        import_off.import_by_category()
