# the field is left to right 0 to 100

class Kickoff:
    def __init__(self,home_team,away_team,home_starters,away_starters):
        """
        Query all rows in the tasks table
        param conn: the Connection object
        :return:
        """
        self.home_team = home_team
        self.away_team = away_team
        self.home_starters = home_starters
        self.away_starters = away_starters

    def opening_kickoff(self,game,situation):
        kicking_team = game.first_possession_second
        receiving_team = game.first_possession

        if self.home_team == kicking_team:
            kicker = self.home_starters["PK"]
            returner = self.away_starters["KR"]
        else:
            kicker = self.away_starters["PK"]
            returner = self.home_starters["KR"] 

        # kickoff is from 35 yard line (of right side, with the field going left to right), so 100-35=65
        distance = Kickoff.kickoffDistance(kicker)
        startOfReturn = 65-distance    
        footballLocation = situation.ballLocation(startOfReturn)
        # 0 is own side of field

        yards = Kickoff.kickoffReturn(returner)
        endOfReturn = startOfReturn+yards

        # if the kickoff travels onto the opponenent's side of the field (it should)
        if footballLocation[0] == 0:
            print(kicker + " of the " + kicking_team + " kicks the ball " + str(distance) + " yards to the " + receiving_team + " " + str(footballLocation[1]) + " yard line.")
        else:
            print(kicker + " of the " + kicking_team + " kicks the ball " + str(distance) + " yards to the " + kicking_team + " " + str(footballLocation[1]) + " yard line.")
        # the return
        print(returner + " of the "+ receiving_team + " returns the ball " + str(yards) + " yards")
        # the %50 location of the football (as opposed to the absolute 0-100 position of the football)
        footballLocation = situation.ballLocation(endOfReturn)
        # 0 is the receiving team's side of field
        if footballLocation[0] == 0:
            print(receiving_team + " ball at the " + receiving_team + " " + str(footballLocation[1]) + " yard line.")
        else:
            print(receiving_team + " ball at the " + kicking_team + " " + str(footballLocation[1]) + " yard line.")

        situation.clock = situation.clock - 15
        situation.min_sec()
        #print(game.clock)

# Put into a definition of PlayYardage
    def kickoffDistance(kicker):
        # random number based on mean
        return 45

    def kickoffReturn(return_man):
        # random number based on mean and std
        # or touchback
        return 15





