import sqlite3
import csv

con=sqlite3.connect("dora.db")
cursor=con.cursor()

##query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
##cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'python','C:\\Users\\Abc\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\idlelib\\idle.pyw')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'Whatsapp', 'https://web.whatsapp.com/')"
#cursor.execute(query)
#con.commit()

#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
    #id INTEGER PRIMARY KEY,
    #name VARCHAR(200),
    #mobile_no VARCHAR(255),
    #email VARCHAR(255) NULL
#)''')

#query = "INSERT INTO contacts VALUES (null,'sakshi', '93217 64810', 'null')"
#cursor.execute(query)
#con.commit()
#query = 'anuja'
#query = query.strip().lower()

#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])

