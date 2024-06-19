#!/usr/bin/python3

import MySQLdb
database = "GogoDB"

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root")
mcursor = db.cursor()
mcursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

db.close()