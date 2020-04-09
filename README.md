# capstone-coronaboard-api-country

This is part of the another projects for capstone Udacity CloudDeveloper

## Country Microservices

The objective for this microservice is got return list of countries affected with the Corona Virus

## Install

To run this make sure you have a Postgres database and Python3 on your machine:

- Execute the [sql](https://raw.githubusercontent.com/claudioacioli/capstone-corona-deployment/master/coronaboard.sql) file to create the database columns
- Clone this project 
```bash
git clone https://github.com/claudioacioli/capstone-coronaboard-api-contry.git api-country
```
- Create and active the environment
```bash
cd apy-country
python3 -m venv venv
source venv/bin/activate
```
- Install the requirements:
```bash
pip install requirements.txt
```

## Run

To execute this:

- Execute the environment file(Remember to edit it with your settings)
```bash
source env.sh
```
- Execute
```bash
flask run
```
