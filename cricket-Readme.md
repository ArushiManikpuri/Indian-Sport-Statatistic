For cricket you’ll need:

Player → base class.

Batsman(Player)

Bowler(Player)

Keeper(Batsman)

CAllRounder(Batsman, Bowler) → multiple inheritance for batting + bowling stats.

Team → base team stats.

TeamIPL(Team) → with win_p and titles.

Sport → for popularity.

## 💡 Keep all these in a models.py file.

      Player
     /      \

Batsman Bowler
\ /
CAllRounder

---
