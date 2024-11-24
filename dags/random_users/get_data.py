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

# JUMP THIS SECTION IF WE WILL BE USING THE extract_data python script
# def extract_selected_columns():
#     data = get_data()

#     # Extract relevant columns
#     data['first_name'] = data['name'].apply(lambda x: x['first']) # extract valuses of specific keys from the dictionary
#     data['last_name'] = data['name'].apply(lambda x: x['last'])
#     selected_data = data[['gender', 'first_name', 'last_name']]

#     return selected_data

# print(extract_selected_columns())  

# def get_shape():
#     data_shape = get_data()
#     return (f"The DataFrame has {data_shape.shape[0]} rows and \
#              {data_shape.shape[1]} columns")


# print(get_shape())
