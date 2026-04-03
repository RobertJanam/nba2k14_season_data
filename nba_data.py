# program needs
# 1. Window for user options
    # example:
    # -----Welcome to nba2k14 data collection-----
    # Team: Pistons
    # 1. Game scores
    # 2. Quarter scores
    # 3. Point scores
    # 4. Assist scores
    # 5. Rebound scores
    # 6. Block scores
    # 7. Steal scores

# 2. User clicks game scores.
    # 1. Check all game scores plus teams played
    # 2. Check wins
    # 3. Check losses
    # 4. Check streak --> options for current streak and longest streak (winning or losing)
    # 5. Check avg scores
    # 6. Check  other score analysis
    #     --gap: display largest and smallest margin score
    #     --lowest and  highest score recorded

# 3. User clicks quarter scores
    # 1. Check quarter scores --> options for all 1st, 2nd, 3rd or 4th quarters
    # 2. Check avg quarter scores --> options for all 1st, 2nd, 3rd or 4th quarters
    # 3. Check quarter analysis
    #     --quarter with the highest scores (displays total as well)
    #     --quarters above 30

# 4. User clicks point scores
    # 1. Check Player Points
    #      -- Sort in ascending order
    #      -- Sort in descending order
    # 2. Check Ranking --> talk about ppg ranked from highest to lowest

# 5. User clicks assist scores
    # 1. Check Player Assists
    #      -- Sort in ascending order
    #      -- Sort in descending order
    # 2. Check Ranking --> assist ranked from highest to lowest

# 6. User clicks point scores
    # 1. Check Player Rebounds
    #      -- Sort in ascending order
    #      -- Sort in descending order
    # 2. Check Ranking --> rebound ranked from highest to lowest

import csv
import os
import time
from itertools import zip_longest
from colorama import Fore, Style

# temp lists
game_list = []
quarter_list = []
ppg_list = []
assist_list = []
rebound_list = []
block_list = []
steal_list = []

