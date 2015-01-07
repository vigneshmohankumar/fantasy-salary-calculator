import csv
import re
import requests

from bs4 import BeautifulSoup


teams = []
rosters = {}

def get_rosters():
    """
    Gets the rosters for all teams in a fantasy league. Enter the URL for
    league rosters as the ROSTERS_URL constant.

    Adds each team to a list (teams) and a roster of players for each team in
    a dict (rosters).

    """
    ROSTERS_URL = 'http://games.espn.go.com/fba/leaguerosters?leagueId=115125'

    r = requests.get(ROSTERS_URL)
    table_soup = BeautifulSoup(r.content)
    roster_tables = table_soup.find_all('table', class_='playerTableTable')

    for roster_table in roster_tables:
        team = roster_table.find(class_='playerTableBgRowHead').a.string
        teams.append(team)
        players = roster_table.find_all('td', class_='playertablePlayerName')

        players_list = []
        for player in players:  # Each row in the table is a player.
            player_name = player.a.string
            players_list.append(re.sub("\s\s+" , " ", player_name))

        rosters[team] = players_list


def player_search(player):
    """
    Searches in the salaries file for a player's salary.

    Args:
        player (string): Name of the player.

    Returns:
        int if player in salaries, else None.

    Examples:
        >>> print player_search('Kobe Bryant')
        30453805
        >>> print player_search('Vignesh Mohankumar')
        None

    """
    with open('./salaries.csv', mode='rU') as f:
        reader = csv.reader(f)
        for num, row in enumerate(reader):
            if player in row[0]:
                return row[1]
            else:
                return None


def calc_salary(team_roster):
    """
    Calculates the salary for a team's roster.

    Args:
        team_roster (list): Players on a team.

    Returns:
        int: total salary for a team.

    """
    total_salary = 0

    for index, player in enumerate(team_roster):
        salary = player_search(player)
        if not salary:
            salary = 0
        total_salary = total_salary + int(salary)

    return total_salary


def print_salary(team, total_salary):
    """
    Prints the salary of a team by taking the total_salary of the roster.

    Args:
        team (string): Name of team.
        total_salary (int): Salary of team.

    Examples:
        >>> total_salary('Winners', 85000000)
        Winners
        OVER CAP
        20,000,000

        >>> total_salary('Losers', 55000000)
        Losers
        under cap
        -10,000,000

    """
    print team
    if total_salary > 65000000:
        print "OVER CAP"
    else:
        print "under cap"
    print ("{0:,}".format(total_salary-65000000))
    print


if __name__ == '__main__':
    get_rosters()
    for team in teams:
        team_roster = rosters[team]
        salary = calc_salary(team_roster)
        print_salary(team, salary)
