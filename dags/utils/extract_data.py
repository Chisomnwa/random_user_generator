# Import packages
import pandas as pd
import requests

def get_api_data():
    """
    This function is used to get the 100 random profiles data
    from the api and then turn the data into a pandas DataFrame.
    """
    url = 'https://randomuser.me/api/?results=1000'
    response = requests.get(url)
    response = response.json()['results']
    data = pd.DataFrame(response)
    return data


def extract_selected_columns():
    """
    This function is used to extract the desired columns from the dataset.
    """
    data = get_api_data()

    # Extract relevant columns
    data['first_name'] = data['name'].apply(lambda x: x['first'])
    data['last_name'] = data['name'].apply(lambda x: x['last'])
    selected_columns = data[['gender', 'first_name', 'last_name']]

    return selected_columns
