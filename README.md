# The Push Palace

## Background
Need a website that does the following:
    - hosts a login
    - user profile section
        - email, password, activities
    - all time leaderboard
    - enter activities screen
    - current month

## database
    - login
        - email
        - password
        - name
        - activities
    - activity
        - user_id
        - datetime
        - activity name
        - activity count

## How to Run
 - After pulling, create a `set_envvars.sh` file that looks like this:
 ```
export HASH=<your password>
 ```
 - Then you can run `docker compose build` and `docker compose up` to see your webpage
    