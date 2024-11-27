# set your bas eimage
FROM apache/airflow:2.10.3

# sets your desired working directory
WORKDIR /downloads

# copy requirements.txt file from local to the downloads folder in the container
COPY requirements.txt /downloads

# Install the dependncies in the text file
RUN pip install --no-cache-dir -r /downloads/requirements.txt