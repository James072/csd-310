import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "TrU3eMa5sT3Er#70",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], 
          config["host"], config["database"]))
    
    input("\n\n Press any key to continue...")
    print()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied user name or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()
cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1);")

cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player p JOIN team t ON p.team_id = t.team_id;")
players = cursor.fetchall()

print("-- DISPLAYING PLAYERS AFTER INSERT --")
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team Name: {player[3]}") 
    print()
print()

cursor = db.cursor()
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player p JOIN team t ON p.team_id = t.team_id;")
playas = cursor.fetchall()

print("-- DISPLAYING PLAYERS AFTER UPDATE --")
for playa in playas:
    print(f"Player ID: {playa[0]}")
    print(f"First Name: {playa[1]}")
    print(f"Last Name: {playa[2]}")
    print(f"Team Name: {playa[3]}") 
    print()
print()

cursor = db.cursor()
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player p JOIN team t ON p.team_id = t.team_id;")
playahs = cursor.fetchall()

print("-- DISPLAYING PLAYERS AFTER DELETE --")
for playah in playahs:
    print(f"Player ID: {playah[0]}")
    print(f"First Name: {playah[1]}")
    print(f"Last Name: {playah[2]}")
    print(f"Team Name: {playah[3]}") 
    print()
print()