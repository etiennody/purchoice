#! usr/bin/python3
# coding: utf-8

from purchoice_database import PurchoiceDatabase

import os


class AppView:

    def __init__(self, controller):
        self.controller = controller
        self.db = PurchoiceDatabase()

    def clear_screen(self):
        """clear_screen method is a cross platform way
        to clear the terminal for Unix/Linux and Windows/Dos.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def homepage(self):
        """homepage method displays the main menu of the application."""
        print(
            "\n --PURCHOICE-- Trouvez une alternative saine à votre produit !"
        )
        print("\n 1 - Quel aliment souhaitez-vous remplacer ?")
        print("\n 2 - Retrouvez mes aliments substitués")
        print("\n 3 - Quitter le programme")

        choice = input("\n Veuillez sélectionner votre choix: ")
        if choice == "3":
            self.controller.run_app = False
        if choice == "1":
            self.controller.page = "list_categories"
        if choice == "2":
            self.controller.page = "saved_products"

    def list_categories(self, categories):
        """list_categories method displays a list of categories."""
        for category in categories:
            print("\n", f"{category.category_id} - {category.category_name}")

        print("\n --------------------------------")
        print("\n Tapez 'a' pour la Page d'accueil")
        print("\n Tapez 'q' pour Quitter")
        choice = input(
            "\n *** Entrez un chiffre correspondant à une catégorie: "
        )
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a":
            self.controller.page = "homepage"
        else:
            self.controller.page = "list_products_by_category"
            self.controller.choice = choice

    def list_products_by_category(self, products):
        """list_products_by_category method displays a list of products by categories."""
        for product in products:
            print(f"{product.product_id} - {product.product_name}")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")

        choice = input("\n *** Entrez un chiffre correspondant à un produit: ")
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a":
            self.controller.page = "homepage"
        else:
            self.controller.page = "show_product"
            self.controller.choice = choice

    def show_product(self, product):
        """show_product method displays a product selected by the user with the product id."""
        for prd in product:
            print(f"Nom du produit : {prd.product_name} \
                Marque : {prd.brands}")
            print(f"Description : {prd.generic_name}")
            print(f"Lien page web : {prd.url}")
            print(f"Magasin : {prd.stores}")
            print("----------------------------------------------------")
            print(f"NutriScore : {prd.nutrition_grade_fr}")
            print(f"Ingredients : {prd.ingredients_text_fr}")
            print(f"Nombre d'additifs : {prd.additives_n}")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")
        choice = input("\n Voulez-vous un substitut à ce produit ? [o/n] ")
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a" or choice == "n":
            self.controller.page = "homepage"
        else:
            self.controller.page = "show_substitut"
            self.choice = choice
