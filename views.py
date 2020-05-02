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

        choice = input(
            "\n Veuillez sélectionner votre choix (entre 1 et 3) et valider avec 'Entrée': "
        )
        if choice == "3":
            self.controller.run_app = False
        if choice == "1":
            self.controller.page = "list_categories"
        if choice == "2":
            self.controller.page = "saved_products"

    def list_categories(self, categories):
        """list_categories method displays a list of categories."""
        print("\n VOICI UNE LISTE DE CATEGORIE D'ALIMENTS A SELECTIONNER :")
        print("\n --------------------------------")
        for category in categories:
            print("\n", f"{category.category_id} - {category.category_name}")
        print("\n --------------------------------")
        print("\n Tapez 'a' pour la Page d'accueil")
        print("\n Tapez 'q' pour Quitter")
        choice = input(
            "\n Entrez un identifiant (entre 0 et 3000) correspondant à une catégorie et valider avec 'Entrée' : "
        )
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a":
            self.controller.page = "homepage"
        else:
            self.controller.page = "list_products_by_category"
            self.controller.choice = choice

    def list_products_by_category(self, products):
        """
        list_products_by_category method displays
        a list of products by categories.
        """
        print("\n VOICI UNE LISTE DE PRODUITS A SELECTIONNER :")
        print("\n --------------------------------")
        for product in products:
            print("\n", f" {product.product_id} - {product.product_name}")
        print("\n --------------------------------")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")
        choice = input(
            "\n Entrez un identifiant (entre 0 et 3000) correspondant à un produit et valider avec 'Entrée' : "
        )
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a":
            self.controller.page = "homepage"
        else:
            self.controller.page = "show_product"
            self.controller.choice = choice

    def show_product(self, product, substitute, is_saved):
        """
        show_product method displays a product
        selected by the user with the product id.
        """
        print("\n VOICI VOTRE PRODUIT :")
        self.print_product(product)
        if substitute:
            print("\n VOICI VOTRE SUBSTITUT :")
            self.print_product(substitute)
        else:
            print("\n Malheureusement, nous n'avons aucun substituts à vous proposer...")
        print("\n --------------------------------")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")
        if not is_saved:
            choice = input("\n Voulez-vous sauvegarder votre substitut ? [o/n] ")
            if choice == "o":
                self.controller.page = "save_substitute"
                self.controller.choice = (product, substitute)
            if choice == "n":
                self.controller.page = "homepage"
        else:
            print("\n Votre substitut est déjà sauvegardé dans votre liste de produits recherchés.")
            print("\n Retournez à la Page d'accueil et tapez '2'.")
            choice = input("\n Allez à la Page d'accueil 'a' ou Quitter 'q' : ")
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a" or choice == "n":
            self.controller.page = "homepage"

    def print_product(self, product):
        brands = ", ".join([str(b) for b in product.brands])
        stores = ", ".join([str(s) for s in product.stores])
        print(" --------------------------------")
        print(
            f"\n Nom du produit : {product.product_name} \
            Marque : {brands}"
        )
        print(f" Description : {product.generic_name}")
        print(f" Lien page web : {product.url}")
        print(f" Magasin : {stores}")
        print(" - - - - - - - - - - - - - - - - - - - - - -")
        print(f" NutriScore : {product.nutrition_grade_fr}")
        print(f" Ingredients : {product.ingredients_text_fr}")
        print(f" Nombre d'additifs : {product.additives_n}")

    # def list_favorites(self, favorites):
    #     """list_products_by_category method displays a list of products by categories."""
    #     for fav in favorites:
    #         print(fav)
