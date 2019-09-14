import random
import sys
sys.path.append(r"C:\Users\Alex\Desktop\GameSim")
from GameSimDatabaseConnection import Database 

from GameSimPlayers import Home_Starters
from GameSimPlayers import Away_Starters
from GameSimKickoff import Kickoff
from GameSimPlays import Plays
from GameSimSituation import Situation

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

        play = Plays(game,home_starters,away_starters)
        situation = Situation(play)
        kickoff = Kickoff(game, homeTeam, awayTeam,home_starters,away_starters)

# make this opening kickoff as opposed to a kickoff after a score
        kickoff.opening_kickoff()
        starting_field_position = kickoff.kickoff_return()
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
