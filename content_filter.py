import ast
import pandas as pd
import openai
from openai import AzureOpenAI

def getSecrets(region):
    '''
    This function fetches key and endpoints from secrets.csv
    given the AOAI service region
    '''

    df = pd.read_csv('secrets.csv')
    filtered_df = df[df['region'] == region]
    endpoint = filtered_df['endpoint'].iloc[0]
    key = filtered_df['key'].iloc[0]
    return key, endpoint
    
def getAoaiResponse(prompt, key, endpoint, api_version, deployment_name):
    '''
    This method calls the completion function of OpenAI and returns response.
    '''
    client = AzureOpenAI(
    api_key = key,
    api_version = api_version,
    azure_endpoint = endpoint
    )

    response = None
    error = None
    error_dict = {}
    try:
        response = client.completions.create(
        model = deployment_name,
        prompt=prompt,
        )
        return response
    except openai.BadRequestError as e:
        error = str(e)
        error_dict = ast.literal_eval(error[17:])
        df = pd.DataFrame(error_dict["error"]["innererror"]["content_filter_result"]).T
        return df
