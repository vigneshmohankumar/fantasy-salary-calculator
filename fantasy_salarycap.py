# coding: utf-8

import simplejson as json
import csv
import requests
from bs4 import BeautifulSoup
import re

teams = []
rosters = {}

def __init__(self, team, total_salary):
	self.team = team
	self.total_salary = total_salary

def get_rosters():
    result = requests.get('http://games.espn.go.com/fba/leaguerosters?leagueId=115125')
    c = result.content
    rosters_dom = BeautifulSoup(c)
    teams_dom = rosters_dom.find_all('table', class_='playerTableTable')
    for team_dom in teams_dom:
        team_name = team_dom.find(class_='playerTableBgRowHead').a.string
        teams.append(team_name)
        players_dom = team_dom.find_all('td', class_='playertablePlayerName')
        players_list = []
        for player_dom in players_dom:
            player_name = player_dom.a.string
            players_list.append(re.sub("\s\s+" , " ", player_name))
        rosters[team_name] = players_list

def player_search(player):
	with open('./salaries.csv', mode='rU') as f:
	    reader = csv.reader(f)
	    for num, row in enumerate(reader):
	        if player in row[0]:
	            return row[1]
            else:
            	return None

def calc_salary(team_roster):
	total_salary = 0
	for index, player in enumerate(team_roster):
		#print player
		if player_search(player) != None:
			salary = player_search(player)
			#print salary
		else:
			salary = 0
			#print salary
		total_salary = total_salary + float(salary)
	return total_salary

def print_salary(total_salary):
	if total_salary > 65000000:
		print team
		print ("${:,.2f}".format(total_salary)) + " -- OVER CAP"
	else:
		print team
		print ("${:,.2f}".format(total_salary)) + " -- UNDER CAP"

get_rosters()
for index, team in enumerate(teams):
	team_roster = rosters[team]
	print_salary(calc_salary(team_roster))