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
            elif self.page == "list_products":
                self.view.list_products(self.db.get_healthy_products())
            elif self.page == "show_product":
                product = get_product_by_id(self.choice)
                self.view.show_product(product)
            # elif self.page == "search":
            #     self.view.search_product()
            # elif self.page == "search_results":
            #     results = search_products(self.choice)
            #     self.view.list_products(results)


# from purchoice_database import PurchoiceDatabase


# class Purchoice:
#     """The Purchoice class is the main class to manage the application."""

#     def __init__(self):
#         """First, we verify if it's possible to connect with the database"""
#         try:
#             self.database = PurchoiceDatabase()
#         except Exception:
#             print(
#                 "Erreur d'accès à la base données. \
#             Veuillez vérifier votre système de configuration."
#             )
#             sys.exit()

#     def display_home(self):
#         """display_home method displays the main menu of the application"""
#         print("\n 1 - Quel aliment souhaitez-vous remplacer ?")
#         print("\n 2 - Quitter le programme")

#     def list_options(self, slct_choice, list_options):
#         """
#         list_options method manage the inputs
#         where user can select to navigate in the apllication.
#         Only integer are accepted.
#         """
#         inpt = input(slct_choice)
#         while True:
#             try:
#                 inpt = int(inpt)
#                 if inpt in list_options:
#                     return inpt
#                 else:
#                     print("\n Désolé, vous devez entrer un chiffre.")
#                     return inpt
#             except ValueError as v:
#                 print(v)

#     def exit_aplication(self):
#         while True:
#             inpt = input(
#                 "\n Revenir au menu principale "h" ou Quitter le programme "q""
#             ).lower()
#             if inpt == "o":
#                 self.clear_screen()
#                 self.display_home()
#             elif inpt == "q":
#                 self.clear_screen()
#                 print("A bientôt !")
#                 sys.exit()
#             else:
#                 print("\n Vous devez entrer (o/O) ou (q/Q)")

#     def clear_screen(self):
#         """clear_screen method is a cross platform way
#         to clear the terminal for Unix/Linux and Windows/Dos.
#         """
#         os.system("cls" if os.name == "nt" else "clear")

#     def choose_category(self):
#         pass

#     def choose_products(self):
#         return self.database.get_healthy_products()

#     def save_product(self):
#         pass


# def main():
#     """
#     The main method in this app.py
#     launch the main loop for Purchoice application.
#     """
#     # Display the bar title
#     print(
#         "\n --Purchoice-- Trouvez une alternative saine à votre produit !"
#     )
#     # Connect to the database and launch the main menu
#     purchoice = Purchoice()
#     purchoice.display_home()
#     run_app = True

#     while run_app:
#         list_options = [1, 2]
#         inpt = purchoice.list_options(
#             "\n Veuillez sélectionner votre choix:", list_options
#         )

#         if inpt == 2:
#             purchoice.clear_screen()
#             purchoice.exit_aplication()
#             run_app = False

#         elif inpt == 1:
#             products = purchoice.choose_products()

#             print("\n")
#             index_product = []
#             # Print the 10th products with nutrition grade higher
#             for i, product in enumerate(products):
#                 print(i+1, "-", product.product_name)
#                 index_product.append(str(i))


# if __name__ == "__main__":
#     main()
