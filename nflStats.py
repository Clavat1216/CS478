import nflgame
years = [2009, 2010, 2011, 2012, 2013, 2014]
weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# teams = ['SD','KC','DEN','OAK','TEN','PIT','MIA','ATL','BAL','PHI','CAR','CIN','MIN','CLE','NYJ','HOU','JAC','IND','DET','NO','DAL','TB','SF','ARI','WAS','NYG','STL','SEA','CHI','GB','BUF','NE']
arff = ['Year','Week',
		'homeTotalYds','homePassYds','homeRushYds','homeFirstDowns','homeTurnovers','homePunts','homePosTime',
		'awayTotalYds','awayPassYds','awayRushYds','awayFirstDowns','awayTurnovers','awayPunts','awayPosTime']


f = open("test.txt", 'w')
f.write("@RELATION nfl\n\n")
for line in arff:
	f.write("@ATTRIBUTE {} real\n".format(line))
f.write("@ATTRIBUTE class {1,2}\n\n@Data\n")
for year in years:
	print "Year: ", year
	for week in weeks:
		games = nflgame.games(year, week, kind='REG')
		for game in games:
			winner = "1" if game.score_home > game.score_away else "2"
			f.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
																					year,
																					week,
																					game.stats_home.total_yds, 
																					game.stats_home.passing_yds,
																					game.stats_home.rushing_yds, 
																					game.stats_home.first_downs, 
																					game.stats_home.turnovers, 
																					game.stats_home.punt_cnt, 
																					game.stats_home.pos_time.total_seconds(),
																					game.stats_away.total_yds,
																					game.stats_away.passing_yds, 
																					game.stats_away.rushing_yds,
																					game.stats_away.first_downs,
																					game.stats_away.turnovers,
																					game.stats_away.punt_cnt,
																					game.stats_away.pos_time.total_seconds(),
																					winner))
			f.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
																					year,
																					week,
																					game.stats_away.total_yds, 
																					game.stats_away.passing_yds,
																					game.stats_away.rushing_yds, 
																					game.stats_away.first_downs, 
																					game.stats_away.turnovers, 
																					game.stats_away.punt_cnt, 
																					game.stats_away.pos_time.total_seconds(),
																					game.stats_home.total_yds,
																					game.stats_home.passing_yds, 
																					game.stats_home.rushing_yds,
																					game.stats_home.first_downs,
																					game.stats_home.turnovers,
																					game.stats_home.punt_cnt,
																					game.stats_home.pos_time.total_seconds(),
																					winner))
