import random
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
        self.stats = stats

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
        self.run = random.randrange(5)
        if absolute_position + self.run > 100: self.run = 100 - absolute_position
        return self.run

    def run_output(self):
        print(self.running_back + " takes the ball ", self.run, " yards on the play")
        self.stats.rb_yards(self.running_back,self.run)
# change to get_qb, passing_attempt
    def passing(self,poss):
        # use situational statistics
        plays = ['complete','incomplete']
        self.play = random.choice(plays)

        xyz = ['X','Y','Z']
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
            self.stats.receiver_receptions(self.wide_receiver)
            self.stats.receiver_yards(self.wide_receiver, self.passing_gain_on_play)
        else:
            print (self.quarterback + " throws an incomplete pass. " + self.wide_receiver + " was the intended target")
            self.passing_gain_on_play = 0
        return self.passing_gain_on_play

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

    def get_kickoff_return_man(self, poss):
        if poss == self.home_team:
            return_man = self.home_starters["KR"]
        else:
            return_man = self.away_starters["KR"]
        self.kickoff_return_man = return_man

    def kickoff_return_yards(self,poss):        
        #startOfReturn = 65-self.kickoff_distance 
        # commented because of situation conflict, send startOfReturn to situation
        # footballLocation = situation.ballLocation(startOfReturn)
        # 0 is own side of field 
        self.kick_return_distance = random.randrange(15)

    def kickoff_return_output(self):
        print(self.kickoff_return_man + " returns the ball ", self.kick_return_distance, " yards")
        absolute_location = self.start_of_kickoff_return + self.kick_return_distance
        return absolute_location

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