# file_name, csv_name + file path
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_games = os.path.join(script_dir, "games.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_quarters = os.path.join(script_dir, "quarters.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_ppg = os.path.join(script_dir, "ppg.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_assists = os.path.join(script_dir, "assists.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_rebounds = os.path.join(script_dir, "rebounds.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_blocks = os.path.join(script_dir, "blocks.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_steals = os.path.join(script_dir, "steals.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "team_name.txt")

# headers + team
official_team_name = ""
game_header = ["Opponent", "myScore", "OpScore", "Winner", "Loser"]
quarter_header = ["1st", "2nd", "3rd", "4th"]
ppg_header = ["matchPlayer", "points", "Opponent"]
assist_header = ["Player", "assists", "Opponent"]
rebound_header = ["Player", "rebounds", "Opponent"]
block_header = ["Player", "blocks", "Opponent"]
steal_header = ["Player", "steals", "Opponent"]

def load_team_name():
    with open(file_path, 'r') as file:
        team = file.read()
        actual_team_name = team[6:]
        global official_team_name
        official_team_name = actual_team_name

def store_team_name():
    while True:
        team_name = input("Enter your team for this season: ").lower().strip().title()
        if len(team_name) == 0:
            print("The name of your team cannot be empty.")
            continue

        if len(team_name) >= 25:
            print("The name you've entered is too long.")
            continue

        with open(file_path, 'a') as file:
            file.write(f"Team: {team_name}\n")
        print("Team name saved✔️")
        break

def time_delay():
    for _ in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)

def install_counter():
    max_value = 10
    value = 0.5
    dash_count = 1
    while value <= max_value:
        print(Fore.RED + '-' * dash_count + Style.RESET_ALL)
        print(f"{value:.1f} / {max_value}")
        time.sleep(1)
        value += 1.0
        dash_count += 1
        print("\033[F\033[K\033[F\033[K", end='')
    initialize_csv()
    print("Finished✅")
    main()

def loading_cycle(message="Loading", cycles=3, delay=0.5):
    for i in range(cycles):
        dots = '.' * ((i % 3) + 1)
        print(f"\r{message}{dots}{' ' * (3 - len(dots))}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(delay)
    print("\r" + " " * (len(message) + 6) + "\r", end='')

# initialize csv if not found
def initialize_csv():
    os.makedirs(os.path.dirname(csv_file_path_games), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_path_quarters), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_path_ppg), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_path_assists), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_path_rebounds), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_path_blocks), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_path_steals), exist_ok=True)

    if not os.path.exists(csv_file_path_games) or not os.path.exists(csv_file_path_quarters) or not os.path.exists(csv_file_path_ppg) or not os.path.exists(csv_file_path_assists) or not os.path.exists(csv_file_path_rebounds) or not os.path.exists(csv_file_path_blocks) or not os.path.exists(csv_file_path_steals):

        with open(csv_file_path_games, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

        with open(csv_file_path_quarters, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

        with open(csv_file_path_ppg, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

        with open(csv_file_path_assists, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

        with open(csv_file_path_rebounds, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

        with open(csv_file_path_blocks, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

        with open(csv_file_path_steals, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

# tries to load details from csv (assumes csv is already created and is not empty: otherwise initializes them)
def load_csv():
    global game_list
    global quarter_list
    global ppg_list
    global assist_list
    global rebound_list
    global block_list
    global steal_list

    print("Loading data", end='')
    time_delay()
    print("\n")
    try:
        if not os.path.exists(csv_file_path_games) or not os.path.exists(csv_file_path_quarters) or not os.path.exists(csv_file_path_ppg) or not os.path.exists(csv_file_path_assists) or not os.path.exists(csv_file_path_rebounds) or not os.path.exists(csv_file_path_blocks) or not os.path.exists(csv_file_path_steals):
            print("Memory locations for all or some of your data are not found.")
            print("New ones will be created when you key data required.")
            return_back()

        track = 0
        if os.stat(csv_file_path_games).st_size == 0:
            print("No game score details found.")
            track = 1

        if os.stat(csv_file_path_quarters).st_size == 0:
            print("No quarter score details found.")
            track = 1

        if os.stat(csv_file_path_ppg).st_size == 0:
            print("No ppg score details found.")
            track = 1

        if os.stat(csv_file_path_assists).st_size == 0:
            print("No assist score details found.")
            track = 1

        if os.stat(csv_file_path_rebounds).st_size == 0:
            print("No rebound score details found.")
            track = 1

        if os.stat(csv_file_path_blocks).st_size == 0:
            print("No block score details found.")
            track = 1

        if os.stat(csv_file_path_steals).st_size == 0:
            print("No steal score details found.")
            track = 1

        if track == 1:
            return_back()

        with open(csv_file_path_games, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            game_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 5 columns
                    if len(row) == 5:
                        game_list.append(row)

        with open(csv_file_path_quarters, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            quarter_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 4 columns
                    if len(row) == 4:
                        quarter_list.append(row)

        with open(csv_file_path_ppg, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            ppg_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        ppg_list.append(row)

        with open(csv_file_path_assists, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            assist_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        game_list.append(row)

        with open(csv_file_path_rebounds, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            rebound_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        rebound_list.append(row)

        with open(csv_file_path_blocks, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            block_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        block_list.append(row)

        with open(csv_file_path_steals, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            steal_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        steal_list.append(row)
        main()
    except Exception as e:
        print(f"An error occurred: {e}")

def automate_load_csv():
    global game_list
    global quarter_list
    global ppg_list
    global assist_list
    global rebound_list
    global block_list
    global steal_list

    game_list.clear()
    quarter_list.clear()
    ppg_list.clear()
    assist_list.clear()
    rebound_list.clear()
    block_list.clear()
    steal_list.clear()

    try:
        if not os.path.exists(csv_file_path_games) or not os.path.exists(csv_file_path_quarters) or not os.path.exists(csv_file_path_ppg) or not os.path.exists(csv_file_path_assists) or not os.path.exists(csv_file_path_rebounds) or not os.path.exists(csv_file_path_blocks) or not os.path.exists(csv_file_path_steals):
            print("Memory locations for all or some of your data are not found.")
            print("New ones will be created when you key data required.")
            return_back()

        with open(csv_file_path_games, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            game_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 5 columns
                    if len(row) == 5:
                        game_list.append(row)

        with open(csv_file_path_quarters, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            quarter_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 4 columns
                    if len(row) == 4:
                        quarter_list.append(row)

        with open(csv_file_path_ppg, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            ppg_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        ppg_list.append(row)

        with open(csv_file_path_assists, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            assist_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        assist_list.append(row)

        with open(csv_file_path_rebounds, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            rebound_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        rebound_list.append(row)

        with open(csv_file_path_blocks, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            block_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        block_list.append(row)

        with open(csv_file_path_steals, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_file.readline()

            steal_list = []
            for row in csv_reader:
                if row:
                    # Ensure all rows have 3 columns
                    if len(row) == 3:
                        steal_list.append(row)

    except Exception as e:
        print(f"An error occurred: {e}")


def save_to_csv():
    try:
        with open(csv_file_path_games, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(game_header)
            if game_list:
                for game in game_list:
                    csv_writer.writerow(game)

        with open(csv_file_path_quarters, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(quarter_header)
            if quarter_list:
                for quarter in quarter_list:
                    csv_writer.writerow(quarter)

        with open(csv_file_path_ppg, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(ppg_header)
            if ppg_list:
                for ppg in ppg_list:
                    csv_writer.writerow(ppg)

        with open(csv_file_path_assists, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(assist_header)
            if assist_list:
                for assist in assist_list:
                    csv_writer.writerow(assist)

        with open(csv_file_path_rebounds, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(rebound_header)
            if rebound_list:
                for rebound in rebound_list:
                    csv_writer.writerow(rebound)

        with open(csv_file_path_blocks, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(block_header)
            if block_list:
                for block in block_list:
                    csv_writer.writerow(block)

        with open(csv_file_path_steals, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(steal_header)
            if steal_list:
                for steal in steal_list:
                    csv_writer.writerow(steal)

    except Exception as e:
        print(f"An error occurred: {e}")

# 2. User clicks game scores.
    # 1. Check all game scores plus teams played
    # 2. Check wins
    # 3. Check losses
    # 4. Check streak --> options for current streak and longest streak (winning or losing)
    # 5. Check avg scores
    # 6. Check  other score analysis
    #     --gap: display largest and smallest margin score
    #     --lowest and  highest score recorded



# =================
# key in nba game data (option)
# =================
def nba_game_data():
    automate_load_csv()
    tempList_exit = []

    def check_for_exit():
        for data in tempList_exit:
            data = str(data)
            if data == "-1":
                print("No data has been saved.")
                loading_cycle()
                main()

    print("----------------------------------------------------")
    print("|"+ "NBA 2K14".center(50)+"|")
    print("|"+ "Enter your data here".center(50)+"|")
    print("----------------------------------------------------")
    print(f"Team: {official_team_name}")
    print()
    print("Type (-1) to return to main menu.")
    print("\n"+ "Opponent's Name".center(50))
    print("====================================================")
    while True:
        opponentName = input("Enter opponent's full team name: ").lower().strip().title()
        tempList_exit.append(opponentName)
        check_for_exit()
        if len(opponentName) >= 25:
            print("The name you've entered is too long.")
            print("----------------------------------------------------")
            continue

        if len(opponentName) == 0:
            print("Opponents name cannot be empty.")
            print("----------------------------------------------------")
            continue
        break

    print("\n"+ "Your Score".center(50))
    print("====================================================")
    while True:
        try:
            myScore = int(input("Enter your final score: "))
            tempList_exit.append(myScore)
            check_for_exit()
            if myScore < 0:
                print("Your score cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    print("\n"+ "Opponent's Score".center(50))
    print("====================================================")
    while True:
        try:
            opScore = int(input("Enter opponent's final score: "))
            tempList_exit.append(opScore)
            check_for_exit()
            if opScore < 0:
                print("Your opponent's score cannot be negative.")
                print("----------------------------------------------------")
                continue

            if myScore == opScore:
                print("Games cannot end in a tie.")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    print("\n"+ "Your Quarter Score".center(50))
    print("====================================================")
    while True:
        try:
            q1 = int(input("1st quarter: "))
            if q1 < 0:
                print("Quarter score cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    while True:
        try:
            q2 = int(input("2nd quarter: "))
            if q2 < 0:
                print("Quarter score cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    while True:
        try:
            q3 = int(input("3rd quarter: "))
            if q3 < 0:
                print("Quarter score cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    while True:
        try:
            q4 = int(input("4th quarter: "))
            if q4 < 0:
                print("Quarter score cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    print("\n"+ "Player's points".center(50))
    print("====================================================")
    while True:
        ppg_playerName = input("Enter your player with the highest points: ").strip().lower().title()
        if len(ppg_playerName) == 0:
            print("Player's name cannot be empty.")
            print("----------------------------------------------------")
            continue
        break

    while True:
        try:
            ppg = int(input("Enter points: "))
            if ppg < 0:
                print("Player's points cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    print("\n"+ "Player's assists".center(50))
    print("====================================================")
    while True:
        assist_playerName = input("Enter your player with the most assists: ").strip().lower().title()
        if len(assist_playerName) == 0:
            print("Player's name cannot be empty.")
            print("----------------------------------------------------")
            continue
        break

    while True:
        try:
            assists = int(input("Enter assists: "))
            if assists < 0:
                print("Player's assists cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    print("\n"+ "Player's rebounds".center(50))
    print("====================================================")
    while True:
        rebound_playerName = input("Enter your player with the most rebounds: ").strip().lower().title()
        if len(rebound_playerName) == 0:
            print("Player's name cannot be empty.")
            print("----------------------------------------------------")
            continue
        break

    while True:
        try:
            rebounds = int(input("Enter rebounds: "))
            if rebounds < 0:
                print("Player's rebounds cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")


    print("\n"+ "Player's blocks".center(50))
    print("====================================================")
    while True:
        block_playerName = input("Enter your player with the most blocks: ").strip().lower().title()
        if len(block_playerName) == 0:
            print("Player's name cannot be empty.")
            print("----------------------------------------------------")
            continue
        break

    while True:
        try:
            blocks = int(input("Enter blocks: "))
            if blocks < 0:
                print("Player's blocks cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    print("\n"+ "Player's steals".center(50))
    print("====================================================")
    while True:
        steal_playerName = input("Enter your player with the most steals: ").strip().lower().title()
        if len(steal_playerName) == 0:
            print("Player's name cannot be empty.")
            print("----------------------------------------------------")
            continue
        break

    while True:
        try:
            steals = int(input("Enter steals: "))
            if steals < 0:
                print("Player's steals cannot be negative.")
                print("----------------------------------------------------")
                continue
            break

        except ValueError:
            print("Enter a valid integer.")
            print("----------------------------------------------------")

    # bundle data and save them to csv
    # also handle logic before saving

    # list wrap
    game_list_wrap = []
    quarter_list_wrap = []
    ppg_list_wrap = []
    assist_list_wrap = []
    rebound_list_wrap = []
    block_list_wrap = []
    steal_list_wrap = []

    game_list_wrap.append(opponentName)
    game_list_wrap.append(str(myScore))
    game_list_wrap.append(str(opScore))

    if myScore > opScore:
        separatedYour_teamName = official_team_name.split()[-1]
        game_list_wrap.append(separatedYour_teamName)

        separatedOp_teamName = opponentName.split()[-1]
        game_list_wrap.append(separatedOp_teamName)

    else:
        separatedOp_teamName = opponentName.split()[-1]
        game_list_wrap.append(separatedOp_teamName)

        separatedYour_teamName = official_team_name.split()[-1]
        game_list_wrap.append(separatedYour_teamName)

    quarter_list_wrap.append(str(q1))
    quarter_list_wrap.append(str(q2))
    quarter_list_wrap.append(str(q3))
    quarter_list_wrap.append(str(q4))

    ppg_list_wrap.append(ppg_playerName)
    ppg_list_wrap.append(str(ppg))
    ppg_list_wrap.append(separatedOp_teamName)

    assist_list_wrap.append(assist_playerName)
    assist_list_wrap.append(str(assists))
    assist_list_wrap.append(separatedOp_teamName)

    rebound_list_wrap.append(rebound_playerName)
    rebound_list_wrap.append(str(rebounds))
    rebound_list_wrap.append(separatedOp_teamName)

    block_list_wrap.append(block_playerName)
    block_list_wrap.append(str(blocks))
    block_list_wrap.append(separatedOp_teamName)

    steal_list_wrap.append(steal_playerName)
    steal_list_wrap.append(str(steals))
    steal_list_wrap.append(separatedOp_teamName)

    # append list_wrap to global list
    game_list.append(game_list_wrap)
    quarter_list.append(quarter_list_wrap)
    ppg_list.append(ppg_list_wrap)
    assist_list.append(assist_list_wrap)
    rebound_list.append(rebound_list_wrap)
    block_list.append(block_list_wrap)
    steal_list.append(steal_list_wrap)

    #save
    save_to_csv()
    print("\n📁All Data saved successfully✅")

    # clear list in case of new entry
    # wrap
    game_list_wrap.clear()
    quarter_list_wrap.clear()
    ppg_list_wrap.clear()
    assist_list_wrap.clear()
    rebound_list_wrap.clear()
    block_list_wrap.clear()
    steal_list_wrap.clear()

    return_back()

# =================
# game score option
# =================
def game_score():
    while True:
        print("\n"+ "NBA 2K14 🏀".center(50))
        print("Game Score".center(50))
        print(f"Team: {official_team_name}")
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Check Teams Played".center(50)+"|")
        print("|"+ "2. Check Wins".center(50)+"|") # games won + total wins
        print("|"+ "3. Check Losses".center(50)+"|") # games lost + total losses
        print("|"+ "4. Check Streaks".center(50)+"|")
        print("|"+ "5. Check Avg spg".center(50)+"|")
        print("|"+ "6. Others".center(50)+"|")
        print("|"+ "7. Main menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                teams_played()
            elif option_prompt == 2:
                wins()
            elif option_prompt == 3:
                losses()
            elif option_prompt == 4:
                streaks()
            elif option_prompt == 5:
                avg_spg()
            elif option_prompt == 6:
                other_game_analytics()
            elif option_prompt == 7:
                automate_load_csv()
                save_to_csv()
                main()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

# Every option under game score
# =============================

# teams played
def teams_played():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()
    print("\n©copyright: Mireri Robert")
    print()
    print(f"Team: {official_team_name}")
    print("="*75)
    print("ALL GAMES PLAYED".center(75))
    print("="*75)
    print(f"{'No.':<5} |        {'OPPONENT':<13} |  {'MySCORE':<8}|  {'OpSCORE':<8}|  {'WINNER':<7}")
    print("-"*75)
    for i, t in enumerate(game_list, start=1):
        print(f"{i:<5} | {t[0]:<20} | {t[1]:<8} | {t[2]:<8} | {t[3]:<10}")
        print("-"*75)

    if t == game_list[-1]:
            total_games = i

    print(f"TOTAL GAMES PLAYED: {total_games}")
    print("-"*75)

    print("="*75 + "\n")
    return_back_game()

def wins():
    automate_load_csv()
    game_list_wins = []
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    shortened_teamName = official_team_name.split()[-1]
    for game in game_list:
        if game[3] == shortened_teamName:
            game_list_wins.append(game)

    print("\n©copyright: Mireri Robert")
    print()
    print(f"Team: {official_team_name}")
    print("="*75)
    print("ALL GAMES WON".center(75))
    print("="*75)
    print(f"{'No.':<5} |        {'OPPONENT':<13} |  {'MySCORE':<8}|  {'OpSCORE':<8}")
    print("-"*75)
    for i, t in enumerate(game_list_wins, start=1):
        print(f"{i:<5} | {t[0]:<20} | {t[1]:<8} | {t[2]:<8}")
        print("-"*75)
        if t == game_list_wins[-1]:
            total_wins = i

    print(f"TOTAL WINS: {total_wins}")
    print("-"*75)
    print("="*75 + "\n")

    game_list_wins.clear()

    return_back_game()

def losses():
    automate_load_csv()
    game_list_losses = []
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    shortened_teamName = official_team_name.split()[-1]
    for game in game_list:
        if game[3] != shortened_teamName:
            game_list_losses.append(game)

    print("\n©copyright: Mireri Robert")
    print()
    print(f"Team: {official_team_name}")
    print("="*75)
    print("ALL GAMES LOST".center(75))
    print("="*75)
    print(f"{'No.':<5} |        {'OPPONENT':<13} |  {'MySCORE':<8}|  {'OpSCORE':<8}")
    print("-"*75)
    for i, t in enumerate(game_list_losses, start=1):
        print(f"{i:<5} | {t[0]:<20} | {t[1]:<8} | {t[2]:<8}")
        print("-"*75)
        if t == game_list_losses[-1]:
            total_losses = i

    print(f"TOTAL LOSSES: {total_losses}")
    print("-"*75)
    print("="*75 + "\n")

    game_list_losses.clear()

    return_back_game()

def streaks():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\n©copyright: Mireri Robert")
    print()
    print(f"Team: {official_team_name}")
    print("="*75)
    print("STREAKS".center(75))
    print("="*75)
    print(f"|  {'Current Streak':<10} |  {'Longest Wstreak':<10} |  {'Longest Lstreak':<10}")
    print("-"*75)


    winning_streaks = []
    losing_streaks = []

    w_counter = 0
    l_counter = 0
    for i, item in enumerate(game_list, start=1):
        if item[3] == official_team_name.split()[-1]:
            w_counter += 1
            if l_counter > 0:
                losing_streaks.append(l_counter)
                l_counter = 0
        else:
            l_counter += 1
            winning_streaks.append(w_counter)
            w_counter = 0

        if len(game_list) == i:
            if l_counter != 0:
                losing_streaks.append(l_counter)
            else:
                winning_streaks.append(w_counter)

    longest_Wstreak = winning_streaks[0]
    for i in winning_streaks:
        if i > longest_Wstreak:
            longest_Wstreak = i

    longest_Lstreak = losing_streaks[0]
    for i in losing_streaks:
        if i > longest_Lstreak:
            longest_Lstreak = i

    for _ in game_list:
        previous_game = game_list[-1]

    if not any(range(1, 100)) in winning_streaks:
        current_streak = losing_streaks[-1]
        print(f"|    {current_streak} {"W":<11}|       {"---":<11}|      {longest_Lstreak:<12}")
        print("-"*75)
        return_back_game()

    if not any(range(1, 100)) in losing_streaks:
        current_streak = winning_streaks[-1]
        print(f"|    {current_streak} {"W":<11}|      {longest_Wstreak:<12}|       {"---":<11}")
        print("-"*75)
        return_back_game()

    if previous_game[3] == official_team_name.split()[-1]:
        current_streak = winning_streaks[-1]
        print(f"|    {current_streak} {"W":<11}|      {longest_Wstreak:<12}|      {longest_Lstreak:<12}")
        print("-"*75)
    else:
        current_streak = losing_streaks[-1]
        print(f"|    {current_streak} {"L":<11}|      {longest_Wstreak:<12}|      {longest_Lstreak:<12}")
        print("-"*75)

    print("-"*75)
    print("="*75 + "\n")

    winning_streaks.clear()
    losing_streaks.clear()

    return_back_game()

def avg_spg():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*25)
    print("AVERAGE SCORE PER GAME".center(25))
    print("="*25)
    print(f"|  {'My AVG':<8} |  {'OP AVG':<8}")
    print("-"*25)

    myscore = []
    opscore = []
    # calculations
    for idx, game in enumerate(game_list, start=1):
        myscore.append(int(game[1]))
        opscore.append(int(game[2]))

    myAvg_score = sum(myscore) / idx
    opAvg_score = sum(opscore) / idx

    myAvg_score = round(myAvg_score, 1)
    opAvg_score = round(opAvg_score, 1)

    print(f"|  {myAvg_score:<9}|   {opAvg_score:<8}")

    print("-"*25)
    print("="*25 + "\n")

    myscore.clear()
    opscore.clear()

    return_back_game()

# displaying gaps, highest and lowest scores
def other_game_analytics():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nL: lowest")
    print("H: highest")
    print("OP: opponent")
    print("AMG: AVG MARGIN SCORE")

    print(f"Team: {official_team_name}")
    print("="*75)
    print("OTHER GAME ANALYTICS".center(75))
    print("="*75)
    print(f"| {'MY H SCORE':<10}| {'OP H SCORE':<18} | {'MY L SCORE':<10}| {'OP L SCORE':<18} | {'AMG':<10}")
    print("-"*75)

    my_list = []
    op_list = []

    for idx, game in enumerate(game_list, start=1):
        my_list.append(int(game[1]))
        op_list.append(int(game[2]))

    # find your highest and lowest score
    y_highest = my_list[0]
    y_lowest = my_list[0]

    for score in my_list:
        if score > y_highest:
            y_highest = score
        if score < y_lowest:
            y_lowest = score

    # find op highest score and lowest score
    o_highest = op_list[0]
    o_lowest = op_list[0]

    for score in op_list:
        if score > o_highest:
            o_highest = score
        if score < o_lowest:
            o_lowest = score

    # name of op with highest and lowest score
    game_h_op_list = []
    dup_h_op_list = []
    game_l_op_list = []
    dup_l_op_list = []

    for game in game_list:
        if str(o_highest) == game[2]:
            # we just need to confirm if there are duplicates in the op_list
            if len(op_list) != len(set(op_list)):
               # let's add the game played to the list
                game_h_op_list.append(game)
                h_opName = game[0]
            else:
                h_opName = game[0]
        if str(o_lowest) == game[2]:
            if len(op_list) != len(set(op_list)):
               # let's add the game played to the list
                game_l_op_list.append(game)
                l_opName = game[0]
            else:
                l_opName = game[0]

    for game in game_h_op_list:
        split_h_opName = game[0].split()[-1]
        if len(game_h_op_list) >= 2:
            dup_h_op_list.append(split_h_opName)

    for game in game_l_op_list:
        split_l_opName = game[0].split()[-1]
        if len(game_l_op_list) >= 2:
            dup_l_op_list.append(split_l_opName)

    #print(dup_l_op_list)
    # find margin score
    my_sum = sum(my_list)
    op_sum = sum(op_list)

    diff = my_sum - op_sum

    margin = diff / idx
    margin = round(margin, 1)

    #split name
    if not dup_h_op_list and not dup_l_op_list:
        s_h_opName = h_opName.split()[-1]
        s_l_opName = l_opName.split()[-1]

        print(f"| {y_highest:<10}| {s_h_opName:<12}: {o_highest:<5}| {y_lowest:<10}| {s_l_opName:<12}: {o_lowest:<5}| {margin:<10}")

    else:
        if len(dup_h_op_list) == 0 and len(dup_l_op_list) > 0:
            state = 0
            s_h_opName = h_opName.split()[-1]
            for y in dup_l_op_list:
                if y == dup_l_op_list[1]:
                    state = 1
                if state == 0:
                    print(f"| {y_highest:<11}| {s_h_opName:<12}: {o_highest:<5}| {y_lowest:<11}| {y:<12}: {o_lowest:<5}| {margin:<10}")
                if state == 1:
                    print(f"|  {" "*10:<8}| {" "*16:<10}|   {" "*9:<9}| {y:<12}: {o_lowest:<5}|   {" "*10:<10}")

        elif len(dup_l_op_list) == 0 and len(dup_h_op_list) > 0:
            state = 0
            s_l_opName = l_opName.split()[-1]
            for y in dup_l_op_list:
                if y == dup_l_op_list[1]:
                    state = 1
                if state == 0:
                    print(f"| {y_highest:<11}| {y:<12}: {o_highest:<5}| {y_lowest:<11}| {s_l_opName:<12}: {o_lowest:<5}| {margin:<10}")
                if state == 1:
                    print(f"|  {" "*10:<8}| {y:<16}: {o_highest:<4}|   {" "*9:<9}| {" "*16:<10}|   {" "*10:<10}")

        else:
            state = 0
            for y, z in zip_longest(dup_l_op_list, dup_h_op_list, fillvalue=""):
                if y == dup_l_op_list[1]:
                    state = 1
                if state == 0:
                    print(f"| {y_highest:<11}| {z:<12}: {o_highest:<5}| {y_lowest:<11}| {y:12}: {o_lowest:<5}| {margin:<10}")
                if state == 1:
                    if z == "":
                        if y == "":
                            print(f"| {' ':<11}| {' ':<19}| {' ':<11}| {' ':<19}| {' ':<10}")
                        else:
                            print(f"| {' ':<11}| {' ':<19}| {' ':<11}| {y:<12}: {o_lowest:<5}| {' ':<10}")
                    else:
                        if y == "":
                            print(f"| {' ':<11}| {z:<12}: {o_highest:<5}| {' ':<11}| {' ':<19}| {' ':<10}")
                        else:
                            print(f"| {' ':<11}| {z:<12}: {o_highest:<5}| {' ':<11}| {y:<12}: {o_lowest:<5}| {' ':<10}")

    print("-"*75)
    print("="*75 + "\n")

    my_list.clear()
    op_list.clear()
    game_h_op_list.clear()
    dup_h_op_list.clear()
    game_l_op_list.clear()
    dup_l_op_list.clear()

    return_back_game()


# =================
# quarter score option
# =================
def quarter_score():
    # 3. User clicks quarter scores
    # 1. Check quarter scores --> options for all 1st, 2nd, 3rd or 4th quarters
    # 2. Check avg quarter scores --> options for all 1st, 2nd, 3rd or 4th quarters
    # 3. Check quarter analysis
    #     --quarter with the highest scores (displays total as well)
    #     --quarters above 30

    while True:
        print("\n"+ "NBA 2K14 🏀".center(50))
        print("Quarter Score".center(50))
        print(f"Team: {official_team_name}")
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Check quarter scores".center(50)+"|")
        print("|"+ "2. Check avg quarter scores".center(50)+"|")
        print("|"+ "3. Check quarter analysis".center(50)+"|")
        print("|"+ "4. Main menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                quarter_gameScore()
            elif option_prompt == 2:
                quarter_avgScore()
            elif option_prompt == 3:
                other_quarter_analytics()
            elif option_prompt == 4:
                automate_load_csv()
                save_to_csv()
                main()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

# Every option under quarter score
# =============================

# check quarter score for every game
def quarter_gameScore():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nQ: Quarter")
    print("'Q' shows your quarter scores")

    print(f"Team: {official_team_name}")
    print("="*75)
    print("QUARTER SCORES".center(75))
    print("="*75)
    print(f"| {'WON':<12} | {'LOST':<12} | {'1Q':<8} | {'2Q':<8} | {'3Q':<8} | {'4Q':<8} |")
    print("-"*75)

    for game, quarter in zip(game_list, quarter_list):
        print(f"| {game[3]:<13}| {game[4]:<13}| {quarter[0]:<9}| {quarter[1]:<9}| {quarter[2]:<9}| {quarter[3]:<9}|")

    print("-"*75)
    print("="*75 + "\n")
    return_back_quarter()

def quarter_avgScore():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nQ: Quarter")
    print("'Q' shows your quarter scores")

    print(f"Team: {official_team_name}")
    print("="*45)
    print("QUARTER AVG SCORES".center(45))
    print("="*45)
    print(f"| {'1Q':<8} | {'2Q':<8} | {'3Q':<8} | {'4Q':<8} |")
    print("-"*45)

    q1_list = []
    q2_list = []
    q3_list = []
    q4_list = []

    q1_list = [int(game[0]) for game in quarter_list]
    q2_list = [int(game[1]) for game in quarter_list]
    q3_list = [int(game[2]) for game in quarter_list]
    q4_list = [int(game[3]) for game in quarter_list]

    q1_avg = sum(q1_list) / len(q1_list)
    q2_avg = sum(q2_list) / len(q2_list)
    q3_avg = sum(q3_list) / len(q3_list)
    q4_avg = sum(q4_list) / len(q4_list)

    print(f"| {round(q1_avg, 1):<9}| {round(q2_avg, 1):<9}| {round(q3_avg, 1):<9}| {round(q4_avg, 1):<9}|")

    print("-"*45)
    print("="*45 + "\n")

    q1_list.clear()
    q2_list.clear()
    q3_list.clear()
    q4_list.clear()

    return_back_quarter()

def other_quarter_analytics():
    #     --quarter with the highest scores (displays total as well)
    #     --quarters above 30
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nQ: Quarter")
    print("H: Highest")
    print("L: Lowest")
    print("O: Overall")
    print("'Q H Score O' means the quarter in which you scored the highest overall in numerical value.\n")

    print(f"Team: {official_team_name}")
    print("="*81)
    print("OTHER QUARTER ANALYTICS".center(81))
    print("="*81)
    print(f"| {'H Q Score':<10}  | {'Q H Score O':<8} | {'Q H Score':<8} | {'L Q Score':<8}   | {'Q L Score O':<8} | {'Q L Score':<8} |")
    print("-"*81)

    q1_list = []
    q2_list = []
    q3_list = []
    q4_list = []

    q1_list = [int(game[0]) for game in quarter_list]
    q2_list = [int(game[1]) for game in quarter_list]
    q3_list = [int(game[2]) for game in quarter_list]
    q4_list = [int(game[3]) for game in quarter_list]

    max_q1 = max(q1_list)
    max_q2 = max(q2_list)
    max_q3 = max(q3_list)
    max_q4 = max(q4_list)

    min_q1 = min(q1_list)
    min_q2 = min(q2_list)
    min_q3 = min(q3_list)
    min_q4 = min(q4_list)

    max_q_list = []
    min_q_list = []

    max_q_list.append(max_q1)
    max_q_list.append(max_q2)
    max_q_list.append(max_q3)
    max_q_list.append(max_q4)

    min_q_list.append(min_q1)
    min_q_list.append(min_q2)
    min_q_list.append(min_q3)
    min_q_list.append(min_q4)

    max_qo = max(max_q_list)
    min_qo = min(min_q_list)

    q1_sum = sum(q1_list)
    q2_sum = sum(q2_list)
    q3_sum = sum(q3_list)
    q4_sum = sum(q4_list)

    quarter_sum_list = []

    quarter_sum_list.append(q1_sum)
    quarter_sum_list.append(q2_sum)
    quarter_sum_list.append(q3_sum)
    quarter_sum_list.append(q4_sum)

    max_sum = max(quarter_sum_list)
    min_sum = min(quarter_sum_list)

    for idx, i in enumerate(quarter_sum_list):
        if max_sum == i:
            if idx == 0:
                hq_score = "1st Quarter"
                max_q = max(q1_list)
            elif idx == 1:
                hq_score = "2nd Quarter"
                max_q = max(q2_list)
            elif idx == 2:
                hq_score = "3rd Quarter"
                max_q = max(q3_list)
            else:
                hq_score = "4th Quarter"
                max_q = max(q4_list)

        if min_sum == i:
            if idx == 0:
                lq_score = "1st Quarter"
                min_q = min(q1_list)
            elif idx == 1:
                lq_score = "2nd Quarter"
                min_q = min(q2_list)
            elif idx == 2:
                lq_score = "3rd Quarter"
                min_q = min(q3_list)
            else:
                lq_score = "4th Quarter"
                max_q = min(q4_list)

    print(f"| {hq_score:<9} |     {max_qo:<8}|    {max_q:<7}| {lq_score:<12}|     {min_qo:<8}|    {min_q:<7}|")

    print("-"*81)
    print("="*81 + "\n")

    q1_list.clear()
    q2_list.clear()
    q3_list.clear()
    q4_list.clear()

    max_q_list.clear()
    min_q_list.clear()

    quarter_sum_list.clear()

    return_back_quarter()


# =================
# ppg score option
# =================
def ppg_score():
    # 4. User clicks point scores
    #   1. Check Player Points
    #      -- Sort in ascending order
    #      -- Sort in descending order
    #   2. Check Ranking --> talk about ppg ranked from highest to lowest

    while True:
        print("\n"+ "NBA 2K14 🏀".center(50))
        print("Player Point Score".center(50))
        print(f"Team: {official_team_name}")
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Check Player points".center(50)+"|")
        print("|"+ "2. Check Ranking".center(50)+"|")
        print("|"+ "3. Main menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                player_points()
            elif option_prompt == 2:
                points_ranking()
            elif option_prompt == 3:
                automate_load_csv()
                save_to_csv()
                main()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

# Every option under point score
# =============================

# provides details for the highest player points in each game.
def player_points():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nW: Won")
    print("L: Lost\n")

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER POINTS".center(50))
    print("="*50)
    print(f"| {'PLAYER NAME':<13} | {'POINTS':<8} | {'OPPONENT':<12} | {'W/L':<4} |")
    print("-"*50)

    def result(game):
        if official_team_name.split()[-1] in game[3]:
            result = "W"
        else:
            result = "L"
        return result

    for points, game in zip(ppg_list, game_list):
        print(f"| {points[0]:<14}| {points[1]:<9}| {points[2]:<13}| {result(game):<5}|")

    print("-"*50)
    print("="*50 + "\n")

    sort = input("\nPress any key to return to menu or (s) to sort: ").lower()
    if sort == "s":
        sort_by_points()
    else:
        ppg_score()

# sort in ascending or descending order
def sort_by_points():
    while True:
        print("Sort".center(50))
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. From highest points".center(50)+"|")
        print("|"+ "2. From lowest points".center(50)+"|")
        print("|"+ "3. Menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                sort_ascending_points()
            elif option_prompt == 2:
                sort_descending_points()
            elif option_prompt == 3:
                ppg_score()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

def sort_ascending_points():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER POINTS (A)".center(50))
    print("="*50)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'POINTS':<8} | {'OPPONENT':<12} |")
    print("-"*50)

    ppg_list.sort(key=lambda points: int(points[1]), reverse=True)

    #print(ppg_list)

    for idx, points in enumerate(ppg_list, start=1):
        print(f"| {idx:<4}| {points[0]:<14}| {points[1]:<9}| {points[2]:<13}|")

    print("-"*50)
    print("="*50 + "\n")

    ppg_list.clear()
    return_back_ppg()

def sort_descending_points():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER POINTS (A)".center(50))
    print("="*50)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'POINTS':<8} | {'OPPONENT':<12} |")
    print("-"*50)

    ppg_list.sort(key=lambda points: int(points[1]))

    for idx, points in enumerate(ppg_list, start=1):
        print(f"| {idx:<4}| {points[0]:<14}| {points[1]:<9}| {points[2]:<13}|")

    print("-"*50)
    print("="*50 + "\n")

    ppg_list.clear()
    return_back_ppg()

def points_ranking():
    #   2. Check Ranking --> talk about ppg ranked from highest to lowest
    #   -- 1. Check Highest Player Ranking
    #   -- 2: Check Avg Leaderboard
    while True:
        print("Player Ranking".center(50))
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Check Highest Player Ranking".center(50)+"|")
        print("|"+ "2. Check Avg Leaderboard".center(50)+"|")
        print("|"+ "3. Menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                points_overallHighest()
            elif option_prompt == 2:
                points_avgLeaderboard()
            elif option_prompt == 3:
                ppg_score()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

def points_overallHighest():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nW: Won")
    print("L: Lost\n")

    print(f"Team: {official_team_name}")
    print("="*56)
    print("PLAYER HIGHEST POINTS (RANKED)".center(50))
    print("="*56)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'POINTS':<8} | {'OPPONENT':<12} | {'W/L':<4} |")
    print("-"*56)

    def result(game):
        if official_team_name.split()[-1] in game[3]:
            result = "W"
        else:
            result = "L"
        return result

    ppg_list.sort(key=lambda points: int(points[1]), reverse=True)

    rank_ppg_list = []

    for p in ppg_list:
        if not any(p[0] == existing[0] for existing in rank_ppg_list):
            rank_ppg_list.append(p)

    #print(rank_ppg_list)

    for idx, (points, game) in enumerate(zip(rank_ppg_list, game_list), start=1):
        print(f"| {idx:<4}| {points[0]:<14}| {points[1]:<9}| {points[2]:<13}| {result(game):<5}|")

    print("-"*56)
    print("="*56 + "\n")

    ppg_list.clear()
    rank_ppg_list.clear()

    input("\nPress enter to return to menu... ")
    points_ranking()

def points_avgLeaderboard():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*39)
    print("PLAYER POINTS LEADERBOARD".center(39))
    print("="*39)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<16} | {'AVG POINTS':<9} |")
    print("-"*39)

    player_unique = []
    # take unique names
    for p in ppg_list:
        if not any(p[0] == existing for existing in player_unique):
            player_unique.append(p[0])

    #print(player_unique)

    sort_ppg_list = []
    # sort ppg list
    for i in player_unique:
        for players in ppg_list:
            if i == players[0]:
                sort_ppg_list.append(players)

    #print(sort_ppg_list)

    sum_counter = 0
    player_tracker = "default"
    player_counter = 0

    player_avg_dict = {}

    for idx, points in enumerate(sort_ppg_list, start=1):
        if idx == 1:
            player_tracker = points[0]
            sum_counter += int(points[1])
            player_counter += 1

        else:
            if player_tracker == points[0]:
                if idx == len(sort_ppg_list):
                    sum_counter += int(points[1])
                    player_counter += 1
                    get_avg = sum_counter / player_counter
                    polish_get_avg = float(round(get_avg, 2))
                    player_avg_dict[player_tracker] = polish_get_avg
                    player_counter = 0
                    sum_counter = 0
                    player_tracker = "default"
                    break

                sum_counter += int(points[1])
                player_counter += 1
                #print(player_counter)
                #print("Sum: ", sum_counter)

            else:
                if idx == len(sort_ppg_list):
                    get_avg = sum_counter / player_counter
                    polish_get_avg = float(round(get_avg, 2))
                    player_avg_dict[player_tracker] = polish_get_avg
                    player_tracker = points[0]
                    player_counter = 0
                    sum_counter = 0

                    sum_counter += int(points[1])
                    player_counter += 1
                    get_avg = sum_counter / player_counter
                    polish_get_avg = float(round(get_avg, 2))
                    player_avg_dict[player_tracker] = polish_get_avg
                    player_counter = 0
                    sum_counter = 0
                    player_tracker = "default"
                    break

                get_avg = sum_counter / player_counter
                polish_get_avg = float(round(get_avg, 2))
                player_avg_dict[player_tracker] = polish_get_avg
                player_tracker = points[0]
                player_counter = 0
                sum_counter = 0
                sum_counter += int(points[1])
                player_counter += 1

    #print(player_avg_dict)

    from collections import OrderedDict

    player_avg_dict_sorted = OrderedDict(sorted(player_avg_dict.items(), key=lambda x: x[1], reverse=True))

    for idx, (player, points) in enumerate(player_avg_dict_sorted.items(), start=1):
        print(f"| {idx:<4}| {player:<17}| {points:<11}|")

    print("-"*39)
    print("="*39 + "\n")

    player_unique.clear()
    sort_ppg_list.clear()
    player_avg_dict.clear()
    player_avg_dict_sorted.clear()

    input("\nPress enter to return to menu... ")
    points_ranking()

# =================
# assist score option
# =================
def assist_score():
    # 5. User clicks assist scores
    # 1. Check Player Assists
    #      -- Sort in ascending order
    #      -- Sort in descending order
    # 2. Check Ranking --> assist ranked from highest to lowest

    while True:
        print("\n"+ "NBA 2K14 🏀".center(50))
        print("Player Assist Score".center(50))
        print(f"Team: {official_team_name}")
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Check Player Assists".center(50)+"|")
        print("|"+ "2. Check Ranking".center(50)+"|")
        print("|"+ "3. Main menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                player_assists()
            elif option_prompt == 2:
                assist_ranking()
            elif option_prompt == 3:
                automate_load_csv()
                save_to_csv()
                main()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

# Every option under assist score
# =============================

# provides details for the highest player assists in each game.
def player_assists():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nW: Won")
    print("L: Lost\n")

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER ASSISTS".center(50))
    print("="*50)
    print(f"| {'PLAYER NAME':<13} | {'ASSISTS':<8} | {'OPPONENT':<12} | {'W/L':<4} |")
    print("-"*50)

    def result(game):
        if official_team_name.split()[-1] in game[3]:
            result = "W"
        else:
            result = "L"
        return result

    for assists, game in zip(assist_list, game_list):
        print(f"| {assists[0]:<14}| {assists[1]:<9}| {assists[2]:<13}| {result(game):<5}|")

    print("-"*50)
    print("="*50 + "\n")

    sort = input("\nPress any key to return to menu or (s) to sort: ").lower()
    if sort == "s":
        sort_by_assists()
    else:
        assist_score()

def sort_by_assists():
    while True:
        print("Sort".center(50))
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. From highest assists".center(50)+"|")
        print("|"+ "2. From lowest assists".center(50)+"|")
        print("|"+ "3. Menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                sort_ascending_assists()
            elif option_prompt == 2:
                sort_descending_assists()
            elif option_prompt == 3:
                assist_score()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

def sort_ascending_assists():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER ASSISTS (A)".center(50))
    print("="*50)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'ASSISTS':<8} | {'OPPONENT':<12} |")
    print("-"*50)

    assist_list.sort(key=lambda assists: int(assists[1]), reverse=True)

    for idx, assists in enumerate(assist_list, start=1):
        print(f"| {idx:<4}| {assists[0]:<14}| {assists[1]:<9}| {assists[2]:<13}|")

    print("-"*50)
    print("="*50 + "\n")

    assist_list.clear()
    return_back_assists()

def sort_descending_assists():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER ASSISTS (A)".center(50))
    print("="*50)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'ASSISTS':<8} | {'OPPONENT':<12} |")
    print("-"*50)

    assist_list.sort(key=lambda assists: int(assists[1]))

    for idx, assists in enumerate(assist_list, start=1):
        print(f"| {idx:<4}| {assists[0]:<14}| {assists[1]:<9}| {assists[2]:<13}|")

    print("-"*50)
    print("="*50 + "\n")

    assist_list.clear()
    return_back_assists()

def assist_ranking():
    #   2. Check Ranking --> assists ranked from highest to lowest
    #   -- 1. Check Highest Player Assist Ranking
    #   -- 2: Check Avg Assist Leaderboard
    while True:
        print("Player Ranking".center(50))
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Check Highest Player Assist Ranking".center(50)+"|")
        print("|"+ "2. Check Avg Assist Leaderboard".center(50)+"|")
        print("|"+ "3. Menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                assist_overallHighest()
            elif option_prompt == 2:
                assist_avgLeaderboard()
            elif option_prompt == 3:
                assist_score()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

def assist_overallHighest():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nW: Won")
    print("L: Lost\n")

    print(f"Team: {official_team_name}")
    print("="*56)
    print("PLAYER HIGHEST ASSISTS (RANKED)".center(50))
    print("="*56)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'ASSISTS':<8} | {'OPPONENT':<12} | {'W/L':<4} |")
    print("-"*56)

    def result(game):
        if official_team_name.split()[-1] in game[3]:
            result = "W"
        else:
            result = "L"
        return result

    assist_list.sort(key=lambda assists: int(assists[1]), reverse=True)

    rank_assists_list = []

    for a in assist_list:
        if not any(a[0] == existing[0] for existing in rank_assists_list):
            rank_assists_list.append(a)

    for idx, (assists, game) in enumerate(zip(rank_assists_list, game_list), start=1):
        print(f"| {idx:<4}| {assists[0]:<14}| {assists[1]:<9}| {assists[2]:<13}| {result(game):<5}|")

    print("-"*56)
    print("="*56 + "\n")

    assist_list.clear()
    rank_assists_list.clear()

    input("\nPress enter to return to menu... ")
    assist_ranking()

def assist_avgLeaderboard():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*39)
    print("PLAYER ASSISTS LEADERBOARD".center(39))
    print("="*39)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<16} | {'AVG ASSIST':<9} |")
    print("-"*39)

    player_unique = []
    # take unique names
    for a in assist_list:
        if not any(a[0] == existing for existing in player_unique):
            player_unique.append(a[0])

    #print(player_unique)

    sort_assists_list = []
    # sort assists list
    for i in player_unique:
        for players in assist_list:
            if i == players[0]:
                sort_assists_list.append(players)

    #print(sort_assists_list)

    sum_counter = 0
    player_tracker = "default"
    player_counter = 0

    player_avg_dict = {}

    for idx, points in enumerate(sort_assists_list, start=1):
        if idx == 1:
            player_tracker = points[0]
            sum_counter += int(points[1])
            player_counter += 1

        else:
            if player_tracker == points[0]:
                if idx == len(sort_assists_list):
                    sum_counter += int(points[1])
                    player_counter += 1
                    get_avg = sum_counter / player_counter
                    polish_get_avg = float(round(get_avg, 2))
                    player_avg_dict[player_tracker] = polish_get_avg
                    player_counter = 0
                    sum_counter = 0
                    player_tracker = "default"
                    break

                sum_counter += int(points[1])
                player_counter += 1
                #print(player_counter)
                #print("Sum: ", sum_counter)

            else:
                if idx == len(sort_assists_list):
                    get_avg = sum_counter / player_counter
                    polish_get_avg = float(round(get_avg, 2))
                    player_avg_dict[player_tracker] = polish_get_avg
                    player_tracker = points[0]
                    player_counter = 0
                    sum_counter = 0

                    sum_counter += int(points[1])
                    player_counter += 1
                    get_avg = sum_counter / player_counter
                    polish_get_avg = float(round(get_avg, 2))
                    player_avg_dict[player_tracker] = polish_get_avg
                    player_counter = 0
                    sum_counter = 0
                    player_tracker = "default"
                    break

                get_avg = sum_counter / player_counter
                polish_get_avg = float(round(get_avg, 2))
                player_avg_dict[player_tracker] = polish_get_avg
                player_tracker = points[0]
                player_counter = 0
                sum_counter = 0
                sum_counter += int(points[1])
                player_counter += 1

    from collections import OrderedDict

    player_avg_dict_sorted = OrderedDict(sorted(player_avg_dict.items(), key=lambda x: x[1], reverse=True))

    for idx, (player, points) in enumerate(player_avg_dict_sorted.items(), start=1):
        print(f"| {idx:<4}| {player:<17}| {points:<11}|")

    print("-"*39)
    print("="*39 + "\n")

    player_unique.clear()
    sort_assists_list.clear()
    player_avg_dict.clear()
    player_avg_dict_sorted.clear()

    input("\nPress enter to return to menu... ")
    assist_ranking()


# =================
# rebound score option
# =================
def rebound_score():# 6. User clicks point scores
    # 1. Check Player Rebounds
    #      -- Sort in ascending order
    #      -- Sort in descending order
    # 2. Check Ranking --> rebound ranked from highest to lowest
    while True:
        print("\n"+ "NBA 2K14 🏀".center(50))
        print("Player Rebound Score".center(50))
        print(f"Team: {official_team_name}")
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Check Player Rebounds".center(50)+"|")
        print("|"+ "2. Check Ranking".center(50)+"|")
        print("|"+ "3. Main menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                player_rebounds()
            elif option_prompt == 2:
                rebound_ranking()
            elif option_prompt == 3:
                automate_load_csv()
                save_to_csv()
                main()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

# Every option under rebound score
# =============================

# provides details for the highest player rebounds in each game.
def player_rebounds():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print("\nW: Won")
    print("L: Lost\n")

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER REBOUNDS".center(50))
    print("="*50)
    print(f"| {'PLAYER NAME':<13} | {'REBOUNDS':<8} | {'OPPONENT':<12} | {'W/L':<4} |")
    print("-"*50)

    def result(game):
        if official_team_name.split()[-1] in game[3]:
            result = "W"
        else:
            result = "L"
        return result

    for rebounds, game in zip(rebound_list, game_list):
        print(f"| {rebounds[0]:<14}| {rebounds[1]:<9}| {rebounds[2]:<13}| {result(game):<5}|")

    print("-"*50)
    print("="*50 + "\n")

    sort = input("\nPress any key to return to menu or (s) to sort: ").lower()
    if sort == "s":
        sort_by_rebounds()
    else:
        rebound_score()

def sort_by_rebounds():
    while True:
        print("Sort".center(50))
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. From highest assists".center(50)+"|")
        print("|"+ "2. From lowest assists".center(50)+"|")
        print("|"+ "3. Menu".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                sort_ascending_rebounds()
            elif option_prompt == 2:
                sort_descending_rebounds()
            elif option_prompt == 3:
                rebound_score()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

def sort_ascending_rebounds():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER REBOUNDS (A)".center(50))
    print("="*50)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'REBOUNDS':<8} | {'OPPONENT':<12} |")
    print("-"*50)

    rebound_list.sort(key=lambda rebounds: int(rebounds[1]), reverse=True)

    for idx, rebounds in enumerate(rebound_list, start=1):
        print(f"| {idx:<4}| {rebounds[0]:<14}| {rebounds[1]:<9}| {rebounds[2]:<13}|")

    print("-"*50)
    print("="*50 + "\n")

    rebound_list.clear()
    return_back_rebounds()

def sort_descending_rebounds():
    automate_load_csv()
    if not game_list:
        print("No games entered yet.\nEnter and save your data first to view them.")
        return_back()

    print(f"Team: {official_team_name}")
    print("="*50)
    print("PLAYER REBOUNDS (A)".center(50))
    print("="*50)
    print(f"| {'NO.':<3} | {'PLAYER NAME':<13} | {'REBOUNDS':<8} | {'OPPONENT':<12} |")
    print("-"*50)

    rebound_list.sort(key=lambda rebounds: int(rebounds[1]))

    for idx, rebounds in enumerate(rebound_list, start=1):
        print(f"| {idx:<4}| {rebounds[0]:<14}| {rebounds[1]:<9}| {rebounds[2]:<13}|")

    print("-"*50)
    print("="*50 + "\n")

    rebound_list.clear()
    return_back_rebounds()

def rebound_ranking():
    pass

def rebound_overallHighest():
    pass

def rebound_avgLeaderboard():
    pass

def block_score():
    pass

def steal_score():
    pass

def main():
    if not os.path.exists(csv_file_path_games) or not os.path.exists(csv_file_path_quarters) or not os.path.exists(csv_file_path_ppg) or not os.path.exists(csv_file_path_assists) or not os.path.exists(csv_file_path_rebounds) or not os.path.exists(csv_file_path_blocks) or not os.path.exists(csv_file_path_steals):
        loading_cycle("Preparing files for storage and loading menu. Give it a sec or maybe two. Don't touch your keyboard", cycles=9, delay=0.5)
        print("Progress")
        install_counter()

    if not os.path.exists(file_path):
        store_team_name()

    load_team_name()

    while True:
        print("\n"+ "NBA 2K14 🏀".center(50))
        print("NBA2k14 Data Collection📊".center(50))
        print("Welcome👋")
        print(f"Team: {official_team_name}")
        print("====================================================")
        print("|"+ "Choose your option".center(50)+"|")
        print("----------------------------------------------------")
        print("|"+ "".center(50)+ "|")
        print("|"+ "1. Add Game Data".center(50)+"|")
        print("|"+ "2. Check Game Scores".center(50)+"|")
        print("|"+ "3. Check Quarter Scores".center(50)+"|")
        print("|"+ "4. Check Point scores".center(50)+"|")
        print("|"+ "5. Check Assist scores".center(50)+"|")
        print("|"+ "6. Check Rebound scores".center(50)+"|")
        print("|"+ "7. Check Block scores".center(50)+"|")
        print("|"+ "8. Check Steal scores".center(50)+"|")
        print("|"+ "9. Exit".center(50)+"|")
        print("====================================================")

        try:
            option_prompt = int(input("Enter your choice here --> "))
            if option_prompt == 1:
                nba_game_data()
            elif option_prompt == 2:
                game_score()
            elif option_prompt == 3:
                quarter_score()
            elif option_prompt == 4:
                ppg_score()
            elif option_prompt == 5:
                assist_score()
            elif option_prompt == 6:
                rebound_score()
            elif option_prompt == 7:
                block_score()
            elif option_prompt == 8:
                steal_score()
            elif option_prompt == 9:
                print("Exiting app. Goodbye👋🌊...")
                automate_load_csv()
                save_to_csv()
                exit()
            else:
                print("Invalid option. Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")


def return_back():
    input("\nPress enter to return to main menu... ")
    main()

def return_back_game():
    input("\nPress enter to return to menu... ")
    game_score()

def return_back_quarter():
    input("\nPress enter to return to menu... ")
    quarter_score()

def return_back_ppg():
    input("\nPress enter to return to menu... ")
    ppg_score()

def return_back_assists():
    input("\nPress enter to return to menu... ")
    assist_score()

def return_back_rebounds():
    input("\nPress enter to return to menu... ")
    rebound_score()

if __name__ == "__main__":
    load_csv()