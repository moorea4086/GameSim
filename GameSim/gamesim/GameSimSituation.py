class Situation:
    def __init__(self, play):
        # 15 minutes (1 quarter) in seconds, 15 * 60 = 900 seconds
        self.clock = 900
        # set the down value to 1 (first down)
        self.down = 1
        self.yards_to_go = 10
        self.home_points = 0
        self.away_points = 0
        self.home_timeouts = 3
        self.away_timeouts = 3
        self.play = play
        self.touchdown = 'touchdown'
        self.field_goal = 'field goal'

# input absolute location and return %50 location
    def ballLocation(self):
        # 0 for own side, 1 for opponents side of the field
        if (self.absolute_location > 50):
            tempYard = self.absolute_location-50
            opponentSide = 50-tempYard
            return [1,opponentSide]
        else: return [0,self.absolute_location]

    def min_sec(self):
        minutes = str(self.clock//60)
        seconds = self.clock%60
        if seconds < 10: seconds = "0" + str(self.clock%60)
        else: seconds = str(seconds)
        return(minutes + ":" + seconds)

    def change_of_possession(self):
        self.down = 1
        self.yards_to_go = 10
        if self.possession == self.play.home_team:
            self.possession = self.play.away_team
        else:
            self.possession = self.play.home_team
        if self.ball_location[0] == 0:
            self.ball_location[0] = 1
        else: 
            self.ball_location[0] = 0
            self.absolute_location = 100 - self.absolute_location

    # make sure i can return for a TD, the only thing different about this is the absolute location param
    #def first_down_after_kick(self,absolute_location):
    #    self.absolute_location = absolute_location
    #    self.ball_location = self.ballLocation()
    #    self.down_and_distance_output()
    #    play_type = self.play.determine_play()
    #    play_length = self.play.runoff()
    #    if play_type == 'run': 
    #        self.play.get_running_back(self.possession)
    #        play_distance = self.play.running_yards()
    #        self.play.run_output()
    #    else: 
    #        completion = self.play.passing(self.possession)
    #        if completion == 'complete':
    #            self.play.pass_air_yards(self.possession)
    #            self.play.pass_yac(self.possession)
    #            play_distance = self.play.pass_output()
    #        else:
    #            play_distance = int(self.play.pass_output())
    #    self.clock = self.clock - play_length
    #    self.yards_to_go = self.yards_to_go - play_distance
    #    self.absolute_location = absolute_location + play_distance
    #    if self.yards_to_go > 0: 
    #        self.down = 2
    #    else: 
    #        self.yards_to_go = 10
    #        self.down = 1

    def first_down(self):
        self.ball_location = self.ballLocation()
        play_length = self.play.runoff(self.play_type,self.possession)
        self.clock = self.clock - play_length
        self.set_strategy()
        #print("Away:"+self.play.away_strategy+"Home:"+self.play.home_strategy)
        if self.clock < 0: return
        self.down_and_distance_output()
        self.play_type = self.play.determine_play()        
        if self.play_type == 'run': 
            self.play.get_running_back(self.possession)
            play_distance = self.play.running_yards(self.absolute_location)
            self.play.run_output()
        else: 
            completion = self.play.passing(self.possession)
            if completion == 'complete':
                self.play.pass_air_yards(self.possession,self.absolute_location)
                self.play.pass_yac(self.possession,self.absolute_location)
                play_distance = self.play.pass_output()
            else:
                play_distance = self.play.pass_output()
        if play_distance >= self.ball_location[1] and self.ball_location[0] == 1:
            self.score(self.touchdown)            
        else:
            self.yards_to_go = self.yards_to_go - play_distance
            self.absolute_location = self.absolute_location + play_distance
            if self.yards_to_go > 0: 
                self.down = 2
            else: 
                self.yards_to_go = 10
                self.down = 1        

    def second_down(self):
        self.ball_location = self.ballLocation()
        play_length = self.play.runoff(self.play_type,self.possession)
        self.clock = self.clock - play_length
        if self.clock < 0: return
        self.down_and_distance_output()
        self.play_type = self.play.determine_play()        
        if self.play_type == 'run': 
            self.play.get_running_back(self.possession)
            play_distance = self.play.running_yards(self.absolute_location)
            self.play.run_output()
        else: 
            completion = self.play.passing(self.possession)
            if completion == 'complete':
                self.play.pass_air_yards(self.possession,self.absolute_location)
                self.play.pass_yac(self.possession,self.absolute_location)
                play_distance = self.play.pass_output()
            else:
                play_distance = self.play.pass_output()
        if play_distance >= self.ball_location[1] and self.ball_location[0] == 1:
            self.score(self.touchdown)
        else:
            self.yards_to_go = self.yards_to_go - play_distance
            self.absolute_location = self.absolute_location + play_distance
            if self.yards_to_go > 0: 
                self.down = 3
            else: 
                self.yards_to_go = 10
                self.down = 1

    def third_down(self):
        self.ball_location = self.ballLocation()
        play_length = self.play.runoff(self.play_type,self.possession)
        self.clock = self.clock - play_length
        if self.clock < 0: return
        self.down_and_distance_output()
        self.play_type = self.play.determine_play()        
        if self.play_type == 'run': 
            self.play.get_running_back(self.possession)
            play_distance = self.play.running_yards(self.absolute_location)
            self.play.run_output()
        else: 
            completion = self.play.passing(self.possession)
            if completion == 'complete':
                self.play.pass_air_yards(self.possession,self.absolute_location)
                self.play.pass_yac(self.possession,self.absolute_location)
                play_distance = self.play.pass_output()
            else:
                play_distance = self.play.pass_output()
        if play_distance >= self.ball_location[1] and self.ball_location[0] == 1:
            self.score(self.touchdown)
        else:
            self.yards_to_go = self.yards_to_go - play_distance
            self.absolute_location = self.absolute_location + play_distance
            if self.yards_to_go > 0: 
                self.down = 4
            else: 
                self.yards_to_go = 10
                self.down = 1

    def fourth_down(self):
        # kickoff or go for it
        self.ball_location = self.ballLocation()
        play_length = self.play.runoff(self.play_type,self.possession)
        self.clock = self.clock - play_length
        if self.clock < 0: return
        self.down_and_distance_output()

        if self.possession == self.play.home_team:
            strategy = self.play.home_strategy
        else:
            strategy = self.play.away_strategy


        if self.absolute_location >= 60 and (strategy == 'neutral' or strategy == 'timekill' or strategy == 'twominute'):            
            self.score(self.field_goal)

        # go for it on opponents side of field when losing big
        elif (self.absolute_location > 80 and strategy == 'aggressive' and self.yards_to_go <= 5) or (self.absolute_location > 70 and strategy == 'aggressive' and self.yards_to_go <= 4) or  (self.absolute_location > 60 and strategy == 'aggressive' and self.yards_to_go <= 3) or (self.absolute_location > 50 and strategy == 'aggressive' and self.yards_to_go <= 2) or strategy == 'lastdrive':            
            self.play_type = self.play.determine_play()        
            if self.play_type == 'run': 
                self.play.get_running_back(self.possession)
                play_distance = self.play.running_yards(self.absolute_location)
                self.play.run_output()
            else: 
                completion = self.play.passing(self.possession)
                if completion == 'complete':
                    self.play.pass_air_yards(self.possession,self.absolute_location)
                    self.play.pass_yac(self.possession,self.absolute_location)
                    play_distance = self.play.pass_output()
                else:
                    play_distance = self.play.pass_output()
            if play_distance >= self.ball_location[1] and self.ball_location[0] == 1:
                self.score(self.touchdown)
            else:
                self.yards_to_go = self.yards_to_go - play_distance
                self.absolute_location = self.absolute_location + play_distance
                if self.yards_to_go > 0: 
                    self.down = 4
                else: 
                    self.yards_to_go = 10
                    self.down = 1  
        
        elif strategy == 'aggressive' and self.absolute_location >= 60:
            self.score(self.field_goal)

        # punt when reasonable
        elif self.absolute_location < 60: 
            punt_distance = self.play.punt(self.possession)
            self.absolute_location = self.absolute_location + punt_distance
            self.ball_location = self.ballLocation()
                  
            if self.ball_location[1] < 0:             
                self.ball_location[0] = 0
                self.ball_location[1] = 20
                print(" into the endzone. Touchback")
                self.change_of_possession()  
            else:
                print(punt_distance, " yards ", end = " ")
                print(" to the ", self.ball_location[1]," yard line")
                self.change_of_possession()
                return_distance = self.play.punt_return(self.possession)
                self.absolute_location = self.absolute_location + return_distance
                self.ball_location = self.ballLocation()
                print(return_distance, "yards to the ",self.ball_location[1]," yard line")

        else:
            print("ERROR!!!")

    def down_and_distance_output(self):
        if self.down == 1: down = "First"
        elif self.down == 2: down = "Second"
        elif self.down == 3: down = "Third"
        elif self.down == 4: down = "Fourth"
        # self.ball_location[0] means opponents side of the field, absolute_location means they've covered 89 yards of the field
        if self.ball_location[0] == 1 and self.absolute_location > 89:
            print("("+ self.min_sec() +")", self.possession, "ball at the " + str(self.ball_location[1]) + ", ", down, "and goal to go")
        else:
            print("("+ self.min_sec() +")", self.possession, "ball at the " + str(self.ball_location[1]) + ", ", down, "and", self.yards_to_go)

    def score(self, type):
        if type == 'field goal':
            outcome = self.play.field_goal_attempt(self.possession)
            if outcome == 'makes':
                print (outcome + " the field goal") 
                if self.possession == self.play.home_team:
                    self.home_points = self.home_points + 3
                else:
                    self.away_points = self.away_points + 3
                self.play_type = 'field_goal'
                self.score_output()
                play_length = self.play.runoff(self.play_type,self.possession)
                self.clock = self.clock - play_length
                # if the field goal occured at the end of the period
                if self.clock > 0:
                   self.kickoff_sequence()
                else:
                   self.down = 0
            
            else:
               print (outcome + " the field goal")
               self.play_type = 'field_goal'
               self.change_of_possession()

            if self.clock < 0: return
 
        else:
           #self.play_type = 'touchdown'
           print("TOUCHDOWN!")
               # add 6 to the score, kick a XP
               # kickoff
           # https://operations.nfl.com/the-rules/2019-nfl-rulebook/#section-41-try
           self.play.get_placekicker(self.possession)
           xp = self.play.xp_attempt()
           self.play.xp_attempt_output()
           if self.possession == self.play.home_team:
               if xp == 'GOOD':
                   self.home_points = self.home_points + 7
               else:
                   self.home_points = self.home_points + 6
           else:
               if xp == 'GOOD':
                   self.away_points = self.away_points + 7
               else:
                   self.away_points = self.away_points + 6
           #self.play_type = 'xp_attempt'
           #self.play_type = 'change_of_possession'
           self.score_output()
           play_length = self.play.runoff(self.play_type,self.possession)
           self.clock = self.clock - play_length

           # if the TD occured at the end of the period
           if self.clock > 0:
               self.kickoff_sequence()
           else:
               self.down = 0
           if self.clock < 0: return

    def score_output(self):
           print("The score is: ")
           print(self.play.home_team + " ", self.home_points)
           print(self.play.away_team + " ", self.away_points)

    def kickoff_sequence(self):
           #play_length = self.play.runoff(self.play_type,self.possession)
           #self.clock = self.clock - play_length
           if self.clock < 0: return

           self.play.get_placekicker(self.possession)
           #print("Kick goes ", kickoff_distance, " yards", end = " ")
           kickoff_distance = self.play.kickoff()
           self.change_of_possession() 
           self.absolute_location = 65 - kickoff_distance
           self.ball_location = self.ballLocation()


           print("("+ self.min_sec() +")",end = " ")
           self.play.kickoff_output(self.ball_location)
           #print(" to the ", self.ball_location[1],"yard line")
           #return_distance = self.play.kickoff_return(self.possession,kickoff_distance)
           #print("Return goes ", return_distance, " yards", end = " ")
           self.play.get_kickoff_return_man(self.possession)
           self.play.kickoff_return_yards(self.possession)
           self.absolute_location = self.play.kickoff_return_output()
           #self.absolute_location = self.absolute_location+return_distance
           self.ball_location = self.ballLocation()

    def set_strategy(self):
        if self.possession == self.play.home_team:
            if self.quarter == 'first' and self.clock > 120: self.play.home_strategy = 'neutral'
            elif self.quarter == 'first' and self.clock < 120: self.play.home_strategy = 'twominute'
            elif self.quarter == 'second' and self.home_points - self.away_points > 10: 
                self.play.home_strategy = 'timekill'
                if self.clock < 120: self.play.home_strategy = 'twominute'
            elif self.quarter == 'second' and self.home_points - self.away_points >= -10: 
                self.play.home_strategy = 'neutral'
                if self.clock < 120: self.play.home_strategy = 'twominute'
            elif self.quarter == 'second' and self.home_points - self.away_points < -10: 
                self.play.home_strategy = 'aggressive'
            elif self.quarter == 'third' and self.home_points - self.away_points > 7: 
                self.play.home_strategy = 'timekill'
                if self.clock < 120: self.play.home_strategy = 'twominute'
            elif self.quarter == 'third' and self.home_points - self.away_points >= -7: 
                self.play.home_strategy = 'neutral'
                if self.clock < 120: self.play.home_strategy = 'twominute'
            elif self.quarter == 'third' and self.home_points - self.away_points < -7: 
                self.play.home_strategy = 'aggressive'

            elif self.quarter == 'fourth' and self.clock < 240:
                if self.home_points - self.away_points > 0: self.play.home_strategy = 'timekill'
                else: self.play.home_strategy = 'lastdrive'

            elif self.quarter == 'fourth' and self.home_points - self.away_points > 7: 
                self.play.home_strategy = 'timekill'
                if self.clock < 120: self.play.home_strategy = 'twominute'
            elif self.quarter == 'fourth' and self.home_points - self.away_points >= -7: 
                self.play.home_strategy = 'neutral'
                if self.clock < 240: self.play.home_strategy = 'lastdrive'
            elif self.quarter == 'fourth' and self.home_points - self.away_points < -7: 
                self.play.home_strategy = 'aggressive'
                if self.clock < 240: self.play.home_strategy = 'lastdrive'
        elif self.possession == self.play.away_team:
            if self.quarter == 'first' and self.clock > 120: self.play.away_strategy = 'neutral'
            elif self.quarter == 'first' and self.clock < 120: self.play.away_strategy = 'twominute'
            elif self.quarter == 'second' and self.away_points - self.home_points > 10: 
                self.play.away_strategy = 'timekill'
                if self.clock < 120: self.play.away_strategy = 'twominute'
            elif self.quarter == 'second' and self.away_points - self.home_points >= -10: 
                self.play.away_strategy = 'neutral'
                if self.clock < 120: self.play.away_strategy = 'twominute'
            elif self.quarter == 'second' and self.away_points - self.home_points < -10: 
                self.play.away_strategy = 'aggressive'
            elif self.quarter == 'third' and self.away_points - self.home_points > 7: 
                self.play.away_strategy = 'timekill'
                if self.clock < 120: self.play.away_strategy = 'twominute'
            elif self.quarter == 'third' and self.away_points - self.home_points >= -7: 
                self.play.away_strategy = 'neutral'
                if self.clock < 120: self.play.away_strategy = 'twominute'
            elif self.quarter == 'third' and self.away_points - self.home_points < -7: 
                self.play.away_strategy = 'aggressive'

            elif self.quarter == 'fourth' and self.clock < 240:
                if self.away_points - self.home_points > 0: self.play.away_strategy = 'timekill'
                else: self.play.away_strategy = 'lastdrive'

            elif self.quarter == 'fourth' and self.away_points - self.home_points > 7: 
                self.play.away_strategy = 'timekill'
                #if self.clock < 120: self.play.away_strategy = 'twominute'
            elif self.quarter == 'fourth' and self.away_points - self.home_points >= -7: 
                self.play.away_strategy = 'neutral'
            elif self.quarter == 'fourth' and self.away_points - self.home_points < -7: 
                self.play.away_strategy = 'aggressive'