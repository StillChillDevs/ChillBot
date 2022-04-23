# Test for storage.py
# WHEN TESTING: Move this file to outside

import storage
from sqlite3 import connect

connection = connect('bot-data.db')
cursor = connection.cursor()

# Setup global_user_data table
cursor.execute('CREATE TABLE global_user_data (user_id int, key text, value text, type text)')

# Setup guild_user_data table
cursor.execute('CREATE TABLE guild_user_data (guild_id int, user_id int, key text, value text, type text)')

# Setupt guild_data table
cursor.execute('CREATE TABLE guild_data (guild_id int, key text, value text, type text)')
