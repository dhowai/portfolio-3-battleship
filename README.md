<h1 align="center">Battleship</h1>

This version of battleship, which is tradionally a board game was created in a python and runs on the Code Institute mock terminal on Heroku. The user plays against the computer and the objective of the game is to find and destroy the computers ships before the computer. Each place thier ships on their respective boards and the ships come in various sizes.

The live link can be found here: https://portfolio-3-battleship.herokuapp.com/

![Screen sizes](insert image here)

## How to play

Battleship is a turn based game which involves two players, read more here from the wikipedia page [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version, the player enters their various sized ships on their board and does the same but, at random.

The player can only see the computer board based on the guesses they have made. An o means its a miss, x means its a hit and a large X means the ship is destroyed.

The player and computer take turns in trying to destroy the other ships and the one who achieve's this first is declared the winner.


## Features

### Existing Features

-   Welcome/home page

    -   User is welcomed with the title of the game and two options.

![Welcome page](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/welcome-title.png)

    -   The first option launches the game.
    -   The about option breifly explains the premise of the game.

![About option](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/about-game.png)

-   Place ships

    -   The first option launches the game and a let's begin text is displayed.
    -   The user then places their ships on their board.
    -   The text lets the user know what length ship they are placing.
    -   A message then shows if the ship was succesfully placed.

![Let's begin](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/begin-game.png)
![Ships placed](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/entering-ships.png)

-   Place ships errors

    -   These input validations are in place to make sure the correct input is used.
    -   The ship order needs to be one after the other either horizontal or vertical.
    -   The input needs to be a number between 0-99, which is the board's dimention
    -   The input needs to be a number

[Ship placed errors](insert image here)

-   Ships placed

    -   Once the user ships are placed the board with the locations get printed to the terminal.

![Player ships](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-ships-placed.png)

-   User guesses

    -   Once the user enters their ship locations and the computer generates their's.
    -   The user then guesses where the computer ships are.
    -   The guesses have input validations to make sure the guesses are according to the board dimentions.
    -   The input needs to be between 0-99.
    -   The input must not be the same number guesses previously.
    -   The input needs to be a integer.

![Guess errors](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/guess-errors.png)

-   Miss the ship

    -   This is a message that displays for the user and computer if the number guessed is a miss.
    -   It is denoted on the board as an o.

![Player miss](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-miss.png)
![Computer miss](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/computer-miss.png)

-   Hit the ship

    -   This is a message that displays for the user and computer if the number guessed is a hit.
    -   It is denoted on the board as an x.

![Player hit](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-hit.png)
![Computer hit](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/computer-hit.png)

-   Destroy the ship

    -   This is a message that displays for the user and computer if the number guessed destroys the ship.
    -   It is denoted on the board as an X folloed by the previous x.

![Player sunk ship](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-sunk-ship.png)
![Computer sunk ship](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/computer-sunk-ship.png)

-   End of game

    -   The first to destroy the others ships first is then declared the winner.
    -   The message also show in how many moves/guesses the game was won.
    -   The computer's guesses on your board is only displaced after the game is over.

![Player wins board with guesses ](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-win-board.png)
![Computer board with guesses](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/computer-board-after-loss.png)

### Future Features

-   Allow the user to select the board size and the number of ships
-   Have the option to show the computer ships if need be
-   Have an option to change the computer difficulty e.g. how accurate the computer guesses

## Data Model 

I defined a function that creates a board for both the computer and user. The board is a grid of 0-9 in the x and y axis and is clearly labelled, the user would need to read the y-axis variable followed by the x-axis to get the point on the board to hit. The points on the board and displayed with brackets [ ] to indicate and empty place until a guess is made. 

The check position and check boat functions are there to make sure the inputs by both the computer and player and contained to the board size and that position of how the ships are placed.

Both the computer and user have similar lists that stores the data. The guesses made, ships hit, ships missed, ships destroyed and ships placed are some examples. The check shot function checks whether the guesses made have hit, missed or destroyed a ship. The result of the guess made by the player or computer is then printed to the terminal to display the result. 

I decided to only show the player's board on the terminal to prevent the user from having to continuesly scroll between the boards and to prevent possible confusion. fix this?

## Testing

I have manually tested this project by doing the following:

    -   Passed the code through a PEP8 linter and confimed there are no problems.
    -   Given invalid inputs to the entering of ships and guesses made: strings when integers are expected, out of board inputs and same inputs.
    -   Tested in my local terminal and the code Institute Heroku terminal.

### Bugs

#### Solved bugs

-   When writing the add ship function, I noticed an error when a string was typed instead of an integer for the ship placement, this caused the game to crash. I then added a try and except statement with the if and else statement to print the according arrors to prevent the game for crashing.

### Remaining Bugs

-   No bugs remaining

### Validator Testing

-   PEP8
    -   No errors were returned from PEP8online.com

## Deployment

This project was deployed using Code institute's mock terminal for Heroku.

-   Steps for deployment:
    -   Fork or clone this repository
    -   Create a new Heroku app
    -   Set the buildbacks to python and NodeJS in that order
    -   Link the Heroku app to the repository
    -   Click on Deploy

## Credits

-   Code Institute for the deployment terminal
-   Wikipedia for the details of the battleship game
-   
