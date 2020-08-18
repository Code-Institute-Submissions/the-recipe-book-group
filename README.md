
<h1 align="center"> the-cook-book-group</h1>
<h2 align="center">A free recipe sharing website</h2>
<br>
<br>

# Table of content

(1) [UX](#ux)

- [Project Purpose](#project-purpose)
- [User Stories](#user-stories)
- [Site Owner Goals](#site-owner-goals)

(2) [UI and Design Choices](#ui-and-design-choices)

- [Design Choices](#design-choices)
- [Fonts](#fonts)
- [Colours](#colours)
- [Background](#background-images)

(3) [Wireframes](#wireframes)

(4) [Testing](#testing)

(5) [Bugs and fixes](#bugs-and-fixes)

(6) [Deployment](#deployment)

(7) [Technologies used](#technologies-used)

(8) [Tools](#tools)

(9) [Code](#code)

(10) [Credits](#credits)

(11) [Please Note](#please-note)

(11) [Disclaimer](#disclaimer)

# UX

## Project Purpose

The purpose of this build is to provide a simple to use platform for a group to share recipes and instructions of their use using a common database.
This should at the same time allow the site owner to collect data saved to the database.

## User Stories

1. As a user, I want to **quickly access the detailed instrucitons for any recipe in the group.** so that I can **cook using the information presented to me**.
2. As a user, I want to **quickly and easily choose a category** so that I can **narrow down the type of recipe I am looking for.**
3. As a user, I want to **add my own reicpes to the group and be able to give a clear presentation of the recipe and instructions for its use** so that I can **allow friends and family to benefit.**
4. As a user, I want to **alter and ammend any of my recipes if I believe it improves the recipe** so that I can **help the group as a whole improve the recipes**
5. As a user, I want to **be able to easily navigate back to the home as well as between pages**

## Site Owner Goals

- To have complete access to the collected data within the associated database.

## UI and Design Choices

# UI

- A mobile first approach to design will be used.
- A navbar with the website title as a central feature. A home button to allow easy navigation back to the main page. A dropdown menu with the main options will feature on the the right side
- Three simple and clear buttons in the main body of the landing page will provide easy options for lookin up, adding and editing recipes.
- A footer with basic website information
- The site should feel clean, simple and most of all intuative to the user as it will be the central hup for a commen family/friends experience
- The site is to be constructed according to the D.R.U.D (create, read, use, delete) principle.
- The site should have it's features emmidiately accesable to a user  
- The user should have easily accesable recipes and be provided with basic instructions for its use
- The users should be able to share their recipes with the group. This will include details of the recipe such as ingredients, cooking time, amount of people it serves, cooking instructions etc.
- The user should be able to add their name to their recipe.
- The user should be able to add their own image of their recipe.
- The user should have the ability to edit or delete all recipes wihtin the group.
- The site should be easily navigated from page to page as it's purpose will be to assist the user in cooking rather then being their main focus of attention
- The site should be a familar place to return to after the initial intuatively learned experience

## Design Choices

## Fonts

Google fonts wil be used thoughout. The font-familes will be indie flower and pangolin as I felt they have a friendly, almost handwritten feel to the site.

## Colours

Colour schemes were chosen using [colorcombos.com](https://www.colorcombos.com)

## Background Images

The background images were chosen to be visually captive and to be an emmidiate indication of the reason and purpose of the website.

## WIREFRAMES

Wireframes were constructed using [whimsical Wireframes](https://whimsical.com/wireframes) as it allow me to easily construct both a mobile and desktop version of original concept.
See the wireframes <a href="https://github.com/andershup/the-recipe-book-group/blob/196ae246d08eeb42e0cca89686e5c49d33c066e4/wireframes">here.</a>

## TESTING

### Manual testing

- Navbar: All navbar links tested as functional in both mobile and expanded view.The "Home" link as well as clicking on the center-logo text returns page to the index page from all pages.
Errors found: The mobile nav is showing on the tablet(medium) setting.
- Index.html main body: All links tested as functional.  
- See our recipes page: All links tested functional. The last 'show this recipe' buttom obscured by footer so buffer div added outside the 'for' loop.
- Add Recipe page: All links tested functional.
Errors found: The Materialize column sizes used not responsive.
- Footer: Footer showing correctly on all pages.

### Validator testing

#### CSS. No errors found.

#### HTML
- base.html.  ![error code](/supportdocs/missingtitle.png)
- 

## Bugs and Fixes

Navbar: Dispite having "show-on-small" as a Materialize class which is defined as "show on mobiles ONLY" it is still showing up to a width of 992px in Dev Tools.
Also the side-nav is showing the entire length of the page.

```html
<a href="#" data-activates="mobile-nav" class="button-collapse show-on-small"><i class="material-icons">menu</i></a>
```

Add Recipe:(example code)

```html
 <div class="input-field col s12 m4 l3">
```

Favicon:

```bash
"GET /favicon.ico HTTP/1.1" 404
```

Restarting workspace in gitpod fixed this issue.



## DEPLOYMENT

- Create requirements.txt in the terminal:

```bash
pip3 freeze > requirements.txt
```

- Create a Procfile in the termianl:

```bash
echo web: python3 app.py > Procfile
```

- Push files to your repository:

```bash
git push
```

- Login to Heroku and in the dashboard create a new app.
- In the depley section select GitHub as the deployment method.
- Go to settings and click 'Reveal Config Vars' then set IP: 0.0.0.0 and PORT: 5000.
- Click 'Open app' to deploy.

## Note

Should you need to install the relevant requirements and dependencies use the following command:

```bash
pip3 -r requirements.txt
```

### How to run this project in the terminal  

```bash
flask run
```

OR

```bash
python3 app.py
```

### All deployment tested on the following

#### HARDWARE

- Desktop PC
- MacBook Air
- Galaxy Tab A
- Iphone X

#### SOFTWARE

- windows 10
- OS X
- Android 10
- iOS 13

## Technologies used

### Front-End

- **HTML** for the base structure of the website
- **CSS** for adding styles to HTML elements
- **MATERIALISE** for frameworks
- **JQUERY** for javascript functionality

### Back-End

- **FLASK** microframework
- **FLASK-PYMONGO**
- **DNSPYTHON**
- **HERUKO**
- **PYTHON**
- **PYMONGO**
- **MongoDB Atlas**
- **BSON**

### Testing

- [Markdownlint](https://dlaa.me/markdownlint/)
- [JavaScript](https://jshint.com/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)
- [HTML Validator](https://validator.w3.org/)

## Tools

- [colorpicker.com](https://www.ginifab.com/feeds/pms/color_picker_from_image.php)
- [whimsical Wireframes](https://whimsical.com/wireframes)
- [HTML formatter](https://webformatter.com/html)

## CODE

Some of my code was adapted from:

- [W3Schools](https://www.w3schools.com/)
- [Whimsical](https://whimsical.com/)

## Inspiration

## Credits

## Please note

This repository was created using the [Code Institute Gitpod Template](https://github.com/Code-Institute-Org/gitpod-full-template) and the README.md file and wireframes were copied to this repository. For version control please kindly see [the-cook-book-group](https://github.com/andershup/the-cook-book-group)

No "git push" commands were used until after commit 3efcdfc12417a64241343ce24c82a6d3d547a34b. I had Heroku directly connected and auto deployment set and so I thought I was not necessary to git push.

## Disclaimer

All content within this website are for educational purposes only.