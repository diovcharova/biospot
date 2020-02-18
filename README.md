# BioSpot
Milestone Project Four: Fullstack Frameworks with Django - Code Institute

This is the online shop of BioSpot - a small shop for organic and healthy products. It is an ecommerce site and includes information about delivery prices, the store location and contacts.

[![Build Status](https://travis-ci.org/diovcharova/biospot.svg?branch=master)](https://travis-ci.org/diovcharova/biospot)


## Demo 
A demo of the website can be found [here](https://biospot.herokuapp.com/).

## UX
The website is requested by the owners of Biospot. Their main goal is to have a online shop, which is is easy to use by their current and potential customers.
The website has to be built in order to simplify usage of both customers and shop employees, who will use the admin panel to manipulate the database. 
The design on the website is very simple and stripped of complicated structures. That is because it is vital for users to be able to navigate easily and find the information they are looking for. The structure of the different pages is the same to further accommodate ease of use. The colors, typography and styles are as neutral as possible, and only complement the main content.  

### User stories
After talking to the owners of Biospot there are several specific features they have requested. The conclusions are summarized below. 
* As a potential customer of Biospot, I want to find information about the products they offer in a concise and clear way.
* As a customer, I want to be able to explore the products by categories.
* As a customer, I want to search for a specific product based on its name.
* As the owner and admin of the page, I want to be able to easily manipulate the database entries. The main features of the products have to be highlighted and secondary information should be desplayed on request.
* Contact between the customers and the shops should be as simplified as possible. 

### UX based design
As part of the design process, I developed wireframes, which can be viewed [here](), and mockups, which can be viewed [here](). They are based on the requirements of the owners of the shop. The design and functionalities are suited to their needs.

## Features

### Existing Features
The header and footer give a general structure to the website. The navbar is a list of links, that collapses to a dropdown menu on smaller screens to save real estate. Above the navigation bar, the search bar, user-profile related links and cart can be found. The footer contains information about the store location, delivery rates, navigation links and links to the social media accounts of the store.

The home page displays a carousel, serving as an introduction to the store. The current promotions the store has are found below that. 

Products can be viewed in different ways - either by category or all at once. Each product is in the form of a card with tabs, with the most important information on the main tab and additional information is displayed by request of the user. The pages for products, belonging to a specific category are built in the same way for consistency. The pages are paginated to display 24 results at a time.

The contact page contains information about the store and the location displayed in a Google Maps element. There is a contact form, so the customer can send a message without leaving the site.

There are several functionalities related to the registration, login, logout and editing of the profile. All the forms are validated. User authentication is either by email or urdername. A user can edit their profile by changing their username, email and password. There is also the option to reset password. To request that, an user fills in their email, where they receive a link to reset their password.

There are also cart and checkout functionalities.

### Features left to implement
In the future, more features can be added on the website. For instance, in order to attract international customers, the website can be translated into other languages and an option can be added to convert the prices to a different currency. The users can recieve different discounts, based on the accumulated amounts they have spent.


## Technologies Used
1. HTML5
2. CCS3
3. Bootstrap - for styling and a more structured layout.
4. JavaScript - to consume the Google Maps and Stripe APIs.
5. jQuery - for easier manipulation of the DOM.
6. Python + Django - to manage the database calls and render the different templates.
7. Postgres and sqlite
8. Google Maps JavaScript API - to render Google Maps.
9. Stripe API - to manage online payments.


## Testing
The testing procedure follows three steps - planning, implementation and outcomes.

Manual and automatic testing of all the features is carried out to establish the degree to which the application works as expected. All the pages, buttons, links and forms need to be manually visited, clicked on or filled in. The calls to the database and the Google Maps and Stripe APIs should return the expected outcomes. 

The navigation bar, appears in all of the pages and is intended to provide more structure and ease of use. When clicked, all the links lead to the expected page. Using the back command in the browser does not cause any problems. 

On the home page, the carousel and promotion cards appear correctly and change size, according to the screen size. On the products pages, the cards work as intended, and when clicked the additional information is displayed. Each product can be added to cart when the corresponding quantity is supplied. Adding a product to the cart redirects the user to the cart page, where they can see which products are currently in the cart. The checkout button brings the user to a page with a summary of the order and forms to complete the payment. The contact page provides the location of the store, shown on Google Maps and a contact form. 

Most of the fields in all of the forms are automatically validated by Django.

Apart from manual testing, the automatic tests have been run and passed. Each app has on average 80% coverage, as some built-in or pre-written Django files have not been tested. The tests cover different aspects of all the views, models, apps and forms in each app.

Different screen sizes have been tested to ensure responsiveness, in the developer tools and on [Responsinator](https://www.responsinator.com/). The website has also been run on various web browsers, such as Chrome, Safari, Internet Explorer and Microsoft Edge, leading to the conclusion the website is compatible with all of them. It does not perform well in most of the Firefox versions, as tested on [Browsershots](http://browsershots.org/). The HTML, CSS, JavaScript and Python codes have been validated by [HTML validator](https://validator.w3.org/), [CSS Validation service - Jigsaw](https://jigsaw.w3.org/css-validator/), [JSHint](https://jshint.com/) and [PEP8Online](http://pep8online.com/) respectively.

The outcomes of the manual and automatic testing show the the website and its features work as expected. The access to the different pages of the website is clear and straightforward as the header provides links to them. It is intuitive and makes it easy for a user to use. The different user stories achieve the intended outcome. 

It is important to note that setting Debug to False in the settings.py file prevents Django from sending emails and when requested displays an error with code 500.

## Deployment
1. A Github repository is created.
2. The site's source code is stored on the master branch (https://github.com/diovcharova/biospot).
3. After creating a new app on Heroku, the site is deployed by pushing the code by the command 'git push origin master' to the Github repository. Heroku is connected to it and deploys happen automatically with each new push. 

In order to deploy properly, a Procfile, specifying the dynos, and a 'requirements.txt' files are needed. The later is created and updated by the command 'pip freeze > requirements.txt' and contains the required frameworks and libraries for the application to run. Additionally, a web process needs to be started in the terminal and the variables need to be configured at Heroku. The evironment variables used locally also need to be added as 'config vars' on Heroku.

To run locally, the repository is cloned into the editor of choice by pasting 'git clone https://github.com/diovcharova/biospot' into the terminal.

## Credits

### Content
All of the content on the website is written by me. The products and their associated information are taken from Biospot's website (http://www.biospot.bg/). The map displayed on the 'Locations' page are a result to a call to the [Google Maps API](https://developers.google.com/maps/documentation/javascript/tutorial).
### Media
The photos used in this site were obtained Biospot's current website (http://www.biospot.bg/), inlcuding the logo in the navbar. 
### Acknowledgements 
The JavaScript functions, used to consume the API are inspired by Rosie's Resume project, built in the Interactive Frontend Development module of the course at Code Institute. 


