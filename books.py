import sqlite3
conn = sqlite3.connect('bookstore.db')
cur = conn.cursor()


#1 Create Inventory Table
try:
    cur.execute('''CREATE TABLE Inventory (Book_title TEXT, Cost REAL, Quantity INTEGER, 
                   ISBN INTEGER, PRIMARY KEY(ISBN))''')
except sqlite3.OperationalError:
    cur.execute('DROP TABLE Inventory')
    cur.execute('''CREATE TABLE Inventory (Book_title TEXT, Cost REAL, Quantity INTEGER, 
                   ISBN INTEGER, PRIMARY KEY(ISBN))''')


#2 Inserts in Inventory
cur.execute('''INSERT INTO Inventory VALUES('Life of Pi', 15.95, 10, 20200429)''')
cur.execute('''INSERT INTO Inventory VALUES('Harry Potter', 15.84, 2, 20200428)''')
cur.execute('''INSERT INTO Inventory VALUES('To Kill A Mocking Bird', 8.99, 3, 20200427)''')
cur.execute('''INSERT INTO Inventory VALUES('1984', 27.71, 9, 20200426)''')
cur.execute('''INSERT INTO Inventory VALUES('Brave New World', 13.07, 7, 20200425)''')
cur.execute('''INSERT INTO Inventory VALUES('Animal Farm', 10.99, 5, 20200424)''')
cur.execute('''INSERT INTO Inventory VALUES('The Hunger Games', 23.99, 10, 20080914)''')
cur.execute('''INSERT INTO Inventory VALUES('Catching Fire', 23.99, 11, 20090901)''')
cur.execute('''INSERT INTO Inventory VALUES('Mockingjay', 23.99, 5, 20100824)''')
cur.execute('''INSERT INTO Inventory VALUES('The Book Thief', 20.05, 0, 20200519)''')
conn.commit()


#3 Most Copies
q3 = '''SELECT Book_title, Quantity FROM Inventory WHERE Quantity = (SELECT MAX(Quantity) FROM Inventory)'''
cur.execute(q3)
for record in cur.fetchall():
    print("most copies: {}".format(record))


#4 Total Number of Books
q4 = '''SELECT SUM(Quantity) FROM Inventory'''
cur.execute(q4)
print("\nnumber of books: {}".format(cur.fetchone()))


#5 Create Author Table
try:
    cur.execute('''CREATE TABLE Author(Book_title TEXT, Author TEXT, PRIMARY KEY(Book_title, Author))''')
except sqlite3.OperationalError:
    cur.execute('DROP TABLE Author')
    cur.execute('''CREATE TABLE Author(Book_title TEXT, Author TEXT, PRIMARY KEY(Book_title, Author))''')

    
#6 Inserts in Author
cur.execute('''INSERT INTO Author VALUES('Life of Pi', 'Yann Martel')''')
cur.execute('''INSERT INTO Author VALUES('The Book Thief', 'Markus Zusak')''')
cur.execute('''INSERT INTO Author VALUES('To Kill A Mocking Bird', 'Harper Lee')''')
cur.execute('''INSERT INTO Author VALUES('Animal Farm', 'George Orwell')''')
cur.execute('''INSERT INTO Author VALUES('Brave New World', 'Aldous Huxley')''')
cur.execute('''INSERT INTO Author VALUES('Burmese Days', 'George Orwell')''') #not in inventory
cur.execute('''INSERT INTO Author VALUES('The Hunger Games', 'Suzanne Collins')''')
cur.execute('''INSERT INTO Author VALUES('Catching Fire', 'Suzanne Collins')''')
cur.execute('''INSERT INTO Author VALUES('Mockingjay', 'Suzanne Collins')''')
conn.commit()


#7 All Available Properties
#not all books are included in the Author Table, natural join will lose all those entries...
#adding the authors for the rest of the books
cur.execute('''INSERT INTO Author VALUES('Harry Potter', 'J.K.Rowling')''')
cur.execute('''INSERT INTO Author VALUES('1984', 'George Orwell')''')
conn.commit()
print("\nall available properties:")
q7 = '''SELECT * FROM Inventory NATURAL JOIN Author'''
cur.execute(q7)
for record in cur.fetchall():
    print(record)
    

#8 Author of Books with More Than 3 Copies
print("\nall authors of more than 3 copies:")
q8 = '''SELECT DISTINCT Author FROM Author NATURAL JOIN Inventory WHERE Quantity > 3'''
cur.execute(q8)
for record in cur.fetchall():
    print(record)


#9 Author With Most Expensive Book
print("\nauthor with most expensive book:")
q9 = '''SELECT Author FROM Author NATURAL JOIN Inventory WHERE Cost = (SELECT MAX(Cost) FROM Inventory)'''
cur.execute(q9)
for record in cur.fetchall():
    print(record)
    
    
#10 Total Inventory of Each Author
print("\ntotal number of books of each author:")
q10 = '''SELECT Author, SUM(Quantity) FROM Author NATURAL JOIN Inventory GROUP BY Author'''
cur.execute(q10)
for record in cur.fetchall():
    print(record)


#11 Other Queries
#11.1 Number of Publications Per Author
print("\nhow many publication per author (in the inventory):")
q11 = '''SELECT Author, COUNT(Quantity) FROM Author NATURAL JOIN Inventory GROUP BY Author'''
cur.execute(q11)
for record in cur.fetchall():
    print(record)

#11.2 Cost To Buy a Series of Books By an Author
print("\ncost to buy all books by an author (in the inventory):")
q11 = '''SELECT Author, SUM(Cost) FROM Author NATURAL JOIN Inventory GROUP BY Author'''
cur.execute(q11)
for record in cur.fetchall():
    print(record)
    

print(cur.execute('SELECT Author From Author WHERE Author = "Authors"').fetchone())