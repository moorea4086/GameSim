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

# input absolute location and return %50 location
    def ballLocation(self, absoluteLocation):
        # 0 for own side, 1 for opponents side of the field
        if (absoluteLocation > 50):
            tempYard = 100-50
            opponentSide = 50-tempYard
            return [1,opponentSide]
        else: return [0,absoluteLocation]

    def min_sec(self):
        #str(self.clock//60)+":"+str(self.clock%60)
        return(str(self.clock//60)+":"+str(self.clock%60))

    def possession(self):
        self.possession = team

    def first_down(self):
        print("("+ self.min_sec() +")", self.possession, "ball, first and", self.yards_to_go)
        play_type = self.play.determine_play()
        play_length = self.play.runoff()
        if play_type == 'run': play_distance = self.play.running()
        else: play_distance = self.play.passing()
        print(self.possession,"decide to",play_type,"the ball for",play_distance,"yards")
        self.clock = self.clock - play_length
        #newminsec = self.min_sec()
        self.yards_to_go = self.yards_to_go - play_distance
        if self.yards_to_go > 0: 
            self.down = 2
        else: self.down = 1
        

    def second_down(self):
        print("(" + self.min_sec() + ")", self.possession, "ball, second and", self.yards_to_go)
        play_type = self.play.determine_play()
        play_length = self.play.runoff()
        if play_type == 'run': play_distance = self.play.running()
        else: play_distance = self.play.passing()
        print(self.possession,"decide to",play_type,"the ball for",play_distance,"yards")
        self.clock = self.clock - play_length
        #newminsec = self.min_sec()
        self.yards_to_go = self.yards_to_go - play_distance
        if self.yards_to_go > 0: 
            self.down = 3
        else: self.down = 1

    def third_down(self):
        print("(" + self.min_sec() + ")", self.possession, "ball, third and", self.yards_to_go)

    def fourth_down(self):
        print("(" + self.min_sec() + ")", self.possession, "ball, fourth and", self.yards_to_go)
