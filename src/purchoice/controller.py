#! usr/bin/python3
# coding: utf-8

import sys

from src.purchoice.purchoice_database import PurchoiceDatabase
from src.purchoice.views import AppView


class Controller:
    """Controller class centralizes the main commands
    and functionalities of the Purchoice application.
    """
    def __init__(self):
        try:
            self.db = PurchoiceDatabase()
            self.view = AppView(self)
            self.run_app = True
            self.page = "homepage"
            self.choice = None
        except Exception:
            print(
                "Erreur d'accès à la base données. "
                "Veuillez vérifier votre système de configuration."
            )
            sys.exit()

    def run(self):
        """Run method is the main loop of the application.
        """
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
                substitute = self.db.get_substitute_for_product(self.choice)
                is_saved = True
                if not substitute:
                    is_saved = False
                    substitute = self.db.get_healthy_products(product)
                self.view.show_product(product, substitute, is_saved)
            elif self.page == "save_substitute":
                self.db.save_substitute(product, substitute)
                self.page = "homepage"
            elif self.page == "list_favorites":
                favorites = self.db.get_favorites()
                self.view.list_favorites(favorites)
            else:
                print("Oops ! Page introuvée...")
                self.run_app = False
