# Purchoice
App built for project 5 in Python developer path at Openclassrooms.

Find an alternative to a food product. A program that would interact with the [Open Food Facts](https://world.openfoodfacts.org/) database to retrieve foods, compare them and offer the user a healthier alternative to the food they want.

## Requirements
* Python 3
* PyMySQL
* Sqlalchemy

## Setup
To run this application locally:

* Create a virtual env. First, install pipenv:

`pip install --user pipenv`

* Clone / create the application repository:

`git clone https://github.com/etiennody/purchoice && cd purchoice`

* Create a database called purchoice (use Mysql)

* Add env variables to .env:
        
    * PURCHOICE_DBURL=mysql+pymysql://`<user>`:`<password>`@localhost/purchoice (use your own credentials for `<user>` and `<password>`)

We’ll need credentials to connect to the database. As per best practice configuration should be stored in the environment, not the code. Put the bellow env variables at the application repository, making sure to update the variables for your environment.

* Install the requirements:

`pipenv install`


