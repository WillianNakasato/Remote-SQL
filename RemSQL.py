#!/usr/bin/python
import MySQLdb
import prettytable
from prettytable import from_db_cursor
host = input('Enter host name ')
user = input('Enter username ')
passwd = input('Enter password ')
database = input('Enter DB ')
db = MySQLdb.connect(host, # your host, usually localhost
                     user, # your username
                      passwd, # your password
                      database) # name of the data base)

# Create a Cursor object
cur = db.cursor() 
col = input('Enter Column Name')
table = input('Enter Table name')
#columns = map(col, col.split())
cur.execute("SELECT "+col+" FROM "+database+ "."+table+"")
pt = from_db_cursor(cur)
print pt
cur.close()
