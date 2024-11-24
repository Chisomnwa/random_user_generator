# Import packages
from .get_data import get_data

def extract_selected_columns():
    """
    This function is used to extract the desired columns from the dataset.
    """
    data = get_data()

    # Extract relevant columns
    data['first_name'] = data['name'].apply(lambda x: x['first']) # extract valuses of specific keys from the dictionary
    data['last_name'] = data['name'].apply(lambda x: x['last'])
    selected_columns = data[['gender', 'first_name', 'last_name']]

    return selected_columns
 
 