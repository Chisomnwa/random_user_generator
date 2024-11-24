# Random User Generator

This project is about exercising my skills on data pipeline orcehestration with **airflow**. A skill I learnt during my intensive data engineer Bootcamp training at Core Data Engineers.

## Project Tasks
  * Go to https://randomuser.me/api
  * Pull 1000 profiles
  * Convert the profiles into a Pandas Dataframe
  * When you go to the Airflow logs, you should see the shape of the dataframe
  * Use AWS Wrangler to transfer the data to S3

  ## Solution
  * Create your projct folder
  * Deploy Airflow on Docker Compose by fetching docker-copmpose.yaml and set
  * Create your necessary files like the `.env`, `Dockerfile`, and `requirements.txt` files.
  * Create your functions that you will use to get the data, from the APIU, extract the necessary columns, and load the data into Amazon S3.

  ## At the end, you will have:
  * **random_users folder** has the:

    * **get_data.py** - file that contains the function that gets the data from the API

    * **extract_data.py** - file that contains the function that extracts the necessary columns from the downloaded data

    * **transfer_data.py** - file that contains the function that uploads the data to Amazon s3.

* **dag_definition folder** has the:

    * **randon_users.py** - file that contains the DAG for the airflow orchestration.
    
