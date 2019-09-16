class Stats:
    def __init__(self,home_starters,away_starters,home_team,away_team):
        self.home_starters = home_starters
        self.away_starters = away_starters
        self.home_quarterback = self.home_starters["QB"]
        self.away_quarterback = self.away_starters["QB"]
        self.home_runningback = self.home_starters["RB"]
        self.away_runningback = self.away_starters["RB"]
        self.home_x_receiver = self.home_starters["X"]
        self.home_y_receiver = self.home_starters["Y"]
        self.home_z_receiver = self.home_starters["Z"]
        self.away_x_receiver = self.away_starters["X"]
        self.away_y_receiver = self.away_starters["Y"]
        self.away_z_receiver = self.away_starters["Z"]
        self.home_quarterback_attempts = 0
        self.away_quarterback_attempts = 0
        self.home_quarterback_completions = 0
        self.away_quarterback_completions = 0
        self.home_quarterback_yards = 0
        self.away_quarterback_yards = 0

        self.home_runningback_attempts = 0
        self.away_runningback_attempts = 0
        self.home_runningback_yards = 0
        self.away_runningback_yards = 0

        self.home_x_receptions = 0
        self.home_y_receptions = 0
        self.home_z_receptions = 0
        self.away_x_receptions = 0
        self.away_y_receptions = 0
        self.away_z_receptions = 0

        self.home_x_yards = 0
        self.home_y_yards = 0
        self.home_z_yards = 0
        self.away_x_yards = 0
        self.away_y_yards = 0
        self.away_z_yards = 0

        self.home_team = home_team
        self.away_team = away_team

    def get_qb(self, team):
        if team == self.home_team:
            return self.home_quarterback
        else:
            return self.away_quarterback

    def qb_attempt(self, qb):
        if qb == self.home_quarterback:
            self.home_quarterback_attempts = self.home_quarterback_attempts + 1
        else:
            self.away_quarterback_attempts = self.away_quarterback_attempts + 1

    def qb_completion(self, qb):
        if qb == self.home_quarterback:
            self.home_quarterback_completions = self.home_quarterback_completions + 1
        else:
            self.away_quarterback_completions = self.away_quarterback_completions + 1

    def qb_yards(self, qb, yards):
        if qb == self.home_quarterback:
            self.home_quarterback_yards = self.home_quarterback_yards + yards
        else:
            self.away_quarterback_yards = self.away_quarterback_yards + yards

    def get_qb_attempts(self, qb):
        if qb == self.home_quarterback:
            return self.home_quarterback_attempts
        else:
            return self.away_quarterback_attempts

    def get_qb_completions(self, qb):
        if qb == self.home_quarterback:
            return self.home_quarterback_completions
        else:
            return self.away_quarterback_completions

    def get_qb_yards(self, qb):
        if qb == self.home_quarterback:
            return self.home_quarterback_yards
        else:
            return self.away_quarterback_yards

    def get_rb(self, team):
        if team == self.home_team:
            return self.home_runningback
        else:
            return self.away_runningback

    def rb_yards(self, rb, yards):
        if rb == self.home_runningback:
            self.home_runningback_yards = self.home_runningback_yards + yards
            self.home_runningback_attempts = self.home_runningback_attempts + 1
        else:
            self.away_runningback_yards = self.away_runningback_yards + yards
            self.away_runningback_attempts = self.away_runningback_attempts + 1

    def get_rb_attempts(self, rb):
        if rb == self.home_runningback:
            return self.home_runningback_attempts
        else:
            return self.away_runningback_attempts

    def get_rb_yards(self, rb):
        if rb == self.home_runningback:
            return self.home_runningback_yards
        else:
            return self.away_runningback_yards

    def receiver_receptions(self,receiver):
        if receiver == self.home_x_receiver: self.home_x_receptions = self.home_x_receptions + 1
        elif receiver == self.home_y_receiver: self.home_y_receptions = self.home_y_receptions + 1
        elif receiver == self.home_z_receiver: self.home_z_receptions = self.home_z_receptions + 1
        elif receiver == self.away_x_receiver: self.away_x_receptions = self.away_x_receptions + 1
        elif receiver == self.away_y_receiver: self.away_y_receptions = self.away_y_receptions + 1
        elif receiver == self.away_z_receiver: self.away_z_receptions = self.away_z_receptions + 1

    def receiver_yards(self,receiver,yards):
        if receiver == self.home_x_receiver: self.home_x_yards = self.home_x_yards + yards
        elif receiver == self.home_y_receiver: self.home_y_yards = self.home_y_yards + yards
        elif receiver == self.home_z_receiver: self.home_z_yards = self.home_z_yards + yards
        elif receiver == self.away_x_receiver: self.away_x_yards = self.away_x_yards + yards
        elif receiver == self.away_y_receiver: self.away_y_yards = self.away_y_yards + yards
        elif receiver == self.away_z_receiver: self.away_z_yards = self.away_z_yards + yards

    def get_receiver_receptions(self,receiver):
        if receiver == self.home_x_receiver: return self.home_x_receptions
        elif receiver == self.home_y_receiver: return self.home_y_receptions
        elif receiver == self.home_z_receiver: return self.home_z_receptions
        elif receiver == self.away_x_receiver: return self.away_x_receptions
        elif receiver == self.away_y_receiver: return self.away_y_receptions
        elif receiver == self.away_z_receiver: return self.away_z_receptions

    def get_receiver_yards(self,receiver):
        if receiver == self.home_x_receiver: return self.home_x_yards
        elif receiver == self.home_y_receiver: return self.home_y_yards
        elif receiver == self.home_z_receiver: return self.home_z_yards
        elif receiver == self.away_x_receiver: return self.away_x_yards
        elif receiver == self.away_y_receiver: return self.away_y_yards
        elif receiver == self.away_z_receiver: return self.away_z_yards

