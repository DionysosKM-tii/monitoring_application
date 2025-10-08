# monitoring_application
An application that will help monitoring specific areas by retrieving remote sense data and leverage ML tools

## Set Up
Create the conda environment by running: `conda env create -f environment.yml`  

Start the postgis DB by runnin: `docker compose up -d`

## Run the application
To run the application run: `python -m uvicorn backend.app:app --reload`.  
This will have the application running on: `http://localhost:8000`