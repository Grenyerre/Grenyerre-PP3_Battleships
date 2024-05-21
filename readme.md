# **Battleships - Code Institute Portfolio Project 3**

Welcome to 'Battleships', a game of skill and chance where the player attempts to destroy their opponent's battleships.
To do this, they must predict the co-ordinates of their targets and use their limited shots wisely.

Project Aim: To build a command line application that allows the user to play a logic game. A dataset will be created by the computer and edited by the user.

![Am I Responsive graphic](./assets/images/).

[Live link to application](https://)

## **User Experience (UX) & Design**

This is my first project where the output is a shell terminal. Although limited to a basic colour palette and simple text effects, I wanted the output to be visually stimulating but also easy to read.  

### **User Stories**

As a user/player:
- I would like to see the title of the application at the top of the display.
- I would like the instructions to be on show at the commencement of the game.
- I would like to see the board onto which my guesses will be placed.
- I would like to see a record of where I had placed my previous shots.
- I would like to know whether my shot was successful or not.
- I would like to know how many shots I have remaining.
- 

### **Wireframe**

### **Gameplay**

Once the 'Play Game' button on the 'Welcome' page has been clicked, the 'Game' page is displayed and gameplay can commence.

- Displayed on the screen are three holes infront of a hungry cat.
- The aim of the game is to predict from which hole a mouse will appear and direct the cat to the hole, so that it can eat the escaping mouse.
- You do this by selecting one of the holes by clicking a control button, marked 'LEFT', 'CENTRE', or 'RIGHT'.
- The image will now change.
  - If you have selected the correct hole, the image will display the cat holding the mouse by its tail.
  - Otherwise, the image will display the cat pouncing towards the chosen hole and the mouse escaping from another hole.
- The message in the 'Game State' area and the score will also change. It will state which hole both you and the mouse chose.
  - If you selected the correct hole, 'Yum yum!' is displayed and 'Eaten' increases by 1.
  - Otherwise, 'Better luck next time.' is diplayed and 'Escaped' increases by 1.
    -The game ends when 'Eaten' + 'Escaped' = 5. The image and 'Game State' message also change.
  - If 'Eaten' is 0 or 1, the image displays a hungry cat and the message states, 'Never mind, 'catname' is still hungry. More mice needed.'.
  - If 'Eaten' is 2 or 3, the image displays a cat washing itself and the message states, 'Good attempt! 'catname' is almost full.'.
  - If 'Eaten' is 4 or 5, the image displays a cat with a mouse in its mouth and the message states, 'Well done! 'catname' has achieved satiety.'.
  - In each of the above scenarios, 'To play again, please press the 'Restart Button', is shown below the messages.

### **Colour Choice**

The colour palette was created using [color.adobe.com](https://color.adobe.com/create/color-wheel).
Base colour: #D467F0
Colour harmony: Shades
As the images in the game play area are monochromatic, I wanted to utilize colours in the surrounding area. I wanted to have sufficient contrast between the settings and control buttons, and the background.

### **Font Choice**

The font is taken from [Google Fonts](https://fonts.google.com/). It is called Englebert.

![image of fonts.google.com Englebert font](./assets/images/englebert.png)

## **Features**


### **Settings Buttons**

### **Game Play Area**

This is the largest section of the page and displays the images of the game's protagonist and antagonist. These images reflect the actions of the player and the computer choice. They also vary at the end of the game to reflect the cat's state of satiety.

### **Control Buttons**

These allow the player to input their choice from which hole they believe the mouse will appear; left, centre, or right.

### **Score Area**

Here is displayed in numbers how many mice have been caught (eaten!) and how many have escaped.

### **Game State Area**

Messages are displayed here to inform the player of the required action, the result of their actions, and the final score messages.

### **Footer**

Contains information regarding the copyright owner of the images and music used and the site's author.

## **Ideas In Development**

- Increase the number of holes from which the mouse can escape to five. Probability: 70%.
- To separate the music and sound effects so that they can be toggled on/off independently. Probability: 50%.
- Alter the game graphics to allow the user to choose the cat's colouring; black, tortoiseshell, ginger, grey, etc. Probability: 10%.
- To include a high score table to record the highest scores, the date and the player name. Probability: 10%.

## **Software Used**

Below is a list of the software/applications used in the construction of this project.

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - Used to create the structure of the webpage.
- [CSS3](https://en.wikipedia.org/wiki/CSS)
  - Used to style the content of the webpage.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - Used to implement functionality in the game.
- [GitHub](https://github.com/)
  - Used to store and manage the project's code.
- [Codeanywhere](https://app.codeanywhere.com/)
  - Used as the project's Independent Development Environment (IDE).
- [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
  - Used in the testing and debugging process.
- [W3C Markup Validation Service](https://validator.w3.org/)
  - Used to validate the project's HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
  - Used to validate the project's CSS code.
- [JSHint](https://jshint.com/)
  - Used to validate the project's JavaScript code.
- [MicroSoft Paint](https://microsoft.com > en-us > windows > paint)
  - Used to create the game's images.
- [Webaim.](https://webaim.org/resources/contrastchecker/)
  - Used to check colour scheme for readability.
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
