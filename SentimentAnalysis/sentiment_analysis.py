'''
 module that contains the means to conduct sentiment analysis on a string
'''

import json
import requests

def sentiment_analyzer(text_to_analyse):
    '''
     calls a API to conduct sentiment analysis on a given string
    '''

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService'
    + '/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        return {"label": formatted_response['documentSentiment']['label'],
                "score": formatted_response['documentSentiment']['score']}
    return {"label": None, "score": None}