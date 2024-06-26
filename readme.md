# **Battleships - Code Institute Portfolio Project 3**

Welcome to 'Battleships', a game of skill and chance where the player attempts to destroy their opponent's battleships.
An enemy has 5 ships located at random locations on an 8 x 8 board, each ship occupies one square. The player must predict the co-ordinates of their targets and use their limited shots wisely as they cannot see the locations of their enemy's ships.

Project Aim: To build a command line application that allows the user to play a logic game. A dataset will be created by the computer and edited by the user.

![Am I Responsive graphic](./assets/Am_I_Responsive.png).

![Live link to application](https://grenyerre-pp3-battleships-01e3dc747fee.herokuapp.com/)

## **User Experience (UX) & Design**

This is my first project where the output is a shell terminal. Although limited to a basic colour palette and simple text effects, I wanted the output to be visually stimulating but also easy to read. This involves manually entering numerous 'spaces' in the user messages in order to centralise specific information and 'tab' away from the left hand side of the display.  

### **User Stories**

As a player:
- I would like to see the title of the application at the top of the display.
- I would like the instructions to be on show at the commencement of the game.
- I would like to see the board onto which my guesses will be placed.
- I would like to see a record of where I had placed my previous shots.
- I would like to know whether my shot was successful or not.
- I would like to know how many shots I have remaining.

### **Gameplay**

Once the game is run, the title and instructions are shown on the terminal. Also on display is the player's 'guess' board.
This shows the location of any shots previously made and will show the location of an enemy's ship that has been hit.

- The player is asked to enter a row number, between 1 and 8, for their shot.
- If the number inputed is less than 1 or greater than 8, the player is asked to re-enter a number. 
- The player is asked to enter a column letter, between A and H, for their shot.
- If the letter inputed is anything other than A - H, the player is asked to re-enter a letter.
- The player is informed whether their shot was successful or not.
- They are also informed how many turns or shots remain.
- The gameplay continues until all of the enemy's ships have been destroyed or the player has used all their turns.
- A message will be displayed to indicator which scenario ended the game.

### **Colour Choice**

I had researched numerous ways of adding colour to the terminal display but was unsatisfied with the results. Subsequently I have stuck to the default colours.


## **Features**

- Ships are placed randomly each time the game is played.
- The input from the player is checked for validity, i.e. you cannot enter a co-ordinate off the board.
- The player cannot shoot at the same location numerous times.

## **Ideas In Development**

- The player is able to select a level of difficulty whereby the board size and number of shots may increase or decrease. Probability: 70%.
- Instead of letters signifying positions, hits and misses, using other ANSI characters. Probability: 50%.
- The ships are different sizes: 1 x 5, 2 x 3, 1 x 3, etc. Probability: 10%.
- If the above is implemented, I would also like a 'mine' feature where the surrounding 8 squares are hit in addition. Probability: 10%.

## **Software Used**

Below is a list of the software/applications used in the construction of this project.

- [GitHub](https://github.com/)
  - Used to store and manage the project's code.
- [Visual Studio Code](https://code.visualstudio.com/)
  - Used as the project's Independent Development Environment (IDE).
- [Am I Responsive](https://ui.dev/amiresponsive)
  - Used to create an image of the various display sizes of the site.

## **Testing**

### **Game Testing**
![screenshot of opening statement](./assets/Opening_stmt.png)

- If any value apart from 1 - 8 is inputed when a row number is requested, the player is informed and invited to enter a valid number.

![screenshot of invalid row number entered](./assets/invalid_row_number.png)

- If any letter apart from A - H is inputed when a column letter is requested, the player is informed and invited to enter a valid letter.

![screenshot of invalid column letter entered](./assets/invalid_column_letter.png)

- When all of your shots have been used and you have not hit all 5 ships, a message is displayed.

![screenshot of game over as did not destroy all the 5 ships with the 5 shots](./assets/out_of_shots.png)

- If you destroy all 5 ships, the game ends and you are congratulated. In the image below the hidden board is on show, this was only for testing purposes.

![screenshot of game over as all 5 ships destroyed](./assets/congratulations.png)

### Software Validation Testing

Code was tested via Code Institute's Python Linter to PEP8. There is only one error showing, "<u>86<u>: E305 expected 2 blank lines after class of function definition, found 1." However lines 87 and 88 are blank.

![screenshot of Code Institute Linter results](./assets/CI_Linter.png)


## **Debugging**

After a long discussion with my mentor on my last project, I now aim to ensure each section of my code is working correctly before I continue ontot the next section. This is not always possible but it has reduced my time spent searching for bugs.

1: When constructing the board, I tried different characters, including a blank space, to show each of the co-ordinates. I chose an upper case letter 'O' to resemble the holes on the plastic version of the game. However when printing the rows, I initially used %d and %s as placeholders for numbers and letters respectively. This continued to cause issues so I changed to a tuple method. The main issue was that the row length extended if a ship or a shot was placed within it. 

## **Deployment**

This code was deployed utilising Code Institute's mock terminal for Heroku.
The steps for deployment are as follows:
- The repository is forked or cloned.
- A new Heroku app is created.
- In the Config Vars, the KEY is set to PORT and the VALUE is set to 8000.
- The buildbacks are set to Python then NodeJS (the order must be maintained).
- Ensure that the repository is linked to the Heroku app.
- Choose whether you want 'Automatic Deployment' or 'Manual Deployment'.
- Click on 'Deploy'.

Thank you to Matt Rudge, Senior Product Developer for Code Institute, for the deployment information.

## **Credits**

- I would like to credit Garrett upon whose YouTube channel projects, 'Knowledge Mavens - Python Battleships' the structure of my code is based.
- I would like to credit Code Institute upon whose mock terminal this code is deployed.
- I also visited the following websites: 'Stack Overflow', 'Geeks for Geeks', 'Python Loop' and 'Real Python' to check syntaxes and correct usage of specific techniques.

## **Acknowledgements**

I would like to thank my mentor Luke Buchanan for his invaluable guidance, understanding and support. Additionally, my wife Tracy for her consistent resilience, support, and encouragement.
