import random
class Plays:
    def __init__(self,game):
        """
        Query all rows in the tasks table
        param conn: the Connection object
        :return:
        """
        self.home_team = game.home_team
        self.away_team = game.away_team

    def determine_play(self):
        plays = ['pass','run']
        play = random.choice(plays)
        return play

    def running(self):
        running = random.randrange(5)
        return running

    def passing(self):
        passing = random.randrange(15)
        return passing

    def runoff(self):
        # need to remember previous play and stop clock or runoff, find length of playclock
        runoff = random.randrange(25)
        return runoff