# the field is left to right 0 to 100

class Kickoff:
    def __init__(self,game,home_team,away_team,home_starters,away_starters):
        """
        Query all rows in the tasks table
        param conn: the Connection object
        :return:
        """
        self.home_team = home_team
        self.away_team = away_team
        self.home_starters = home_starters
        self.away_starters = away_starters
        self.first_possession_second = game.first_possession_second
        self.first_possession = game.first_possession

    def opening_kickoff(self):
        self.kicking_team = self.first_possession_second
        self.receiving_team = self.first_possession

        if self.home_team == self.kicking_team:
            self.kicker = self.home_starters["PK"]
            self.returner = self.away_starters["KR"]
        else:
            self.kicker = self.away_starters["PK"]
            self.returner = self.home_starters["KR"] 

        # kickoff is from 35 yard line (of right side, with the field going left to right), so 100-35=65
        self.distance = Kickoff.kickoffDistance(self.kicker)
        #return distance

    def kickoff_return(self):
        
        startOfReturn = 65-self.distance   
        # commented because of situation conflict, send startOfReturn to situation
        # footballLocation = situation.ballLocation(startOfReturn)
        # 0 is own side of field

        return_yards = Kickoff.kickoffReturn(self.returner)
        endOfReturn = startOfReturn+return_yards

        # if the kickoff travels onto the opponenent's side of the field (it should)
        # commented because of reference to footballLocation which references situation
        #if footballLocation[0] == 0:
        #    print(self.kicker + " of the " + kicking_team + " kicks the ball " + str(distance) + " yards to the " + receiving_team + " " + str(footballLocation[1]) + " yard line.")
        #else:
        #    print(self.kicker + " of the " + kicking_team + " kicks the ball " + str(distance) + " yards to the " + kicking_team + " " + str(footballLocation[1]) + " yard line.")

        print(self.kicker + " of the " + self.kicking_team + " kicks the ball " + str(self.distance) + " yards to the " + self.receiving_team + " " + str(startOfReturn) + " yard line.")

        # the return
        print(self.returner + " of the "+ self.receiving_team + " returns the ball " + str(return_yards) + " yards")
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
    def kickoffDistance(kicker):
        # random number based on mean
        return 45

    def kickoffReturn(return_man):
        # random number based on mean and std
        # or touchback
        return 15





