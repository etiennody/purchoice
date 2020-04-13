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
        self.db.add_category(self.category)
        products = self.get_off()
        for product in products:
            self.db.add_product(product)
            self.db.add_brand(product.get("brands"))
            self.db.add_store(product.get("stores"))


def main():
    reset = PurchoiceDatabase()
    reset.truncate_tables()
    for category in CATEGORY_SELECTED:
        import_off = ImportOff(category)
        import_off.import_by_category()
        continue


if __name__ == "__main__":
    main()
