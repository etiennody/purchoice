#! usr/bin/python3
# coding: utf-8

import os

from src.purchoice.purchoice_database import PurchoiceDatabase


class AppView:
    """class AppView provide a means of bundling data and functionality
    for the visual appearance of Purchoice application.
    """
    def __init__(self, controller):
        self.controller = controller
        self.db = PurchoiceDatabase()

    def clear_screen(self):
        """clear_screen method is a cross platform way
        to clear the terminal for Unix/Linux and Windows/Dos.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def homepage(self):
        """homepage method displays the main menu of the application.
        """
        print(
            "\n --PURCHOICE-- Trouvez une alternative saine à votre produit !"
            )
        print("\n 1 - Quel aliment souhaitez-vous remplacer ?")
        print("\n 2 - Retrouvez mes aliments substitués")
        print("\n 3 - Quitter le programme")

        choice = input(
            "\n Veuillez sélectionner votre choix (entre 1 et 3) "
            "et valider avec 'Entrée': "
        )
        if choice == "3":
            self.controller.run_app = False
        if choice == "1":
            self.controller.page = "list_categories"
        if choice == "2":
            self.controller.page = "list_favorites"

    def list_categories(self, categories):
        """list_categories method displays a list of categories.

        Arguments:
            categories {list} -- a list of categories from Category table.
        """
        print("\n VOICI UNE LISTE DE CATEGORIE D'ALIMENTS A SELECTIONNER :")
        print("\n --------------------------------")
        for category in categories:
            print(f"{category.category_id} - {category.category_name}")
        print("\n --------------------------------")
        print("\n Tapez 'a' pour la Page d'accueil")
        print("\n Tapez 'q' pour Quitter")
        choice = input(
            "\n Entrez un identifiant (entre 1 et 645) correspondant "
            "à une catégorie et valider avec 'Entrée' : "
        )
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a":
            self.controller.page = "homepage"
        elif choice.isnumeric():
            self.controller.page = "list_products_by_category"
            self.controller.choice = choice

    def list_products_by_category(self, products):
        """list_products_by_category method displays
        a list of products by categories.

        Arguments:
            products {list} -- a list from Product table.
        """
        print("\n VOICI UNE LISTE DE PRODUITS A SELECTIONNER :")
        print("\n --------------------------------")
        for product in products:
            print("\n", f" {product.product_id} - {product.product_name}")
        print("\n --------------------------------")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")
        choice = input(
            "\n Entrez un identifiant correspondant "
            "à un produit et valider avec 'Entrée' : "
        )
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a":
            self.controller.page = "homepage"
        elif choice.isnumeric():
            self.controller.page = "show_product"
            self.controller.choice = choice

    def show_product(self, product, substitute, is_saved):
        """show_product method displays a product
        selected by the user with the product id.

        Arguments:
            product {instance} -- a product selected.
            substitute {instance} -- a suggested substitute.
            is_saved {bool} -- state of the substitute.
        """
        print("\n VOICI VOTRE PRODUIT :")
        self.print_product(product)
        if substitute:
            print("\n VOICI VOTRE SUBSTITUT :")
            self.print_product(substitute)
        else:
            print(
                "\n Malheureusement, nous n'avons aucun substituts "
                "à vous proposer..."
            )
        print("\n --------------------------------")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")
        if not is_saved:
            choice = input(
                "\n Voulez-vous sauvegarder votre substitut ? "
                "[o/n] "
            )
            if choice == "o":
                self.controller.page = "save_substitute"
                self.controller.choice = (product, substitute)
            if choice == "n":
                self.controller.page = "homepage"
        else:
            print(
                "\n Votre substitut est déjà sauvegardé "
                "dans votre liste de produits recherchés."
            )
            print("\n Retournez à la Page d'accueil et tapez '2'.")
            choice = input(
                "\n Allez à la Page d'accueil 'a' "
                "ou Quitter 'q' : "
            )
        if choice == "q":
            self.controller.run_app = False
        elif choice == "a" or choice == "n":
            self.controller.page = "homepage"

    def print_product(self, product):
        """print_product method displays details of a product.

        Arguments:
            product {instance} -- a product selected.
        """
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

    def list_favorites(self, favorites):
        """list_favorites method displays
        a list of saved substitutes by products.

        Arguments:
            favorites {list} -- a list of saved products
            with their substitutes.
        """
        print("\n VOICI LA LISTE DES ALIMENTS SUBSTITUES :")
        print("\n --------------------------------")
        if not favorites:
            print(
                "\n La liste des aliments substitués est vide. "
                "Veuillez d'abord effectuer une recherche "
                "et sauvegardez le résultat."
            )
        else:
            for fav in favorites:
                print(fav)
        print("\n --------------------------------")
        print("\n 'a' pour la Page d'accueil")
        print("\n 'q' pour Quitter")
        choice = input(
            "\n Tapez 'a' pour la Page d'accueil ou 'q' pour quitter : "
        )
        if choice == "q":
            self.controller.run_app = False
        if choice == "a":
            self.controller.page = "homepage"