f.close()

	# for team in teams:
	# 	print "Team: ", team
	# 	aveYardsPG = 0
	# 	avePassPG = 0
	# 	aveRushPG = 0
	# 	ave1stDownsPG = 0
	# 	aveTurnoversPG = 0
	# 	aveForcedTurnoversPG = 0
	# 	avePuntsPG = 0
	# 	aveTimePossessionPG = 0
	# 	last3YPG = 0
	# 	last3PPG = 0
	# 	last3RPG = 0
	# 	last3FDPG = 0
	# 	last3TPG = 0
	# 	last3FTPG = 0
	# 	last3PuPG = 0
	# 	last3TPPG = 0
	# 	for week in weeks:
	# 		print "Week: ", week
	# 		if(week == 1):
	# 			d = 1
	# 		else:
	# 			d = 2
	# 		games = nflgame.games(year, week, kind='REG')
	# 		for game in games:
	# 			if game.home == team:
	# 				# print game.stats_home.total_yds, game.stats_home.passing_yds, game.stats_home.rushing_yds, game.stats_home.turnovers, game.stats_away.turnovers, game.stats_home.punt_cnt, game.stats_home.pos_time
	# 				aveYardsPG = (aveYardsPG + game.stats_home.total_yds)/d
	# 				avePassPG = (avePassPG + game.stats_home.passing_yds)/d
	# 				aveRushPG = (aveRushPG + game.stats_home.rushing_yds)/d
	# 				ave1stDownsPG = (ave1stDownsPG + game.stats_home.first_downs)/d
	# 				aveTurnoversPG = (aveTurnoversPG + game.stats_home.turnovers)/d
	# 				aveForcedTurnoversPG = (aveForcedTurnoversPG + game.stats_away.turnovers)/d
	# 				avePuntsPG = (avePuntsPG + game.stats_home.punt_cnt)/d
	# 				# aveTimePossessionPG = (aveTimePossessionPG + game.stats_home.pos_time)/d
	# 				awayScore = game.score_away
	# 				homeScore = game.score_home
	# 				print "Opponent: ", game.away
	# 				if awayScore > homeScore:
	# 					print "Winner: ", game.away
	# 				else:
	# 					print "Winner: ", game.home
	# 				print "Last 3 Games Average: ", last3YPG, last3PPG, last3RPG, last3FDPG, last3TPG, last3FTPG, last3PuPG, last3TPPG
	# 				print "Season Average: ", aveYardsPG, avePassPG, aveRushPG, ave1stDownsPG, aveTurnoversPG, aveForcedTurnoversPG, avePuntsPG, aveTimePossessionPG
	# 				f.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(game.stats_home.total_yds, 
	# 																					game.stats_home.passing_yds,
	# 																					game.stats_home.rushing_yds, 
	# 																					game.stats_home.first_downs, 
	# 																					game.stats_home.turnovers, 
	# 																					game.stats_home.punt_cnt, 
	# 																					game.stats_home.pos_time,
	# 																					game.stats_away.total_yds,
	# 																					game.stats_away.passing_yds, 
	# 																					game.stats_away.rushing_yds,
	# 																					game.stats_away.first_downs,
	# 																					game.stats_away.turnovers,
	# 																					game.stats_away.punt_cnt,
	# 																					game.stats_away.pos_time))
	# 			elif game.away == team:
	# 				# print game.stats_away.total_yds, game.stats_away.passing_yds, game.stats_away.rushing_yds, game.stats_away.turnovers, game.stats_home.turnovers, game.stats_away.punt_cnt, game.stats_away.pos_time
	# 				aveYardsPG = (aveYardsPG + game.stats_away.total_yds)/d
	# 				avePassPG = (avePassPG + game.stats_away.passing_yds)/d
	# 				aveRushPG = (aveRushPG + game.stats_away.rushing_yds)/d
	# 				ave1stDownsPG = (ave1stDownsPG + game.stats_away.first_downs)/d
	# 				aveTurnoversPG = (aveTurnoversPG + game.stats_away.turnovers)/d
	# 				aveForcedTurnoversPG = (aveForcedTurnoversPG + game.stats_home.turnovers)/d
	# 				avePuntsPG = (avePuntsPG + game.stats_away.punt_cnt)/d
	# 				# aveTimePossessionPG = (aveTimePossessionPG + game.stats_away.pos_time)/d
	# 				awayScore = game.score_away
	# 				homeScore = game.score_home
	# 				print "Opponent: ", game.home
	# 				if awayScore > homeScore:
	# 					print "Winner: ", game.away
	# 				else:
	# 					print "Winner: ", game.home
	# 				print "Last 3 Games Average: ", last3YPG, last3PPG, last3RPG, last3FDPG, last3TPG, last3FTPG, last3PuPG, last3TPPG
	# 				print "Season Average: ", aveYardsPG, avePassPG, aveRushPG, ave1stDownsPG, aveTurnoversPG, aveForcedTurnoversPG, avePuntsPG, aveTimePossessionPG

			# games = nflgame.games(year, week=week, kind="REG")
			# for game in games:
			# 	# Find stats on the home team from entire season
			# 	if(week != 1):
			# 		curWeek = week-1;
			# 		# Broken, not away and home
			# 		lastAway = nflgame.games(year, week=curWeek, away=game.away, kind="REG")
			# 		lastHome = nflgame.games(year, week=curWeek, home=game.home, kind="REG")
			# 		print lastAway.stats_away.total_yds, lastAway.stats_away.passing_yds, lastAway.stats_away.rushing_yds, lastAway.stats_away.turnovers, lastAway.stats_away.punt_cnt, lastAway.stats_away.pos_time
			# 		print lastHome.stats_away.total_yds, lastHome.stats_away.passing_yds, lastHome.stats_away.rushing_yds, lastHome.stats_away.turnovers, lastHome.stats_away.punt_cnt, lastHome.stats_away.pos_time
			# 	else:
			# 		pass
			# 	print game.away
			# 	print game.home
			# 	# print game.stats_away
			# 	print "Total Yards, Passing Yards, Rushing Yards, Turnovers, Punt Count, Possession Time"
			# 	print game.stats_away.total_yds, game.stats_away.passing_yds, game.stats_away.rushing_yds, game.stats_away.turnovers, game.stats_away.punt_cnt, game.stats_away.pos_time
			# 	print game.stats_home.total_yds, game.stats_home.passing_yds, game.stats_home.rushing_yds, game.stats_home.turnovers, game.stats_home.punt_cnt, game.stats_home.pos_time
