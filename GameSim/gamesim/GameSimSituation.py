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
        #self.ball_location = 0
        #self.absolute_location = 0

# input absolute location and return %50 location
    def ballLocation(self, absolute_position):
        # 0 for own side, 1 for opponents side of the field
        if (absolute_position > 50):
            tempYard = absolute_position-50
            opponentSide = 50-tempYard
            return [1,opponentSide]
        else: return [0,absolute_position]

    def min_sec(self):
        #str(self.clock//60)+":"+str(self.clock%60)
        minutes = str(self.clock//60)
        seconds = self.clock%60
        if seconds < 10: seconds = "0" + str(self.clock%60)
        else: seconds = str(seconds)
        return(minutes + ":" + seconds)

    def possession(self):
        self.possession = team

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
    # make sure i can return for a TD
    def first_down_after_kick(self,absolute_location):
        self.ball_location = self.ballLocation(absolute_location)
        print("("+ self.min_sec() +")", self.possession, "ball at the " + str(self.ball_location[1]) + ", first and", self.yards_to_go)
        play_type = self.play.determine_play()
        play_length = self.play.runoff()
        if play_type == 'run': play_distance = self.play.running(self.possession)
        else: play_distance = self.play.passing(self.possession)
        #print(self.possession,"decide to",play_type,"the ball for",play_distance,"yards")
        print(" for",play_distance,"yards")
        self.clock = self.clock - play_length
        #newminsec = self.min_sec()
        self.yards_to_go = self.yards_to_go - play_distance
        self.absolute_location = absolute_location + play_distance
        if self.yards_to_go > 0: 
            self.down = 2
        else: 
            self.yards_to_go = 10
            self.down = 1

    def first_down(self):
        self.ball_location = self.ballLocation(self.absolute_location)
        print("("+ self.min_sec() +")", self.possession, "ball at the " + str(self.ball_location[1]) + ", first and", self.yards_to_go)
        play_type = self.play.determine_play()
        play_length = self.play.runoff()
        if play_type == 'run': play_distance = self.play.running(self.possession)
        else: play_distance = self.play.passing(self.possession)
        #print(self.possession,"decide to",play_type,"the ball for",play_distance,"yards")
        if play_distance >= self.ball_location[1] and self.ball_location[0] == 1:
            self.score(self.touchdown)
            self.clock = self.clock - play_length
        else:
            print("for",play_distance,"yards")
            self.clock = self.clock - play_length
            self.yards_to_go = self.yards_to_go - play_distance
            self.absolute_location = self.absolute_location + play_distance
            if self.yards_to_go > 0: 
                self.down = 2
            else: 
                self.yards_to_go = 10
                self.down = 1
        

    def second_down(self):
        self.ball_location = self.ballLocation(self.absolute_location)
        print("("+ self.min_sec() +")", self.possession, "ball at the " + str(self.ball_location[1]) + ", second and", self.yards_to_go)
        play_type = self.play.determine_play()
        play_length = self.play.runoff()
        if play_type == 'run': play_distance = self.play.running(self.possession)
        else: play_distance = self.play.passing(self.possession)
        #print(self.possession,"decide to",play_type,"the ball for",play_distance,"yards")
        if play_distance >= self.ball_location[1] and self.ball_location[0] == 1:
            self.score(self.touchdown)
            self.clock = self.clock - play_length
        else:
            print("for",play_distance,"yards")
            self.clock = self.clock - play_length
            self.yards_to_go = self.yards_to_go - play_distance
            self.absolute_location = self.absolute_location + play_distance
            if self.yards_to_go > 0: 
                self.down = 3
            else: 
                self.yards_to_go = 10
                self.down = 1

    def third_down(self):
        self.ball_location = self.ballLocation(self.absolute_location)
        print("("+ self.min_sec() +")", self.possession, "ball at the " + str(self.ball_location[1]) + ", third and", self.yards_to_go)
        play_type = self.play.determine_play()
        play_length = self.play.runoff()
        if play_type == 'run': play_distance = self.play.running(self.possession)
        else: play_distance = self.play.passing(self.possession)
        #print(self.possession,"decide to",play_type,"the ball for",play_distance,"yards")
        if play_distance >= self.ball_location[1] and self.ball_location[0] == 1:
            self.score(self.touchdown)
            self.clock = self.clock - play_length
        else:
            print("for",play_distance,"yards")
            self.clock = self.clock - play_length
            self.yards_to_go = self.yards_to_go - play_distance
            self.absolute_location = self.absolute_location + play_distance
            if self.yards_to_go > 0: 
                self.down = 4
            else: 
                self.yards_to_go = 10
                self.down = 1

    def fourth_down(self):
        print("(" + self.min_sec() + ")", self.possession, "ball, fourth and", self.yards_to_go)
        # kickoff or go for it
        self.ball_location = self.ballLocation(self.absolute_location)
        if self.ball_location[1]<40 and self.ball_location[0] == 1: 
            self.score(self.field_goal)
        else: 
            punt_distance = self.play.punt(self.possession)
            self.absolute_location = self.absolute_location + punt_distance
            self.ball_location = self.ballLocation(self.absolute_location)
                  
            if self.ball_location[1] < 0:             
                self.ball_location[0] = 0
                self.ball_location[1] = 20
                print(" into the endzone. Touchback")
                self.change_of_possession()  
            else:
                print(punt_distance, " yards ", end = " ")
                #self.absolute_location = self.absolute_location + punt_distance
                #self.ball_location = self.ballLocation(self.absolute_location)
                print(" to the ", self.ball_location[1]," yard line")
                self.change_of_possession()
                return_distance = self.play.punt_return(self.possession)
                self.absolute_location = self.absolute_location + return_distance
                self.ball_location = self.ballLocation(self.absolute_location)
                print(return_distance, "yards to the ",self.ball_location[1]," yard line")
        play_length = self.play.runoff()
        

    def score(self, type):
        if type == 'field goal':
           outcome = self.play.field_goal_attempt(self.possession)
           if outcome == 'makes':
               print (outcome + " the field goal") 
               # kickoff
               kickoff_distance = self.play.kickoff(self.possession)
               print("Kick goes ", kickoff_distance, " yards", end = " ")
               self.change_of_possession() 
               self.absolute_location = 65 - kickoff_distance
               self.ball_location = self.ballLocation(self.absolute_location)
               print(" to the ", self.ball_location[1],"yard line")
               return_distance = self.play.kickoff_return(self.possession,kickoff_distance)
               print("Return goes ", return_distance, " yards", end = " ")
               self.absolute_location = self.absolute_location+return_distance
               self.ball_location = self.ballLocation(self.absolute_location)
               print(" to the ", self.ball_location[1],"yard line")
           else:
               print (outcome + " the field goal")
               self.change_of_possession()
 
        else:
           print("into the endzone. Touchdown!")
               # add 6 to the score, kick a XP
               # kickoff
           kickoff_distance = self.play.kickoff(self.possession)
           print("Kick goes ", kickoff_distance, " yards", end = " ")
           self.change_of_possession()  ####
           self.absolute_location = 65 - kickoff_distance
           self.ball_location = self.ballLocation(self.absolute_location)
           print(" to the ", self.ball_location[1],"yard line")
           return_distance = self.play.kickoff_return(self.possession,kickoff_distance)
           print("Return goes ", return_distance, " yards", end = " ")
           self.absolute_location = self.absolute_location+return_distance
           self.ball_location = self.ballLocation(self.absolute_location)
           print(" to the ", self.ball_location[1],"yard line")