# Getting Started
To set up and run Slash:
1. Ensure you have the following installed:
    * [Python 3](https://www.python.org/downloads/) 
    * [pip](https://pip.pypa.io/en/stable/installation/)
    * [git](https://git-scm.com/)
    * [node.js](https://nodejs.org/en/download/)
2. Clone this repo onto your local machine
    ```
    git clone https://github.com/SE21-Team2/slash.git
    cd slash
    ```
3. In the repository directory, run
    ```
    pip install -r requirements.txt
    ```
4. Set up the database. Slash currently uses [Heroku](https://www.heroku.com/) as a cloud platform for running the bot, and uses a PostgreSQL database hooked up to the Heroku application that runs the bot.
   1. [Create a Heroku account](https://signup.heroku.com/login).
   2. Sign in to Heroku and create a new Heroku application.
   3. Add the Heroku Postgres extension (in the `Resources` tab of the Heroku application web UI).
   4. Acquire the PostgreSQL database connection URL (In the web UI inside the Heroku app, navigate to `Resources > Heroku Postgres > Settings > View Credentials...` and note the URI). Copy this URI into the `.env` file; your `.env` file should look like this: 
      ```
      # .env
      DATABASE_URL={your-database-url}
      ```
5. To start the Slash web app locally, in the root directory, run
    ```
    python server.py
    ```
   Open another terminal and run
    ```
    cd frontend
    npm install # This only needs to be done once
    ```
   When the packages have completed installing, run
    ```
    npm start
    ```
   A browser should open showing the web app.

## Running the app through Heroku

In order to run the app through Heroku, first ensure that the app is connected to, and deployed from, your GitHub repo. 
1. In the Heroku web UI for your app, navigate to `Deploy > GitHub` and connect the app to your Slash fork. 
2. After the app is deployed, navigate to `Resources`
3. Click the pencil icon, flip the switch to on, and click confirm, within the `worker` dyno.
4. In a terminal, run `python server.py` in the root directory of the project.
5. In a browser, go to `localhost:8080`.
6. After changes to code, run `npm run build` before pushing to the repo.

## Working with the Heroku PostgreSQL database
Working directly with the PostgreSQL database can be done through the PostgreSQL command line interface `psql`.

Setup:
1. [Install PostgreSQL on your system](https://www.postgresql.org/download/) (details differ depending on OS) and ensure you can access the `psql` program through a terminal.
2. Set up the heroku command line tool:
   1. [Install the heroku command line tool](https://devcenter.heroku.com/articles/heroku-cli)
   2. Authenticate to the Heroku CLI: `heroku login`
   3. Connect the Heroku CLI to your Heroku app: from your project's root directory run `heroku git:remote -a <name-of-your-app>`

You should now be able to connect to the Heroku PostgreSQL database through the `psql` client by running `heroku pg:psql` (if this step fails you may have not installed PostgreSQL correctly. Documentation for `psql` can be found [here](https://www.postgresql.org/docs/13/app-psql.html)

## Run Tests
To run tests on Slash, run `pytest` in the root directory.

## Run Pylint
To run the pylint style checker on Slash, run `pylint` in the root directory.