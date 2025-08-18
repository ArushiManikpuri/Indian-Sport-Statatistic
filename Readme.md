Step-by-Step Implementation Order
Create models.py → all class definitions with display() methods.

Create loaders.py → implement all load\_\* functions.

Create search.py → implement search() and search_cricket().

Create main.py → implement menus and connect to functions.

Test one sport (Cricket) first before adding Kabaddi & Football.

Add search and “see more” logic.

Add console clear & pause functionality.

Final testing with all .txt data files.

=================
bat = Batsman("Virat", 12000)
│
▼
Batsman.**init**(bat, "Virat", 12000)
│
▼
super().**init**("Virat") <-- 'bat' is already known to super()
│
▼
Player.**init**(bat, "Virat") <-- self = bat

---
