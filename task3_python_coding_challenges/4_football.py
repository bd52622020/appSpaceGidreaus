import random


taunt = {"You suck!"}
good_comments = { "Amazing performance!", "Nice plays!"}
bad_comments = {"No defense...", "They are playing so bad."}

def team(team, games, wins, losses):

	draws = games - wins - losses
	points = wins*3 + draws

	if wins/games > 0.35 :
		comment = random.choice(list(good_comments))
	else:
		comment = random.choice(list(bad_comments))

	print(team, " points:", points, random.choice(list(taunt)), comment )


team("liverpool", 30, 15, 5)
