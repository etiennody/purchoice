#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import create_engine

# Engine configuration to connect database with PyMySQL
engine = create_engine('mysql+pymysql:purbeurre/purbeurre@localhost/purchoice', echo=True)
