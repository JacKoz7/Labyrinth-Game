## Student Project Description - "The Labyrinth" Game
### Upon starting the game, three options are available:
- Play
- Instructions ---> contain a slightly modified game guide from the website: https://zabawnik.org/wystarczy-kartka-i-dlugopis.
- Exit
![image](https://github.com/user-attachments/assets/6b46e89c-5591-472b-8fcd-b20d9bf587ef)


### Modifications:

- We set the number of squares to 35.
- We removed the labels 'from A to J' and 'from 1 to 10' on the top and side margins of the board to improve the interface aesthetics.
### The first stage of the game is as follows:

- After pressing the 'Play' button ---> Player 1 draws the maze.
- Upon completing the drawing ---> Move on to drawing the maze for Player 2.
  ![image](https://github.com/user-attachments/assets/152625f4-66ce-46b5-a9c7-b448b1f57701)

### The second stage of the game:

- Player 1 starts guessing the maze created by Player 2.
- When Player 1 clicks on a wall or finds 5 squares ---> Player 2 starts guessing.
The maze guessing process is dynamic for both players ---> it switches between them automatically.
Determining the winner:

### The game ends when Player 1 or Player 2 finds the treasure.
After the game ends, the winner is revealed.
![image](https://github.com/user-attachments/assets/ba0442c1-77e6-4ba5-97e3-63536c83799b)

### Run the project

```
git clone https://github.com/JacKoz7/Labyrinth-Game.git
cd Labyrinth-Game
pip install -r requirements.txt
python Main.py
```

Authors: Jacek Kozłowski and Mykhailo Kapustianyk.
