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
        print (kicker, end = " ")
        return outcome

    def kickoff(self, poss):
        kickoff = random.randint(38,50)
        if poss == self.home_team:
            kicker = self.home_starters["PK"]
        else:
            kicker = self.away_starters["PK"]
        print (kicker + " kicks off ")
        return kickoff

   #def opening_kickoff(self):
   #     self.kicking_team = self.first_possession_second
   #     self.receiving_team = self.first_possession

   #     if self.home_team == self.kicking_team:
   #         self.kicker = self.home_starters["PK"]
   #         self.returner = self.away_starters["KR"]
   #     else:
   #         self.kicker = self.away_starters["PK"]
   #         self.returner = self.home_starters["KR"] 

   #     # kickoff is from 35 yard line (of right side, with the field going left to right), so 100-35=65
   #     self.distance = Kickoff.kickoffDistance(self.kicker)
   #     #return distance

    def kickoff_return(self, poss, kickoff_distance):
        
        startOfReturn = 65-kickoff_distance 
        # commented because of situation conflict, send startOfReturn to situation
        # footballLocation = situation.ballLocation(startOfReturn)
        # 0 is own side of field
        if poss == self.home_team:
            return_man = self.home_starters["KR"]
        else:
            return_man = self.away_starters["KR"]
        return_yards = Plays.kickoffReturn(return_man)
        endOfReturn = startOfReturn+return_yards

        # if the kickoff travels onto the opponenent's side of the field (it should)
        # commented because of reference to footballLocation which references situation
        #if footballLocation[0] == 0:
        #    print(self.kicker + " of the " + kicking_team + " kicks the ball " + str(distance) + " yards to the " + receiving_team + " " + str(footballLocation[1]) + " yard line.")
        #else:
        #    print(self.kicker + " of the " + kicking_team + " kicks the ball " + str(distance) + " yards to the " + kicking_team + " " + str(footballLocation[1]) + " yard line.")

        #print(self.kicker + " of the " + self.kicking_team + " kicks the ball " + str(self.distance) + " yards to the " + self.receiving_team + " " + str(startOfReturn) + " yard line.")

        # the return
        #print(self.returner + " of the "+ self.receiving_team + " returns the ball " + str(return_yards) + " yards")
        # the %50 location of the football (as opposed to the absolute 0-100 position of the football)
        #footballLocation = situation.ballLocation(endOfReturn)
        # 0 is the receiving team's side of field
        #if footballLocation[0] == 0:
        #    print(receiving_team + " ball at the " + receiving_team + " " + str(footballLocation[1]) + " yard line.")
        #else:
        #    print(receiving_team + " ball at the " + kicking_team + " " + str(footballLocation[1]) + " yard line.")

        #situation.clock = situation.clock - 15
        #situation.min_sec()
        return endOfReturn
        #print(game.clock)

# Put into a definition of PlayYardage
    #def kickoffDistance(kicker):
    #    # random number based on mean
    #    return 45

    def kickoffReturn(return_man):
        # random number based on mean and std
        # or touchback
        kick_return_distance = random.randrange(15)
        return kick_return_distance