class Player:
    def __init__(self, name, gender, dob, nationality, match_played, award):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.nationality = nationality
        self.match_played = match_played
        self.award = award

    def display(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Dob: {self.dob}")
        print(f"Nationality: {self.nationality}")
        print(f"Matches played: {self.match_played}")
        print(f"Award won: {self.award}")

class Batsman(Player):
    def __init__(self, name, gender, dob, nationality, match_played, award, runs, innings, six, four, hundreds, fifties, strike_rate, rank):
        super().__init__(name, gender, dob, nationality, match_played, award)        
        self.runs = runs
        self.innings = innings
        self.six = six
        self.four = four
        self.hundreds = hundreds
        self.fifties = fifties
        self.strike_rate = strike_rate
        self.rank = rank

    def display(self):
        super().display()
        print(f"Runs scored: {self.runs}")
        print(f"Inings played: {self.innings}")
        print(f"Sixes: {self.six}")
        print(f"Fours: {self.four}")
        print(f"Hundreds: {self.hundreds}")
        print(f"fifties: {self.fifties}")
        print(f"Strike_rate: {self.strike_rate}")
        print(f"rank: {self.rank}")

class Bowler(Player):
    def __init__(self, name, gender, dob, nationality, match_played, award, runs, innings, wicket, strike_rate, overs, rank):
        super().__init__(name, gender, dob, nationality, match_played, award)

        self.rank = rank
        self.innings = innings
        self.wicket = wicket
        self.strike_rate = strike_rate
        self.overs = overs

    def display(self):
        super().display()
        print(f"Rank: {self.rank}")
        print(f"Innings played: {self.innings}")
        print(f"wicket: {self.wicket}")
        print(f"strike_rate: {self.strike_rate}")
        print(f"overs: {self.overs}")

class Keeper(Player):
    def __init__(self, name, gender, dob, nationality, match_played, award, wickets, innings, rank):
        super().__init__(name, gender, dob, nationality, match_played, award) #called to set inheritated player
        self.wickets = wickets
        self.innings = innings
        self.rank = rank

    def display(self):
        print(f"Name {self.name}")
        print(f"Wicket {self.wickets}")
        print(f"Innings {self.innings}")
        print(f"rank {self.rank}")

class c_All_Rounder(Batsman, Bowler):
    def __init__(self, name, gender, dob, nationality, match_played, award,runs, innings, wicket, strike_rate, overs, rank):
        Player.__init__(self, name, gender, dob, nationality, match_played, award) #called to set inheritated player
        self.wicket = wicket
        self.innings = innings
        self.rank = rank
        self.overs = overs
        self.strike_rate = strike_rate
        self.award = award
        self.runs = runs
        self.match_played = match_played
        self.name = name

    def display(self):
        print(f"Name:{self.name}")
        print(f"Wicket: {self.wicket}")
        print(f"Over: {self.overs}")
        print(f"Innings: {self.innings}")
        print(f"runs: {self.runs}")
        print(f"rank: {self.rank}")
        print(f"strike rate: {self.strike_rate}")
        print(f"award: {self.award}")
        print(f"match played: {self.match_played}")

class team:
    def __init__(self, name, win, loss, tie):
        self.name = name
        self.win = win
        self.loss = loss
        self.tie = tie

    def display(self):
        print(f"Name:{self.name}")
        print(f"win: {self.win}")
        print(f"loss: {self.loss}")
        print(f"tie: {self.tie}")

class rider(Player):
    def __init__(self, name, gender, dob, nationality, match_played, award, rank, rides, points, current_team):
        #call to parent constructor
        super().__init__(name, gender, dob, nationality, match_played, award)
        #attributes of rider class
        self.rank = rank
        self.rides = rides
        self.points = points
     
        self.current_team = current_team

    def display(self):
        print(f"Rank: {self.rank}")
        print(f"Name: {self.name}") #attribute from parent class
        print(f"Rides: {self.rides}")
        print(f"Points: {self.points}")
        print(f"current_team: {self.current_team}")

class defender(Player):
    def __init__(self, name, gender, dob, nationality, match_played, award, rank, tackle, points, current_team):
        super().__init__(name, gender, dob, nationality, match_played, award)
        self.rank = rank
        self.tackle = tackle
        self.points = points
        self.current_team = current_team

    def display(self):
        print(f"Rank: {self.rank}")
        print(f"Name: {self.name}")
        print(f"Tackle: {self.tackle}")
        print(f"Points: {self.points}")
        print(f"current_team: {self.current_team}")
        print(f"match_played: {self.match_played}")

class k_all_rounder(Rider, Defender):
    def __init__(self, name, gender, dob, nationality, match_played, award, rank, tackle, points, current_team):
        super().__init__(name, gender, dob, nationality, match_played, award)
        self.rank = rank
        self.tackle = tackle
        self.points = points
        self.current_team = current_team

    def display(self):
        print(f"Rank: {self.rank}")
        print(f"Name: {self.name}")
        print(f"Tackle: {self.tackle}")
        print(f"Points: {self.points}")
        print(f"current_team: {self.current_team}")
        print(f"match_played: {self.match_played}")        

class team_ipl(team):
    def __init__(self, name, win, loss, tie, win_title, win_p):
        self.name = name
        self.win = win
        self.loss = loss
        self.tie = tie
        self.win_title = win_title
        self.win_p = win_p

    def display(self):
        print(f"Name:{self.name}")
        print(f"win: {self.win}")
        print(f"win_title:{self.win_title}")
        print(f"win_p: {self.win_p}")

class sport:
    def __init__(self, name, popularity):
        self.name = name
        self.popularity = popularity

    def display(self):
        print(f"Name:{self.name}")
        print(f"Viewers: {self.popularity}")

        










