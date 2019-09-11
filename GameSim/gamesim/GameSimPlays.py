import random
class Plays:
    def __init__(self,game,home_starters,away_starters):
        """
        Query all rows in the tasks table
        param conn: the Connection object
        :return:
        """
        self.home_team = game.home_team
        self.away_team = game.away_team
        self.home_starters = home_starters
        self.away_starters = away_starters

    def determine_play(self):
        plays = ['pass','run']
        play = random.choice(plays)
        return play

    def running(self,poss):
        running = random.randrange(5)
        if poss == self.home_team:
            rb = self.home_starters["RB"]
        else:
            rb = self.away_starters["RB"]
        print (rb + " runs")
        return running

    def passing(self,poss):
        passing = random.randrange(15)
        return passing

    def runoff(self):
        # need to remember previous play and stop clock or runoff, find length of playclock
        runoff = random.randrange(25)
        return runoff