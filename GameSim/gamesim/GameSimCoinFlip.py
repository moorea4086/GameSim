import random
import sys
sys.path.append(r"C:\Users\Alex\Desktop\GameSim")
from GameSimDatabaseConnection import Database 

from GameSimPlayers import Home_Starters
from GameSimPlayers import Away_Starters
from GameSimKickoff import Kickoff
from GameSimPlays import Plays
from GameSimSituation import Situation
from GameSimStats import Stats

class Game:

#https://stackoverflow.com/questions/14882530/python-coin-toss (Rushy Panchel)
    def __init__(self,home_team,away_team):
        """
        Query all rows in the tasks table
        param conn: the Connection object
        :return:
        """
        self.home_team = home_team
        self.away_team = away_team

    def coinToss(self):
        sides = ['heads','tails']
        print(self.away_team + ", heads or tails")
        kick_or_receive = input().strip()
        flip = random.choice(sides)
        if (flip == "heads"):        
            print("It is Heads")
        else:
            print("It is Tails")
        if (flip == kick_or_receive):
            self.coinFlipWinner = self.away_team
        else:
            self.coinFlipWinner = self.home_team

    def firstHalfChoice(self):
        print (self.coinFlipWinner + " elect to...(R or K)")
        self.kick_or_receive = input().strip()
        
        if (self.kick_or_receive == "R"):        
            print(self.coinFlipWinner + " will receive")
        else:
            print(self.coinFlipWinner + " will kick")

    def firstPossession(self):
        if (self.kick_or_receive == "K" and self.coinFlipWinner == self.away_team): self.first_possession = self.home_team
        elif (self.kick_or_receive == "K" and self.coinFlipWinner == self.home_team): self.first_possession = self.away_team
        elif (self.kick_or_receive == "R" and self.coinFlipWinner == self.away_team): self.first_possession = self.away_team
        elif (self.kick_or_receive == "R" and self.coinFlipWinner == self.home_team): self.first_possession = self.home_team

    def firstPossession_SecondHalf(self):
        if (self.kick_or_receive == "K" and self.coinFlipWinner == self.away_team): self.first_possession_second = self.away_team
        elif (self.kick_or_receive == "K" and self.coinFlipWinner == self.home_team): self.first_possession_second = self.home_team
        elif (self.kick_or_receive == "R" and self.coinFlipWinner == self.away_team): self.first_possession_second = self.home_team
        elif (self.kick_or_receive == "R" and self.coinFlipWinner == self.home_team): self.first_possession_second = self.away_team
        print(self.first_possession_second + " will receive the ball to start the second half")



def main():
# obtain players, name Captains

        print("Enter the home team")
        homeTeam = input().strip()
        print("Enter the visiting team")
        awayTeam = input().strip()
        game = Game(homeTeam,awayTeam)

        database = r"C:\Users\Alex\Desktop\2019DepthChart\Rosters2019.db"
        conn = Database(database)
# initialize
        home_start = Home_Starters(conn, game.home_team)
        away_start = Away_Starters(conn, game.away_team)
# create rosters as globals
        home_starters = home_start.roster()
        away_starters = away_start.roster()

        game.coinToss()
        game.firstHalfChoice()
        game.firstPossession()
        game.firstPossession_SecondHalf()

        stats = Stats(home_starters, away_starters, homeTeam, awayTeam)
        play = Plays(game,stats)
        situation = Situation(play)
        kickoff = Kickoff(game, homeTeam, awayTeam,home_starters,away_starters)
        print("("+ situation.min_sec() +")", end = " ") ######
# make this opening kickoff as opposed to a kickoff after a score
        kickoff.half = 'First'
        kickoff.opening_kickoff()
        starting_field_position = kickoff.kickoff_return()
        situation.play_type = 'kickoff'
        situation.quarter = 'first'
# find out which team ends up with the ball and set game.possession
        situation.possession = game.first_possession

# set the situation.absolute_location directly and eliminated the method situation.first_down_after_kick
        #situation.first_down_after_kick(starting_field_position)
        situation.absolute_location = starting_field_position
