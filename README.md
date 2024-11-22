This project ...

## Project Steps
  * Go to https://randomuser.me/api
  * Pull 1000 profiles
  * Convert the profiles into a pandas Dataframe
  * When you go to the logs, you should see the shape of te dataframe
  * Use AWS Wrangler to transfer the data to S3


### Steps to Loading the Data into s3
 * Install AWS Wrangler or AWS SDK for Pandas: `pip install awswrangler`
 * Set up your AWS Credentials
    * Download AWS CLI on your terminal
    * Configure your AWS credentials
 * Create an s3 bucket
 * Create a function for data transfer
 * Update your dAG for the data transfer task
