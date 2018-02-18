import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE store (item TEXT, quanity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quanity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quanity,price))
    conn.commit()
    conn.close()

#insert("Coffee Cup",8,10.5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quanity=?, price=? WHERE item=?",(quanity,price,item))
    conn.commit()
    conn.close()

update(11,6,"Coffee Cup")
#delete("Water")
print(view())
