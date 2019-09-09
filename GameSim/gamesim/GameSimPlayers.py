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
        cur.execute("SELECT Position,STARTER FROM {tn}".format(tn=self.home_team))
 
        rows = self.conn.fetchall()
        for row in rows:
            #print(row)
            value = row[1]
            key = row[0]
        
            self.home_starters[key] = value
            #namepos = home_starters_position(row[0],row[1])
            #print(namepos, " plays ", row[0])
            #print(namepos)
        print(self.home_starters["QB"])
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
            #namepos = home_starters_position(row[0],row[1])
            #print(namepos, " plays ", row[0])
            #print(namepos)
        print(self.away_starters["QB"])
        return self.away_starters

