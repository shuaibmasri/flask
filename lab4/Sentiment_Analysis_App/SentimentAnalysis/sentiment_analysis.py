import requests
from textblob import TextBlob

## this function takes a string as input and returns the sentiment analysis result from the Watson Sentiment Analysis API
## and need Real endpoint from IBM Cloud, and the API key to work. You can get these from your IBM Cloud account after creating an instance of the Watson Sentiment Analysis service.
## Example usage:
## def sentiment_analyzer(text_to_analyse):
##   url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
##    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
##    json_data = {"raw_document": {"text": text_to_analyse}}
##    response = requests.post(url, json=json_data, headers=headers)
##    return response.text

## This function uses the TextBlob library to perform sentiment analysis on the input text. It returns a dictionary containing the polarity and subjectivity of the text.
def sentiment_analyzer(text):
    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }

##print(sentiment_analyzer("I love this product! It's amazing."))