import sqlite3

def add_player(cursor):
    name = input('name: ')
    goals = int(input('# of goals scored: '))
    shirt = int(input('shirt number: '))
    team = input('team name: ')
    cursor.execute('INSERT INTO Players VALUES(?,?,?,?)', (name,goals,shirt,team))
    conn.commit()
    
def add_team(cursor):
    team = input('team name: ')
    points = int(input('points: '))
    cursor.execute('INSERT INTO Teams VALUES(?,?)', (team,points))
    conn.commit()
    

conn = sqlite3.connect('league.db')
cur = conn.cursor()

#Create and fill Players table
try:
    cur.execute('''CREATE TABLE Players (Name TEXT, Goals_scored INTEGER,
                   Shirt_number INTEGER, Team_name TEXT, PRIMARY KEY(Shirt_number, Team_name))''')
except sqlite3.OperationalError:
    cur.execute('DROP TABLE Players')
    cur.execute('CREATE TABLE Players (Name TEXT, Goals_scored INTEGER, Shirt_number INTEGER, Team_name TEXT, PRIMARY KEY(Shirt_number, Team_name))')

cur.execute('INSERT INTO Players VALUES("John Smith", 3, 3, "Orange")')
cur.execute('INSERT INTO Players VALUES("Jeff Lerner", 0, 7, "TRSL United")')
cur.execute('INSERT INTO Players VALUES("Steve Smith", 4, 18, "Maple Laughs")')
cur.execute('INSERT INTO Players VALUES("Tom Morrow", 2, 2, "Maple Laughs")')
cur.execute('INSERT INTO Players VALUES("Will Power", 1, 10, "Orange")')
cur.execute('INSERT INTO Players VALUES("Adam Foster", 6, 5, "TRSL United")')
cur.execute('INSERT INTO Players VALUES("Tiger Woods", 0, 11, "Maple Laughs")')
cur.execute('INSERT INTO Players VALUES("Morris Les", 7, 15, "Orange")')

#Create and fill Teams table
try:
    cur.execute('CREATE TABLE Teams (Team_name TEXT, Points INTEGER, PRIMARY KEY(Team_name))')
except:
    cur.execute('DROP TABLE Teams')
    cur.execute('CREATE TABLE Teams (Team_name TEXT, Points INTEGER, PRIMARY KEY(Team_name))')

cur.execute('INSERT INTO Teams VALUES("Orange", 8)')
cur.execute('INSERT INTO Teams VALUES("TRSL United", 10)')
cur.execute('INSERT INTO Teams VALUES("Maple Laughs", 3)')

conn.commit()


for i in range(12):
    add_player(cur)
for i in range(2):
    add_team(cur)
conn.commit()


    
#WRITE YOUR EXERCISE QUERIES BELOW HERE (simple example shown)
query = '''SELECT * FROM Players'''
cur.execute(query)
for record in cur.fetchall():
    print(record)
print('-------------------------------------------------')


#Find players with team names containing an "A", order them by number of goals scored (most to least)
q1 = '''SELECT * FROM Players WHERE Team_name LIKE "%a%" ORDER BY Goals_scored DESC'''
cur.execute(q1)
for record in cur.fetchall():
    print(record)
print('-------------------------------------------------')


#Find players with a four letter first name, order them by their shirt number
q2 = '''SELECT Name,Shirt_number FROM Players WHERE Name LIKE "____ _%" ORDER BY Shirt_number'''
cur.execute(q2)
for record in cur.fetchall():
    print(record)
print('-------------------------------------------------')


#Put all teams containing 'E' in their name in order from most to least points
q3 = '''SELECT Team_name FROM Teams WHERE Team_name LIKE "%E%" ORDER BY Points DESC'''
cur.execute(q3)
for record in cur.fetchall():
    print(record)
print('-------------------------------------------------')


#find all players from teams of more than 5 points that has more than 3 goals
q4 = '''SELECT DISTINCT Name,Goals_scored,Points 
        FROM Players NATURAL JOIN Teams 
        WHERE Goals_scored>2 AND Points>5'''
cur.execute(q4)
for record in cur.fetchall():
    print(record)
print('-------------------------------------------------')


#Order players in teams which have more than 5 points alphabetically by first name
q5 = '''SELECT * FROM Players  NATURAL JOIN Teams
        WHERE Points>5 ORDER BY Name'''
cur.execute(q5)
for record in cur.fetchall():
    print(record)


conn.close()