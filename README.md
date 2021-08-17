# Covid Tracker Backend

## This repo will become an API to obtain Brazil´s COVID-19 data.

### It is just a simple hello world yet, but if want to run this localy you need to follow a few steps:
## With Docker

    * Install Docker and Docker-compose
    * run 'docker-compose up --build' in the root of project
    * import the data into the database that docker will build (link to download in the end of this repo)
    * run 'docker exec <container name> python manage.py make migrations api'
    * run 'docker exec <container name> python manage.py make migrate'

### Obs: will be automated in the future

## Without Docker

    * Install python 3.8
    * Run 'pip install -r requirements.txt'
    * Download postgres
    * Create tables compatible with the models
    * import the data into the database that docker will build (link to download in the end of this repo)

Download the file ['caso.csv.gz'](https://brasil.io/dataset/covid19/files/)  to populate the database