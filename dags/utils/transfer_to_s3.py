import awswrangler as wr

from aws import session
from extract_data import extract_selected_columns


def upload_to_s3():
    """
    Uploads a pandas dataframe to an s3 bucket using AWS Wrangler.

    :param data: pandas DataFrame to upload
    :param bucket_name: Name of the S3 bucket
    :param file_key: Path/key for the file in the bucket
    """

    # creating a variable to save outr extraxted data
    data = extract_selected_columns()

    # Verify that the dataFrame is not empty
    if data.empty:
        print("The DataFrame is empty. No data to upload.")
        return

    bucket_name = "s3://chisomnwa-bucket"
    file_key = "random-profiles.parquet"

    # Upload the Dataframe as a Parquet file to s3
    wr.s3.to_parquet(
        df=data,
        path=f"{bucket_name}/{file_key}",
        index=False,
        boto3_session=session(),
        dataset=True,
        mode='overwrite'
    )

    print(f"Data Successfully uploaded to {bucket_name}/{file_key}")
