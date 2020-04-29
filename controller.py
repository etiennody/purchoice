#! usr/bin/python3
# coding: utf-8

import sys

from views import AppView
from purchoice_database import PurchoiceDatabase


class Controller:

    def __init__(self):
        try:
            self.db = PurchoiceDatabase()
            self.view = AppView(self)
            self.run_app = True
            self.page = "homepage"
            self.choice = None
        except Exception:
            print(
                "Erreur d'accès à la base données. \
            Veuillez vérifier votre système de configuration."
            )
            sys.exit()

    def run(self):
        self.view.clear_screen()
        while self.run_app:
            self.view.clear_screen()
            if self.page == "homepage":
                self.view.homepage()
            elif self.page == "list_categories":
                self.view.list_categories(self.db.get_categories())
            elif self.page == "list_products_by_category":
                products = self.db.get_product_by_category(
                    category_id=self.choice
                )
                self.view.list_products_by_category(products)
            elif self.page == "show_product":
                product = self.db.get_product_by_id(product_id=self.choice)
                self.view.show_product(product)
