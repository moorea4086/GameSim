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
        # use situational statistics
        running = random.randrange(5)
        if poss == self.home_team:
            rb = self.home_starters["RB"]
        else:
            rb = self.away_starters["RB"]
        print (rb + " runs", end = " ")
        return running

    def passing(self,poss):
        # use situational statistics
        passing = random.randrange(15)
        if poss == self.home_team:
            qb = self.home_starters["QB"]
            wr = self.home_starters["WR"]
        else:
            qb = self.away_starters["QB"]
            wr = self.away_starters["WR"]
        print (qb + " passes to " + wr, end = " ")
        return passing

    def runoff(self):
        # need to remember previous play and stop clock or runoff, find length of playclock
        runoff = random.randrange(25)
        return runoff

    def punt(self, poss):
        punt = random.randint(20,40)
        if poss == self.home_team:
            punter = self.home_starters["P"]
        else:
            punter = self.away_starters["P"]
        print (punter + " punts ", end = " ")
        return punt

    def punt_return(self, poss):
        punt_return_distance = random.randrange(15)
        if poss == self.home_team:
            return_man = self.home_starters["PR"]
        else:
            return_man = self.away_starters["PR"]
        print (return_man + " returns the ball ", end = " ")
        return punt_return_distance

    def field_goal_attempt(self, poss):
        # define this as make or miss
        outcomes = ['makes','misses']
        outcome = random.choice(outcomes)
        if poss == self.home_team:
            kicker = self.home_starters["PK"]
        else:
            kicker = self.away_starters["PK"]
        print (kicker + " " + outcome + " the field goal")
        return outcome

    def kickoff(self, poss):
        kickoff = random.randint(38,50)
        if poss == self.home_team:
            kicker = self.home_starters["PK"]
        else:
            kicker = self.away_starters["PK"]
        print (kicker + " kicks ", end = " ")
        return kickoff