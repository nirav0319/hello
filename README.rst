
TildeHat Platform
=======================

Jira: https://tildehat.atlassian.net/
Best Practices: https://gitlab.com/samiranrl/tildehat_style_guide.git


Installation
=======================

- Install: 

sudo apt-get install --upgrade python3

sudo apt-get install python3-pip

- For psycopg2:

sudo apt-get install python3-setuptools

sudo apt-get install python3-dev libpq-dev

- For test cases:

pip3 install coverage

- Install requirements

pip3 install -r requirements.txt

- To run:

python3 manage.py runserver

open localhost:8000 in browser

Overview
=======================

The project is divided into two folders:

- config/ Global settings
- tildehat_core/ Contains apps, each one broadly responsible for *one* function, as well as the frontend elements in static/ and templates/

High level app details:

- profiles - which handle user+recruiter login, registration and authentication
- chat_agent - landing page, eventually the logic for tilde_lady
- job_search - the swiping ui for user jobs
- job_post - handle job posting and verification
- common - global elements to be used across all apps

