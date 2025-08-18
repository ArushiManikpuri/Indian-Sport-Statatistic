from data_loader import load_batsman, load_bowler, load_keeper, load_c_allrounder, load_rider, load_defender, load_k_allrounder, loader_footballer

def main():
    batsman = load_batsman("data/Top_Batsman.txt")
    bowler = load_bowler("data/Top_Bowler.txt")
    keeper = load_keeper("data/Top_Wicket_keeper.txt")
    c_all_rounder = load_c_allrounder("data/C_All_Rounder.txt")
    Riders = load_rider("data/Top_Rider.txt")
    Defender = load_defender("data/Top_Defender.txt")
    k_allrounder = load_k_allrounder("data/K_All_Rounder.txt")
    Footballer = loader_footballer("data/Top_Footballer.txt")
    while True:
        print("Welcome to Indian Sports Stat System")
        print("1. Cricket")
        print("2. Kabaddi")
        print("3. Football")
        print("4. Exit")

        choice_menu = input("Enter your choice")
        if choice_menu == "1":
            print("1. Tops Batsman")
            print("2. Tops Bowler")
            print("3. Top Keeper")
            print("4. Cricket_All_Rounder")
            choice = input("Enter your choice")
            if choice == "1":
                for b in batsman:
                    b.display()
            elif choice == "2":
                for b in bowler:
                    b.display()
            elif choice == "3":
                for k in keeper:
                    k.display() 
            elif choice == "4":
                for c in c_all_rounder:
                    c.display()            
            else:
                print("Invalid option")        

        elif choice_menu == "2":
            print("1. Top Riders")
            print("2. Top Defender")
            print("3. All Rounder Kabaddi Player")
            choice = input("Enter your choice")
            if choice == "1":
                for r in Riders:
                    r.display()
            elif choice == "2":
                for d in Defender:
                    d.display()
            elif choice == "3":
                for k in k_allrounder:
                    k.display()              
        elif choice_menu == "3":
            for f in Footballer:
                f.display()
        else:
            print("Invalid input")    



if __name__ == "__main__":
    main()  
