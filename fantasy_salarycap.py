# coding: utf-8

import simplejson as json
import csv

def __init__(self, team, total_salary):
	self.team = team
	self.total_salary = total_salary

def player_search(player):
	with open('./salaries.csv', mode='rU') as f:
	    reader = csv.reader(f)
	    for num, row in enumerate(reader):
	        if player in row[0]:
	            return row[1]
            else:
            	return None

def calc_salary(team):
	total_salary = 0
	for index, player in enumerate(team):
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

team1 = ['Deron Williams', 'Chris Paul', 'Kobe Bryant']
team2 = ['Dwight Howard', 'Kevin Durant', 'Wesley Matthews']

team_list = [team1, team2]

for index, team in enumerate(team_list):
	#print team
	print_salary(calc_salary(team))