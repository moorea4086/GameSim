import random
import sys
class Plays:
    def __init__(self,game,stats):
        """
        Query all rows in the tasks table
        param conn: the Connection object
        :return:
        """
        self.home_team = game.home_team
        self.away_team = game.away_team
        self.home_starters = stats.home_starters
        self.away_starters = stats.away_starters
        self.home_strategy = 'neutral'
        self.away_strategy = 'neutral'
        self.stats = stats
        sys.stdout = open(r"C:\Users\Alex\Desktop\gamebook.txt","w+")

    def runoff_snapclock(self, strategy):
        if strategy == "timekill":
            runoff = random.randint(30,39)
        elif strategy == "twominute":
            runoff = random.randint(5,15)
        elif strategy == "neutral":
            runoff = random.randint(10,30)
        elif strategy == "aggressive":
            runoff = random.randint(5,15)
        return runoff

    def runoff_play(self):
        # need to remember previous play and stop clock or runoff, find length of playclock
        runoff = random.randint(4,12)
        return runoff

    def runoff(self,previous_play,poss):
        if poss == self.home_team:
            snap = self.runoff_snapclock(self.home_strategy)
        else:
            snap = self.runoff_snapclock(self.away_strategy)
        play = self.runoff_play()
        if previous_play == 'pass' and self.play == 'incomplete':
            clock_runoff = play
        elif previous_play == 'kickoff':
            clock_runoff = play
        elif previous_play == 'timeout':
            clock_runoff = play
        elif previous_play == 'start_of_quarter':
            clock_runoff = 0
        elif previous_play == 'touchback':
            clock_runoff = 0
        elif previous_play == 'field_goal':
            clock_runoff = snap
        elif previous_play == 'change_of_possession':
            clock_runoff = play
        else:
            clock_runoff = snap + play
        return clock_runoff

    def determine_play(self):
        plays = ['pass','run']
        play = random.choice(plays)
        return play

    def get_running_back(self,poss):
        # use situational statistics
        if poss == self.home_team:
            rb = self.home_starters["RB"]
        else:
            rb = self.away_starters["RB"]
        self.running_back = rb

    def running_yards(self,absolute_position):
        # use situational statistics
        # https://forums.footballguys.com/forum/topic/401561-why-rushing-yards-are-worth-more-than-passing-yards/
        self.run = int(random.gauss(4.28, 3))
        if absolute_position + self.run > 100: self.run = 100 - absolute_position
        return self.run

    def run_output(self):
        print(self.running_back + " takes the ball ", self.run, " yards on the play")
        #self.f.write(self.running_back + " takes the ball ", self.run, " yards on the play")
        self.stats.rb_yards(self.running_back,self.run)
    
    # change to get_qb, passing_attempt
    def passing(self,poss):
        # use situational statistics
        plays = ('complete','incomplete')
        #self.play = random.choice(plays)
        #https://docs.python.org/3/library/random.html#examples-and-recipes
        #choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5
        #print(random.choices(plays, cum_weights=(0.65, 1.00), k = 1))
        if random.choices(plays, cum_weights=(0.65, 1.00), k = 1) == ['complete']:
            self.play = 'complete'
        else: self.play = 'incomplete'
        xyz = ['X','Y','Z','TE','RB']
        self.xyz = random.choice(xyz)

        if poss == self.home_team:
            qb = self.home_starters["QB"]
            wr = self.home_starters[self.xyz]
        else:
            qb = self.away_starters["QB"]
            wr = self.away_starters[self.xyz]
        self.quarterback = qb
        self.wide_receiver = wr

        if self.play == 'complete':
            self.stats.qb_attempt(self.quarterback)
            self.stats.qb_completion(self.quarterback)
        else:
            self.stats.qb_attempt(self.quarterback)

        return self.play

    def pass_air_yards(self,poss,absolute_position):
        self.pass_air = random.randrange(15)
        if absolute_position + self.pass_air > 100: self.pass_air = 100 - absolute_position

        #print (self.quarterback + " passes to " + self.wide_receiver + " for ", passing, " yards")
        #return passing

    def pass_yac(self,poss,absolute_position):
        self.yac = random.randrange(10)
        #print (self.wide_receiver + " runs for ", yac, " additonal yards")
        self.passing_gain_on_play = self.pass_air + self.yac
        if self.passing_gain_on_play + absolute_position > 100: 
            self.yac = 100 - (self.pass_air + absolute_position)
            self.passing_gain_on_play = self.pass_air + self.yac
        self.stats.qb_yards(self.quarterback,self.passing_gain_on_play)
        #return passing_gain_on_play

    def pass_output(self):
        if self.play == 'complete':
            print (self.quarterback + " passes ", self.pass_air, "to " + self.wide_receiver + " who runs for an additional", self.yac, " yards")
            print ("Gain of ", self.passing_gain_on_play, " yards on the play")
            #self.f.write(self.quarterback + " passes ", self.pass_air, "to " + self.wide_receiver + " who runs for an additional", self.yac, " yards")
            #self.f.write("Gain of ", self.passing_gain_on_play, " yards on the play")
            self.stats.receiver_receptions(self.wide_receiver)
            self.stats.receiver_yards(self.wide_receiver, self.passing_gain_on_play)
        else:
            print (self.quarterback + " throws an incomplete pass. " + self.wide_receiver + " was the intended target")
            #self.f.write(self.quarterback + " throws an incomplete pass. " + self.wide_receiver + " was the intended target")
            self.passing_gain_on_play = 0
        return self.passing_gain_on_play

    def punt(self, poss):
        punt = random.randint(20,40)
        if poss == self.home_team:
            punter = self.home_starters["P"]
        else:
            punter = self.away_starters["P"]
        print (punter + " punts ", end = " ")
        #self.f.write(punter + " punts ", end = " ")
        return punt

    def punt_return(self, poss):
        punt_return_distance = random.randrange(15)
        if poss == self.home_team:
            return_man = self.home_starters["PR"]
        else:
            return_man = self.away_starters["PR"]
        print (return_man + " returns the ball ", end = " ")
        #self.f.write(return_man + " returns the ball ", end = " ")
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

    def get_placekicker(self, poss):
        if poss == self.home_team:
            kicker = self.home_starters["PK"]
        else:
            kicker = self.away_starters["PK"]
        self.placekicker = kicker
        #print (kicker + " kicks off ")
        #return kickoff

    def kickoff(self):
        self.kickoff_distance = random.randint(38,50)
        return self.kickoff_distance

    def kickoff_output(self, ball_location):
        self.start_of_kickoff_return = ball_location[1]
        print (self.placekicker + " kicks the ball", self.kickoff_distance, "yards to the ", self.start_of_kickoff_return , " yard line.")
        #self.f.write(self.placekicker + " kicks the ball", self.kickoff_distance, "yards to the ", self.start_of_kickoff_return , " yard line.")
    
    def get_kickoff_return_man(self, poss):
        if poss == self.home_team:
            return_man = self.home_starters["KR"]
        else:
            return_man = self.away_starters["KR"]
        self.kickoff_return_man = return_man

    def kickoff_return_yards(self,poss):        
        #startOfReturn = 65-self.kickoff_distance 
        # 0 is own side of field 
        self.kick_return_distance = random.randrange(15)

    def kickoff_return_output(self):
        print(self.kickoff_return_man + " returns the ball ", self.kick_return_distance, " yards")
        #self.f.write(self.kickoff_return_man + " returns the ball ", self.kick_return_distance, " yards")
        absolute_location = self.start_of_kickoff_return + self.kick_return_distance
        return absolute_location

# Put into a definition of PlayYardage
    #def kickoffDistance(kicker):
    #    # random number based on mean
    #    return 45

    #def kickoffReturn(return_man):
    #    # random number based on mean and std
    #    # or touchback
    #    kick_return_distance = random.randrange(15)
    #    return kick_return_distance

    def xp_attempt(self):
        self.xp = 'GOOD'
        return self.xp

    def xp_attempt_output(self):
        print("The kick by " + self.placekicker + " is up, it is " + self.xp)
        #self.f.write("The kick by " + self.placekicker + " is up, it is " + self.xp)

