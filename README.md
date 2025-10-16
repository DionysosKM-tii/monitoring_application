# monitoring_application
An application that will help monitoring specific areas by retrieving remote sense data and leverage ML tools

## Set Up
Clone the repository: `git clone https://github.com/DionysosKM-tii/monitoring_application.git` and `cd monitoring_application`

Create the conda environment by running: `conda env create -f environment.yml`  

Start the postgis DB by running: `docker compose up -d`  
Once the DB is up, perform the migrations by running: `alembic upgrade head`. 

Copy template.env to .env and modify the variables as needed. Keep the existing values to have the defaults,  
and for the missing values, follow the explanation in the file.

## Run the application
To run the application run: `python -m uvicorn backend.app:app --reload`.  
This will have the application running on: `http://localhost:8000`

## Run the frontend 
To run the frontend run : `python home_page.py`
This will have the frontend running on: `http://localhost:8080`
A new tab with the homepage will open automatically on your browser if not go to `http://localhost:8080` manually