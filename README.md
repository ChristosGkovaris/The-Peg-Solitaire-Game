# Peg Solitaire Game

Welcome to the "Peg Solitaire Game," a classic single-player puzzle game implemented in Python. The goal is to remove pegs from the board by jumping over them, leaving only one peg remaining.

## Game Instructions
**Objective:** Reduce the number of pegs on the board by jumping over them, ideally leaving only one peg.
**How to Play:**
The game begins with a board setup containing pegs ('1') and empty spaces ('0').
Enter the position of the peg you want to move followed by the direction (L for left, R for right, U for up, D for down).
Valid moves involve jumping over a peg into an empty space, which removes the jumped peg.
Continue playing until no more valid moves are possible.
**Game End:** The game ends when there are no valid moves left. The fewer pegs remaining, the better your performance.


## Implementation Details
- The game is implemented in Python as a command-line interface.
- The board is represented as a 2D list, with the initial configuration matching the traditional English peg solitaire layout.
- The game logic includes functions to handle user input, validate moves, and update the game state.


## How to Run
**Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/peg-solitaire.git
    cd peg-solitaire
    ```
**Ensure you have Python installed:** The game requires Python 3. Ensure you have it installed on your system.
**Run the Game:**
    ```bash
    python peg_solitaire.py
    ```
