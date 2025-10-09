# monitoring_application
An application that will help monitoring specific areas by retrieving remote sense data and leverage ML tools

## Set Up
Clone the repository: `git clone https://github.com/DionysosKM-tii/monitoring_application.git` and `cd monitoring_application`

Create the conda environment by running: `conda env create -f environment.yml`  

Start the postgis DB by running: `docker compose up -d`  
Once the DB is up, perform the migrations by running: `alembic upgrade head`. 

## Run the application
To run the application run: `python -m uvicorn backend.app:app --reload`.  
This will have the application running on: `http://localhost:8000`