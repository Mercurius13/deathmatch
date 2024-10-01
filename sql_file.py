import mysql.connector
from mysql.connector import cursor


def create_table():
    create_table_sql = "CREATE TABLE IF NOT EXISTS stats (id INT AUTO_INCREMENT PRIMARY KEY, player_name VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, no_of_games INT NOT NULL DEFAULT 0, no_of_wins INT NOT NULL DEFAULT 0, avg_turns_per_game DECIMAL(10, 2) NOT NULL DEFAULT 0.00, max_damage_as_rogue INT NOT NULL DEFAULT 0, max_damage_as_lancelot INT NOT NULL DEFAULT 0, max_damage_as_master INT NOT NULL DEFAULT 0, max_win_streak INT NOT NULL DEFAULT 0, CONSTRAINT unique_player_password UNIQUE (player_name, password));"

    cursor.execute(create_table_sql)


def sign_up(username, password):
    # Establish a connection to MySQL
    connection = mysql.connector.connect(
        user="root",
        password="admin@123",
        database="game_stats"
    )
    cursor = connection.cursor()
    print(username, password)

    # Define the SQL command to insert data using parameters
    insert_data_sql = "INSERT INTO stats (player_name, password) VALUES (%s, %s)"

    # Define the data to be inserted
    data_to_insert = (username, password)

    # Execute the SQL command to insert data
    cursor.execute(insert_data_sql, data_to_insert)

    # Commit the changes
    connection.commit()
    print("Data inserted successfully.")
    cursor.close()
    connection.close()


def login(username, password):
    # Establish a connection to MySQL
    connection = mysql.connector.connect(
        user="root",
        password="admin@123",
        database="game_stats"
    )
    cursor = connection.cursor()
    print(f"Attempting to log in with username: {username}")

    # Define the SQL command to select a row with the given username and password
    select_user_sql = "SELECT * FROM stats WHERE player_name = %s AND password = %s"

    # Define the data to be used as parameters in the query
    data_to_select = (username, password)

    # Execute the SQL command to select the user
    cursor.execute(select_user_sql, data_to_select)

    # Fetch the result
    result = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()

    if result:
        print(result)
        return result
    else:
        print("No user found with the given username and password.")
        return None


def update_game_stats(new_max_damage_as_rogue, new_max_damage_as_lancelot,
                      new_max_damage_as_master, win_or_loss, no_of_turns, holy_tuple):
    # Establish a connection to MySQL
    connection = mysql.connector.connect(
        user="root",
        password="admin@123",
        database="game_stats"
    )
    cursor = connection.cursor()
    id, username, password, no_of_games, no_of_wins, avg_turns_per_game, max_damage_as_rogue, max_damage_as_lancelot, max_damage_as_master, max_win_streak = holy_tuple
    print(f"Updating game stats for player: {username}")
    # Update the game stats
    no_of_games += int(no_of_games) + 1
    avg_turns_per_game = ((int(avg_turns_per_game) * int(no_of_games)) + int(no_of_turns)) / int(no_of_games)
    if new_max_damage_as_master > max_damage_as_master:
        max_damage_as_master = new_max_damage_as_master
    if new_max_damage_as_rogue > max_damage_as_rogue:
        max_damage_as_rogue = new_max_damage_as_rogue
    if new_max_damage_as_lancelot > max_damage_as_lancelot:
        max_damage_as_lancelot = new_max_damage_as_lancelot
    if win_or_loss:
        max_win_streak += win_or_loss
    else:
        max_win_streak = 0
    # Define the SQL command to update the game stats for the player
    update_data_sql = "UPDATE stats SET no_of_games = %s, no_of_wins = %s, avg_turns_per_game = %s, max_damage_as_rogue = %s, max_damage_as_lancelot = %s, max_damage_as_master = %s, max_win_streak = %s WHERE player_name = %s;"

    # Define the data to be used as parameters in the query
    print(no_of_games, no_of_wins, avg_turns_per_game, max_damage_as_rogue, max_damage_as_lancelot,
          max_damage_as_master,
          max_win_streak, username)
    data_to_update = (
        no_of_games, no_of_wins, avg_turns_per_game, max_damage_as_rogue, max_damage_as_lancelot, max_damage_as_master,
        max_win_streak, username)
    cursor.execute(update_data_sql, data_to_update)
    print(no_of_games, no_of_wins, avg_turns_per_game, max_damage_as_rogue, max_damage_as_lancelot, max_damage_as_master,
          max_win_streak, username)
    connection.commit()
    cursor.close()
    connection.close()


def get_stats(tup):
    # get stats of a player
    connection = mysql.connector.connect(
        user="root",
        password="admin@123",
        database="game_stats"
    )
    cursor = connection.cursor()
    # get the stats from the
    select_user_sql = "SELECT * FROM stats WHERE player_name = %s AND password = %s;"

    data_to_select_1 = (tup[0][0], tup[0][1])
    cursor.execute(select_user_sql, data_to_select_1)
    result_1 = cursor.fetchone()

    data_to_select_2 = (tup[1][0], tup[1][1])
    cursor.execute(select_user_sql, data_to_select_2)
    result_2 = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return result_1, result_2

# create_table()
# sign_up("Athena", "howboutalilmor")
# holy_tuple = login("Athena", "howboutalilmor")
