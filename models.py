from dataclass import dataclass
from datetime import date

def _ensure_date(d : data | str) -> date:
    if isinstance(d, data):
        return d
    if isinstance(d, str):
        #expect "YYY-MM-DDD"
        return date.fromisoformat(d)
    raise TypeError("dob must be a date or ISO date string") #"2025-0-15" d.year, d.month, d.date       
-------------#core function------------------------------
@dataclass
class Player:
        name: str
        gender: str
        dob: date | str
        nationality: str
        match_played: int = 0
        award: int = 0
    def __post_init__(self) -> None:
        self.dob = _ensure_date(self.dob)
        if self.match_played < 0:
            raise ValueError("matches played cannot be negative")
        if self.award < 0:
            raise ValueError("award earned cannot be negative")        
    @property
    def age(self) -> int:
        today = date.today()
        return (
            today.year - self.dob.year - 
            ((today.month, today.date) < (self.dob.month, self.dob.date))
        )


    def __str__(self) -> str: #print(player)
        return (f"{self.name} ({self.nationality}) - Age: {self.age}\n"
        f"Matches: {self.match_played} | Awards: {self.award}"
        )
    
    def to_dict(self) -> dict[str, any]: #player.to_dict()
        d = asdict(self)
        d["dob"] = self.dob.isoformat()
        d["age"] = self.age
        return d

----------#value object composition#------------- 
@dataclass(frozen = True)      
class BatsmanStats:      
        runs: int
        innings: int
        six: int
        four: int
        hundreds: int
        fifties: int
        strike_rate: float
        rank: Optional[int] = None
    def __post_init(self) -> None:
        if n in ("runs", "innings", "six", "four", "hundreds", "fifties", "rank"):
            if getattr(self, n) < 0: #getattr(object, "attribute_name", default)  
                raise ValueError("f(n) cannot be negative")
        if self.strike_rate < 0:
            raise ValueError("f strike_rate cannot be negative")
class BowlerStats:
        innings: int
        wicket: int
        strike_rate:float
        overs: int
        runs: int
        rank: Optional[int]
    def display(self):
        super().display()
        print(f"Rank: {self.rank}")
        print(f"Innings played: {self.innings}")
        print(f"wicket: {self.wicket}")
        print(f"strike_rate: {self.strike_rate}")
        print(f"overs: {self.overs}")
        print(f"runs: {self.runs}")           
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
        self.runs = runs

    def display(self):
        super().display()
        print(f"Rank: {self.rank}")
        print(f"Innings played: {self.innings}")
        print(f"wicket: {self.wicket}")
        print(f"strike_rate: {self.strike_rate}")
        print(f"overs: {self.overs}")
        print(f"runs: {self.runs}")

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

class CAllRounder(Batsman, Bowler):
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

class Rider(Player):
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

class Defender(Player):
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

class KAllRounder(rider, defender):
    def __init__(self, name, gender, dob, nationality, match_played, award, rank, points, current_team):
        Player.__init__(self, name, gender, dob, nationality, match_played, award)
        self.rank = rank
        self.points = points
        self.current_team = current_team

    def display(self):
        print(f"Rank: {self.rank}")
        print(f"Name: {self.name}")
        print(f"current_team: {self.current_team}") 
        print(f"match_played: {self.match_played}") 
        print(f"Total Points: {self.points}")  
       
class Footballer(Player):
    def __init__(self, name, gender, dob, nationality, match_played, award, goal, assists, red_card, yellow_card, rank):
        super().__init__(name, gender, dob, nationality, match_played, award)
        self.goal = goal
        self.assists = assists
        self.red_card = red_card
        self.yellow_card = yellow_card
        self.rank = rank
    
    def display(self):
        print(f"name: {self.name}")
        print(f"rank: {self.rank}")
        print(f"goal: {self.goal}")
        print(f"assists: {self.assists}")
        print(f"red_card: {self.red_card}")
        print(f"yellow_card: {self.yellow_card}")

class Team:
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

class TeamIPL(Team):
    def __init__(self, name, win, loss, tie, win_title, win_p):
        super().__init__(name, win, loss, tie)
        self.win_title = win_title
        self.win_p = win_p

    def display(self):
        super().display()
        print(f"win: {self.win}")
        print(f"win_title:{self.win_title}")
        print(f"win_p: {self.win_p}")

class TeamISL(Team):
    def __init__(self, name, win, loss, tie, goal_for, goal_against, goal_diff, points):
        super().__init__(name, win, loss, tie)
        self.goal_for = goal_for
        self.goal_against = goal_against
        self.goal_diff = goal_diff
        self.points = points
    def display(self):
        super().display()
        print(f"Goal for:{self.goal_for}")
        print(f"Goal against:{self.goal_against}")
        print(f"Goal Difference:{self.goal_diff}")
        print(f"Goal points:{self.points}")

class TeamKabbadi(Team):
    def __init__(self, name, win, loss, tie, per_win, per_loss, per_tie):
        super().__init__(name, win, loss, tie)
        self.per_win = per_win
        self.per_loss = per_loss
        self.per_tie = per_tie
    def display(self):
        super().display()
        print(f"Winning percentage:{self.per_win}")
        print(f"loss percentage:{self.per_loss}")
        print(f"lie percentage:{self.per_tie}")

class Sport:
    def __init__(self, name, popularity):
        self.name = name
        self.popularity = popularity

    def display(self):
        print(f"Name:{self.name}")
        print(f"Viewers: {self.popularity}")



        










