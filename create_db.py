#! usr/bin/python3
# coding: utf-8

import os

# Script shell python to create database with mysql and its user
os.system("mysql -u ${PURCHOICE_DBUSER} -p < purchoice_db.sql")
