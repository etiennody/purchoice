#! usr/bin/python3
# coding: utf-8

# from constants import CATEGORY_SELECTED
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

    # def list_options(self, slct_choice, list_options):
    #     """
    #     list_options method manage the inputs
    #     where user can select to navigate in the apllication.
    #     Only integer are accepted.
    #     """
    #     inpt = input(slct_choice)
    #     while True:
    #         try:
    #             inpt = int(inpt)
    #             if inpt in list_options:
    #                 return inpt
    #             else:
    #                 print("\n Désolé, vous devez entrer un chiffre.")
    #         except ValueError:
    #             print("\n Désolé, vous devez entrer un chiffre.")
    #         break

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
        # for category in categories:
        #     print(f"{category.category_id} - {category.name_label}")
        index_category = []
        categories = self.db.get_categories()
        for i, category in enumerate(categories):
            print("\n", i+1, f"- {category.name_label}")
            index_category.append(str(i))
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
            self.controller.page = "list_products"
            self.controller.choice = choice

    # def show_category(self, category):

    #     print(
    #         f"Nom du produit: {product.product_name} \
    #         Marque : {product.brands}"
    #     )
    #     print("\n 'a' pour la Page d'accueil")
    #     print("\n 'q' pour Quitter")
    #     choice = input("Selectionnez votre choix: ")
    #     if choice == "q":
    #         self.controller.run_app = False
    #     elif choice == "a":
    #         self.controller.page = "homepage"

    def list_products(self, products):
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

    def show_product(self, product, stores, brands):
        print(
            f"Nom du produit: {product.product_name} \
            Marque : {product.brands}"
        )
        print(f"Description: {product.generic_name}")
        print(f"Lien page web: {product.url}")
        print(f"Magasin: {product.store}")
        print("-------------------------------------------")
        print(f"NutriScore: {product.nutrition_grade_fr}")
        print(f"Ingredients: {product.ingredients_text_fr}")
        print(f"Nombre d'additifs: {product.additives_n}")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")
        choice = input("Selectionnez votre choix: ")
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a":
            self.controller.page = "homepage"

    def search_product(self):
        self.controller.page = "search_results"
        self.controller.choice = input(
            "\n *** Entrer le nom du produit recherché: "
        )

    def saved_products(self):
        print("Page de sauvegarde de produits en cours de construction")
