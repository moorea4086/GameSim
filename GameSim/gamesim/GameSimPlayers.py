class Home_Starters:
    def __init__(self,conn,home_team):
        """
        Query all rows in the tasks table
        param conn: the Connection object
        :return:
        """
        self.conn = conn
        self.home_team = home_team
        self.home_starters = {}
# since these methods are used for both classes, create an inheritance?
    def roster(self):
        cur = self.conn.cursor
        #https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html#querying-the-database---selecting-rows
        cur.execute('SELECT Position,STARTER FROM {tn} WHERE Position != "WR"'.format(tn=self.home_team))
 
        rows = self.conn.fetchall()
        for row in rows:
            value = row[1]
            key = row[0]        
            self.home_starters[key] = value

        cur.execute('SELECT Position,STARTER FROM {tn} WHERE Position == "WR"'.format(tn=self.home_team))
        rows = self.conn.fetchall()
        #print(row)
        value = rows[0][1]
        key = "X"
        self.home_starters[key] = value
        value = rows[1][1]
        key = "Y"
        self.home_starters[key] = value
        value = rows[2][1]
        key = "Z"
        self.home_starters[key] = value
        return self.home_starters

class Away_Starters:
    def __init__(self,conn,away_team):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        self.conn = conn
        self.away_team = away_team
        self.away_starters = {}
# since these methods are used for both classes, create an inheritance?
    def roster(self):
        cur = self.conn.cursor
        #https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html#querying-the-database---selecting-rows
        cur.execute("SELECT Position,STARTER FROM {tn}".format(tn=self.away_team))
 
        rows = self.conn.fetchall()
        for row in rows:
            #print(row)
            value = row[1]
            key = row[0]
        
            self.away_starters[key] = value

        cur.execute('SELECT Position,STARTER FROM {tn} WHERE Position == "WR"'.format(tn=self.away_team))
        rows = self.conn.fetchall()
        value = rows[0][1]
        key = "X"
        self.away_starters[key] = value
        value = rows[1][1]
        key = "Y"
        self.away_starters[key] = value
        value = rows[2][1]
        key = "Z"
        self.away_starters[key] = value
        return self.away_starters

