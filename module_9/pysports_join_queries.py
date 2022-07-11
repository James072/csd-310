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
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM team t JOIN player p ON t.team_id = p.team_id")
members = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")
for member in members:
    print(f"Player ID: {member[0]}")
    print(f"First Name: {member[1]}")
    print(f"Last Name: {member[2]}")
    print(f"Team Name: {member[3]}") 
    print()
print()
