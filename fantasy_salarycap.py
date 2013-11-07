import simplejson as json

salaries_file = open('/Users/vignesh/Desktop/DESKTOP/python/salaries')
salaries = json.load(salaries_file)
salaries_file.close()

print json.dumps(salaries)

team_list = [team1, team2, team3]

team1 = ['rajon rondo', 'deron williams', 'chris paul', 'kobe bryant', 'carmelo anthony']
team2 = ['dwight howard', 'kevin durant', 'chris johnson', 'wesley matthews']
team3 = ['nene', 'gerald wallace', 'paul pierce', 'stephen curry']

team1_salaries = []
team2_salaries = []
team3_salaries = []

for index in range(len(team_list)):
	i = (item).next()
	i = team
	calc_salary(team)
	calc_netsalary(team)

def calc_salary(team):
	for index in range(len(%r)): 
		i = (item["salary"] for item in salaries if item["player"] == %r[index]).next() % team
		%r_salaries.append(i) % team

def calc_netsalary(team)
	net_salary_%r = sum(%r_salaries) % (team, team)

def print_net_print_salary(team)
	if net_salary_team1 > 65000000:
		print (${:,.2f}".format(net_salary_team1)) + " -- !OVER CAP!"
	else:
		print ("${:,.2f}".format(net_salary_team1)) + " -- UNDER CAP"