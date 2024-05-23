# **Battleships - Code Institute Portfolio Project 3**

Welcome to 'Battleships', a game of skill and chance where the player attempts to destroy their opponent's battleships.
An enemy has 5 ships located at random locations on an 8 x 8 board, each ship occupies one square. The player must predict the co-ordinates of their targets and use their limited shots wisely as they cannot see the locations of their enemy's ships.

Project Aim: To build a command line application that allows the user to play a logic game. A dataset will be created by the computer and edited by the user.

![Am I Responsive graphic](./assets/images/).

[Live link to application](https://)

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
- 

### **Wireframe**

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

The colour palette was created using [color.adobe.com](https://color.adobe.com/create/color-wheel).
Base colour: #D467F0
Colour harmony: Shades
As the images in the game play area are monochromatic, I wanted to utilize colours in the surrounding area. I wanted to have sufficient contrast between the settings and control buttons, and the background.

### **Font Choice**

The font is taken from [Google Fonts](https://fonts.google.com/). It is called Englebert.

![image of fonts.google.com Englebert font](./assets/images/englebert.png)

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

![screenshot of MS Excel testing document](./assets/images/excel_testing_screenshot.png)

### Alternative Browsers

Once deployed, I tested the site using the following browsers; Google Chrome, Mozilla Firefox, Microsoft Edge, and Opera Software's Opera. Each browser loaded successfully and no issues were detected.

Google Chrome
![screenshot of site running on Google Chrome](./assets/images/chrome_screenshot.png)

Mozilla Firefox
![screenshot of site running on Mozilla Firefox](./assets/images/firefox_screenshot.png)

Microsoft Edge
![screenshot of site running on Microsoft Edge](./assets/images/edge_screenshot.png)

Opera Software Opera
![screenshot of site running on Opera](./assets/images/opera_screenshot.png)

### Software Validation Testing

The warnings issued on the HTML documents seem to be an aftereffect of Codeanywhere's IDE. I have attempted to remove the unnecessary slashes however they always return once reloaded.

index.html
![screenshot of w3c validator index.html](./assets/images/validator_index.html_screenshot.png)

"Section lacks heading" - I have been informed by my peers that it is best practice to use sections in this case.
"Empty heading" - I have been informed that the HTML still passes validation however it is is slight misuse of semantics.

game.html
![screenshot of w3c validator game.html](./assets/images/validator_game.html_screenshot.png)

style.css
![screenshot of w3c validator css](./assets/images/validator_css_screenshot.png)

I have carried out some research into the 'Best Practices' issue that reduced the score to 95%. I discussed this research with my mentor and it was decided to focus on other issues due to the time restrains. I will investigate further when time allows.

I am unhappy with the 'Performance' score. When time allows, I will alter the image sizes to see if that increases the performance but doesn't distract from the gameplay.

Google Chrome DevTools Lighthouse
![screenshot of lighthouse validation](./assets/images/lighthouse_screenshot.png)

Accessibility check: wave.webaim.com

index.html

![screenshot of wave.webaim.com validation of index.html](./assets/images/webaim_index.html_screenshot.png)

game.html

![screenshot of wave.webaim.com validation of game.html](./assets/images/webaim_game.html_screenshot.png)

## **Debugging**

1. Functions
   I amended each function to include a console.log message so that I could tell whether it was being called and under which circumstances this was happening. This helped me to remove a function that had become nested and subsequently was never called.

2. Naming
   I like to be clear when I name variables, functions, etc. I find it makes the code easier to follow for myself and other users. However switching between HTML and CSS, and JavaScript led to issues trying to use the same names but only changing the style of the text, eg. cat-name in HTML/CSS became catName in JavaScript. Hence I had to rename variables similarly.

3. Boolean logic
   An issue arose as I didn't state the logic and equalities for both 'Eaten' and 'Escaped' in my functions. This was rectified by explicitly completing the Boolean arguments.

4. If Else statements
   Issues arose as I initially relied on an 'else' declaration, instead of explicitly stating each outcome.

## **Deployment**

The site was deployed to GitHub pages.

## **Credits**

- I would like to credit a Code Institute alumni, Adam Gilroy, with the game layout upon which 'Catch The Mousie!' is based.
- I visited w3schools.com numerous times during this project's development. The code for the modal is based upon this page; [w3schools css modal how to](https://w3schools.com/howto/howto_css_modals.asp/).
- I also visited 'Stack Overflow', w3docs.com, and developer.mozilla.org to check syntaxes and correct usage.

## **Acknowledgements**

I would like to thank my mentor(s), Luke Buchanan and Daisy McGirr (who stood in for Luke whilst on leave) for their guidance, understanding and support. I would also like to thank John and Martin from the Code Institute Tutoring Team for their assistance. Additionally, I would like to thank my wife Tracy for her consistent resilience, support, and encouragement.
