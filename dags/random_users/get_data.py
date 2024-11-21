# import packages
import pandas as pd
import requests


def extract_data():
    url = 'https://randomuser.me/api/?results=5'
    response = requests.get(url)
    response = response.json()['results']
    data = pd.DataFrame(response)
    return data


def get_shape():
    data_shape = extract_data()
    return (f"The DataFrame has {data_shape.shape[0]} rows and \
             {data_shape.shape[1]} columns")


print(get_shape())
