import nflgame
years = [2009, 2010, 2011, 2012, 2013, 2014]
weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
teams = ['SD','KC','DEN','OAK','TEN','PIT','MIA','ATL','BAL','PHI','CAR','CIN','MIN','CLE','NYJ','HOU','JAC','IND','DET','NO','DAL','TB','SF','ARI','WAS','NYG','STL','SEA','CHI','GB','BUF','NE']

f = open("teamStats.arff", 'w')
for team in teams:
	print "Team: ", team
	f.write("Team: {}\n".format(team))
	for year in years:
		print "Year: ", year
		f.write("Year: {}\n".format(year))
		for week in weeks:
			# print "Week: ", week
			f.write("Week: {}, ".format(week))
			games = nflgame.games(year, week, kind='REG')
			foundGame = False
			for game in games:
				winner = game.home if game.score_home > game.score_away else game.away
				if game.home == team:
					f.write("{},{},{},{},{},{},{},{}\n".format(game.stats_home.total_yds, 
															game.stats_home.passing_yds,
															game.stats_home.rushing_yds, 
															game.stats_home.first_downs, 
															game.stats_home.turnovers, 
															game.stats_home.punt_cnt, 
															game.stats_home.pos_time.total_seconds(),
															winner))
					foundGame = True
				elif game.away == team:
					f.write("{},{},{},{},{},{},{},{}\n".format(game.stats_away.total_yds, 
															game.stats_away.passing_yds,
															game.stats_away.rushing_yds, 
															game.stats_away.first_downs, 
															game.stats_away.turnovers, 
															game.stats_away.punt_cnt, 
															game.stats_away.pos_time.total_seconds(),
															winner))
					foundGame = True
			if(not foundGame):
				f.write("\n")
f.close()