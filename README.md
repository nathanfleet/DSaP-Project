# DSaP-Project
Team project for Data Security and Privacy course

## Installation
First you need to install Docker to get a database setup.

Once Docker is installed, you can install a Postgres docker container: docker run --name healthcare -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

Now, copy the .env.defaults file to a .env file and fill out the secret key.

## Getting Started
Create the virtual environment `python -m venv venv`.

Activate the virtual environment:
- Mac: `source venv/bin/activate`
- Windows: `venv\Scripts\activate`

To install all of the requirements, run `pip install -r requirements.txt`

To apply database migrations, run `python manage.py makemigrations`,
followed by `python manage.py migrate`

Start the development server using `python manage.py runserver`