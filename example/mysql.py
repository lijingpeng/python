#!/usr/bin/env python
# Last edited: 20130713
# @author lijingpeng
# Python mysql test

import MySQLdb

# Create a mysql connection
conn = MySQLdb.connection( host = 'localhost', user = 'root', passwd = 'lijingpeng' )

# Create Cursor
cursor = conn.cursor()

# Select database
conn.select_db('test')

# 1. Insert
cursor.execute("""insert into test values( 'admin', 'a' ) """)

# Close the connection
cursor.close()
