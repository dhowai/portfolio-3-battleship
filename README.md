<h1 align="center">Battleship</h1>

This version of battleship, which is traditionally a board game was created in a python and runs on the Code Institute mock terminal on Heroku. The user plays against the computer and the objective of the game is to find and destroy the computer's ships before the computer finds yours. Each has ships on their respective boards and the ships come in various sizes.

The live link can be found here: https://portfolio-3-battleship.herokuapp.com/

![Screen sizes](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/screen-sizes.png)

## How to play

Battleship is a turn based game which involves two players, read more here from the [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) page.

In this version, the player enters their various sized ships on their board and does the same but, at random.

The player can only see the computer board based on the guesses they have made. An o means its a miss, x means its a hit and a large X means the ship is destroyed.

The player and the computer take turns in trying to destroy the other ships and the one who achieve's this first is declared the winner.


## Features

### Existing Features

-   Welcome/home page

    -   User is welcomed with the title of the game and three options.

![Welcome page](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/welcome-title.png)

-   Options

    -   The first option launches the game.
    -   The about option briefly explains the premise of the game.
    -   The credits section has a title with the author's name. 

![About option](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/about-game.png)

![Credits](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/credits.png)

-   Place ships

    -   The first option launches the game and a get set up text is displayed.
    -   The user then places their ships on their board.
    -   The text lets the user know what length ship they are on.
    -   A message then shows if the ship was successfully placed.

![Let's begin](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/begin-game.png)

![Ships placed](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/entering-ships.png)

-   Place ships errors

    -   These input validations are in place to make sure the correct input is used.
    -   The ship order needs to be one after the other either horizontal or vertical.
    -   The input needs to be a number between 0-99, which is the board's dimensions
    -   The input needs to be a number

![Ship placed errors](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/entering-ship-error.png)

![Ship placed errors](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/entering-ship-error%20(2).png)

![Ship placed errors](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/entering-ship-error%20(3).png)

![Ship placed errors](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/entering-ship-error%20(4).png)

![Ship placed errors](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/entering-ship-error%20(5).png)

-   Ships placed

    -   Once the user ships are placed the board with the locations get printed to the terminal.
    -   Once all the ships are placed a message gets printed to the terminal to being the guessing.

![Player ships](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-ships-placed.png)

![Player ships all placed](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/ships-all-placed.png)

-   User guesses

    -   Once the user enters their ship locations and the computer generates their's.
    -   The user then guesses where the computer's ships are.
    -   The guesses have input validations to make sure the guesses are according to the board dimensions.
    -   The input needs to be a number between 0-99.
    -   The input must not be the same number guesses previously.
    -   The input needs to be a number.

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
    -   It is denoted on the board as an X followed by the previous x.

![Player sunk ship](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-sunk-ship.png)

![Player sunk ship board](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-sunk-ship-board.png)

![Computer sunk ship](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/computer-sunk-ship.png)

-   End of game

    -   The first to destroy the others ships first is then declared the winner.
    -   The message also shows in how many moves/guesses the game was won.
    -   The computer's guesses on your board is only displaced after the game is over.

![Player wins, computer board with guesses](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-win.png)

![Player board with player guesses](https://github.com/dhowai/portfolio-3-battleship/blob/main/images/player-board-with-computer-guesses.png)

### Future Features

-   Allow the user to select the board size,number of ships and maximum turns
-   Have the option to show the players board with the computer guesses
-   Have an option to change the computer difficulty e.g. how accurate the computer guesses

## Data Model 

I defined a function that creates a board for both the computer and user. The board is a grid of 0-9 in the x and y axis and is clearly labelled, the user would need to read the y-axis variable followed by the x-axis to get the point on the board to hit. The points on the board and displayed in brackets [ ] to indicate the empty field until a guess is made. 

The check position and check boat functions are there to make sure the inputs by both the computer and player and contained to the board size and that position of how the ships are placed.

Both the computer and user have similar lists that store the data. The guesses made, ships hit, ships missed, ships destroyed and ships placed are some examples. The check shot function checks whether the guesses made have hit, missed or destroyed a ship. The result of the guess made by the player or computer is then printed to the terminal to display the result. 

I decided to only show the computers board with the player guesses, this prevents the user from having to scroll between both boards to see the outcomes. Also adds a sense of suspense that the computer could be on the verge of winning.

## Testing

-   I have manually tested this project by doing the following:

    -   Passed the code through a PEP8 linter and confimed there are no problems.
    -   Given invalid inputs to the entering of ships and guesses made: strings when integers are expected, out of board inputs and same inputs.
    -   Tested in my local terminal and the code Institute Heroku terminal.

### Bugs

#### Solved bugs

-   When writing the add ship function, I noticed an error when a string was typed instead of an integer for the ship placement, this caused the game to crash. I then added a try and except statement with the if and else statement to print the according errors to prevent the game from crashing.

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
-   Followed a tutorial by [DR. Codie](https://www.youtube.com/channel/UCFH0iZlolP0HiJOUuDxihqg)
-   Used [Stackoverflow](https://stackoverflow.com/questions/19964603/creating-a-menu-in-python) for the menu
-   [Devdungeon](https://www.devdungeon.com/content/create-ascii-art-text-banners-python) for the pyfiglet font tutorial 
-   Used [amiresponsive](http://ami.responsivedesign.is/#)
-   My mentor for giving constant feedback throughout the sessions.
