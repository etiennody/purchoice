# Purchoice
App built for project 5 in Python developer path at Openclassrooms.

Find an alternative to a food product. A program that would interact with the [Open Food Facts](https://world.openfoodfacts.org/) database to retrieve foods, compare them and offer the user a healthier alternative to the food they want.

## Requirements
* Python 3
* PyMySQL
* SQLAlchemy

## Setup
To run this application locally:

* Create a virtual environment. First, install pipenv:
    ```
    pip install --user pipenv
    ```

* Clone / create the application repository:
    ```
    git clone https://github.com/etiennody/purchoice.git && cd purchoice
    ````

* Create a database called purchoice (use Mysql)


* Add environment variable to .env file:
        
    * PURCHOICE_DBURL=mysql+pymysql://`<user>`:`<password>`@localhost/purchoice

    We’ll need credentials to connect to the database. As per best practice configuration should be stored in the environment, not the code. Put the bellow environment variable at the application repository, making sure to update the variable for your environment.

* Install the requirements:
    ```
    pipenv install
    ```

* Activate the pipenv shell. If a .env file is present, $ pipenv shell and $ pipenv run will automatically load it, for you:
    ```
    pipenv shell
    ```

* Get products from Open Food Facts:
    ```
    python import_off.py
    ```

* Run the Purchoice application:
    ````
    python app.py
    ````

* Enjoy!
