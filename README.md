# game-recommendation-api
Python backend build top of flask and uses rawg open api to stream the game db for database operations.
Also uses sqlite for saving liked games for a user. For image recognition feature, it uses google reverse
image search engine in serpapi.

## Recommendation Engine

Initially the project used only a single genre of the selected game to recommend games to the user along
with the metacritic rating of the game. This wasn't good enough as some games belonged to more than one 
genre, hence selecting the best genre was a tedious task, and the recommended games were no where close 
to the original ones.

### Update 1.1

The number of games that the user can select was increased to three to provide more freedom to the user
to choose his/her favorite games. Also, a new image search feature was added where in the user can upload
a screenshot/poster of the game and the search engine would be able to guess the required game(s).

### Update 1.2

The recommendation architecture was improved to accommodate all the genres of a game. This not only
increased the variety of the games that were recommended but also improved the performance of the 
recommendation engine. Also, a random page of the games that belonged to a particular genre was selected to have more
variance in the recommended games on each subsequent recommendation.

## Getting Started with the project

The FE code repo is available at [https://github.com/abhin2149/game-recommendation-react](https://github.com/abhin2149/game-recommendation-react)

## Available Scripts

NOTE: To make sure docker is up and running in your system, run the following command:

### `docker --version`

In the project directory, you can run:

### `docker-compose up`

Runs the app in the development mode.\
Open [http://localhost:5000](http://localhost:5000) to view it in the browser.