# put this in a function and add any additional loops
        while situation.clock > 0:
            if situation.down == 1: situation.first_down()
            elif situation.down == 2: situation.second_down()
            elif situation.down == 3: situation.third_down()
            elif situation.down == 4: situation.fourth_down()
            else: break
        print("End of first")
        situation.clock = 900
        situation.quarter = 'second'
        situation.play_type = 'start_of_quarter'
        while situation.clock > 0:
            if situation.down == 1: situation.first_down()
            elif situation.down == 2: situation.second_down()
            elif situation.down == 3: situation.third_down()
            elif situation.down == 4: situation.fourth_down()
            # if a touchdown or field goal was scored as the last play of the previous quarter
            elif situation.down == 0: situation.kickoff_sequence()
            else: break
        print("Half Time")
        situation.clock = 900
        situation.quarter = 'third'
        kickoff.half = "Second"
        print("("+ situation.min_sec() +")", end = " ")
        kickoff.opening_kickoff()
        starting_field_position = kickoff.kickoff_return()
        situation.absolute_location = starting_field_position
        while situation.clock > 0:
            if situation.down == 1: situation.first_down()
            elif situation.down == 2: situation.second_down()
            elif situation.down == 3: situation.third_down()
            elif situation.down == 4: situation.fourth_down()
            else: break
        print("End of third")
        situation.clock = 900
        situation.quarter = 'fourth'
        situation.play_type = 'start_of_quarter'
        while situation.clock > 0:
            if situation.down == 1: situation.first_down()
            elif situation.down == 2: situation.second_down()
            elif situation.down == 3: situation.third_down()
            elif situation.down == 4: situation.fourth_down()
            # if a touchdown or field goal was scored as the last play of the previous quarter
            elif situation.down == 0: situation.kickoff_sequence()
            else: break

        home_qb = stats.get_qb(homeTeam)
        away_qb = stats.get_qb(awayTeam) 
 
        QB_home_attempts = stats.get_qb_attempts(home_qb)
        QB_away_attempts = stats.get_qb_attempts(away_qb)

        QB_home_completions = stats.get_qb_completions(home_qb)
        QB_away_completions = stats.get_qb_completions(away_qb)
        
        QB_home_yards = stats.get_qb_yards(home_qb)
        QB_away_yards = stats.get_qb_yards(away_qb)

        print(home_qb,":", QB_home_completions,"/",QB_home_attempts, "for", QB_home_yards)
        print(away_qb,":", QB_away_completions,"/",QB_away_attempts, "for",QB_away_yards)

        home_rb = stats.get_rb(homeTeam)
        away_rb = stats.get_rb(awayTeam)  

        RB_home_attempts = stats.get_rb_attempts(home_rb)
        RB_away_attempts = stats.get_rb_attempts(away_rb)
        
        RB_home_yards = stats.get_rb_yards(home_rb)
        RB_away_yards = stats.get_rb_yards(away_rb)

        print(home_rb,":", RB_home_attempts, "attempts for", RB_home_yards)
        print(away_rb,":", RB_away_attempts, "attempts for", RB_away_yards)
        
        receiver_array = [stats.home_x_receiver, stats.home_y_receiver, stats.home_z_receiver, stats.away_x_receiver, stats.away_y_receiver, stats.away_z_receiver]
        for receiver in receiver_array:
            print(receiver, ": ", stats.get_receiver_receptions(receiver), " receptions for ", stats.get_receiver_yards(receiver), " yards")
        
        #if situation.clock > 0:
        #    if situation.down == 1: situation.first_down()
        #    elif situation.down == 2: situation.second_down()
        #    elif situation.down == 3: situation.third_down()
        #    elif situation.down == 4: situation.fourth_down()

        #if situation.clock > 0:
        #    if situation.down == 1: situation.first_down()
        #    elif situation.down == 2: situation.second_down()
        #    elif situation.down == 3: situation.third_down()
        #    elif situation.down == 4: situation.fourth_down()

if __name__ == "__main__":
    main()
