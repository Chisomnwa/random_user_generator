# import packages
import pandas as pd
import requests


def get_data():
    """
    This function is used to get the 100 random profiles data
    from the api and then turn the data into a pandas DataFrame.
    """
    url = 'https://randomuser.me/api/?results=1000'
    response = requests.get(url)
    response = response.json()['results']
    data = pd.DataFrame(response)
    return data
