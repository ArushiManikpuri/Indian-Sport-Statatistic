from models import Batsman,Bowler,Keeper,CAllRounder,AllRounder, Rider, Defender, KAllRounder, Footballer

def load_batsman(filepath) -> list[Batsman]:
    batsman_list = []

    with open(filepath, 'r') as file:
        for line in file:
            if not line.strip():
                continue  # skip empty lines

            data = line.strip().split()

            rank = int(data[0])
            name = data[1]
            match_played = int(data[2])
            innings = int(data[3])
            high_score = int(data[4])
            hundreds = int(data[5])
            average = float(data[6])
            runs = int(data[7])
            strike_rate = float(data[8])
            
            batsman = Batsman(
                name, "Male", "DOB", "India",
                match_played, "None",
                runs, innings, 0, 0, hundreds, 0, strike_rate, rank
            )
            batsman_list.append(batsman)

    return batsman_list
#batsman_list = [
#    Batsman("Virat_Kohli", "Male", "DOB", "India", 177, "None", 5412, 169, 191, 480, 5, 36, 131.61, 1),
#    Batsman("Suresh_Raina", "Male", "DOB", "India", 193, "None", 5368, 189, 194, 493, 1, 38, 137.14, 2)
#]
def save_batsman(filepath, batsman_list: list[Batsman]):     
    with open(filepath, 'w') as result:
        for b in batsman_list:
            result.write(f"{b.rank} {b.name} {b.match_played} {b.innings} {b.hundreds} {b.six} {b.four}")


def load_bowler(filepath) -> list[Bowler]:
    bowler_list = []

    with open(filepath, 'r') as file:
        for line in file:
            if not line.strip():#if its empty strings
                continue 
            data = line.strip().split()
            rank = int(data[0])
            name = data[1]
            match_played = data[2]
            innings = data[3]
            strike_rate = float(data[4])
            overs = data[5]
            wicket = data[6]
            award = data[7]
            runs = data[8]

            bowler = Bowler(name, "Male","DOB", "India", match_played, award, runs, innings, wicket, strike_rate, overs, rank)
            bowler_list.append(bowler)
    return bowler_list        
 #award, runs, innings, wicket, strike_rate, overs, rank

def load_keeper(filepath) -> list[Keeper]:
    keeper_list = []
    with open(filepath, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            data = line.strip().split()
            #name, gender, dob, nationality, match_played, award, wickets, innings, rank
            rank = data[0]
            name = data[1]
            wickets = data[2]
            innings = data[3]
            match_played = data[4]
            award = data[5]

            keeper = Keeper(name, "Male","DOB", "India", match_played, award, wickets, innings, rank)
            keeper_list.append(keeper)

    return keeper_list   

def load_c_allrounder(filepath) -> list[c_All_Rounder]:
    c_all_rounder = []

    with open(filepath, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            data = line.strip().split()
            #name, gender, dob, nationality, match_played, award,runs, innings, wicket, strike_rate, overs, rank
            rank = data[0]
            name = data[1]
            match_played = data[2]
            strike_rate = float(data[4])
            innings = int(data[3])
            overs = int(data[5])
            award = int(data[6])
            wicket = int(data[7])
            runs = int(data[8])
            c_rounder = c_All_Rounder(name, "Male", "DOB", "India", match_played, award, runs, innings, wicket, strike_rate, overs, rank)
            c_all_rounder.append(c_rounder)
        return c_all_rounder

def load_rider(filepath) -> list[rider]:
    rider_list = []
    with open(filepath, "r") as file:
        for line in file:
            if not line.strip():
                continue
            data = line.strip().split()
            rank = data[0]
            name = data[1]
            current_team = data[2]
            rides = data[3]
            points = data[4]
            Rider = rider(name, "Male", "DOB", "India", 4, "None", #Player field
            rank, rides, points, current_team) #self, rank, rides, points, current_team
            
            rider_list.append(Rider)
    return rider_list    
#1	Pardeep_Narwal		Patna_Pirates		107	1160	880
def load_defender(filepath) -> list[defender]:
    defender_list = []
    with open(filepath, "r") as file:
        for line in file:
            if not line.strip():
                continue
            data = line.strip().split()
            rank = data[0]
            name = data[1]
            current_team = data[2]
            tackle = data[3]
            points = data[4]
            match_played = data[5]
            Defender = defender(name, "Male", "DOB", "India", match_played, "None", #Player field
            rank, tackle, points, current_team) #self, rank, rides, points, current_team
            
            defender_list.append(Defender)
    return defender_list


def load_k_allrounder(filepath) -> list[k_all_rounder]:
    k_rounder_list = []
    with open(filepath, "r") as file:
        
        for line in file:
            if not line.strip():
                continue
            data = line.strip().split()

            rank = data[0]
            name = data[1]
            current_team = data[2]
            match_played = data[3]
            total_points = data[4]

            k_allrounder = k_all_rounder(name, "Male", "DOB", "India", match_played, "None",
        rank, total_points, current_team) 
            k_rounder_list.append(k_allrounder)
    return k_rounder_list    

#self, name, gender, dob, nationality, match_played, award, rank, points, current_team

def loader_footballer(filepath) -> list[footballer]:
    footballer_list = []

    with open(filepath, "r") as file:

        for line in file:
            if not line.strip():
                continue
            data = line.strip().split()

            rank = data[0]
            name = data[1]
            goal = data[2]
            red_card = data[3]
            yellow_card = data[4]
            assists = data[5]

            Footballer = footballer(name, "Male", "DOB", "India", "None", "None", 
            goal, assists, red_card, yellow_card, rank)
#(self, name, gender, dob, nationality, match_played, award, goal, assists, red_card, yellow_card, rank)
            footballer_list.append(Footballer)

    return footballer_list    