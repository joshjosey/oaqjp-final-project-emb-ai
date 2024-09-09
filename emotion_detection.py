'''
Emotion detection project using watson embedded AI
'''
import requests
import json

def emotion_detector(text_to_analyze):
    #Set the URL, headers, and input object to send to the API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers ={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myObj = { "raw_document": { "text": text_to_analyze } }

    #send a POST request to update the API with the text to analyze
    response = requests.post(url, json=myObj , headers=headers)
    
    #format the repsponse text into a json
    formatted_res = json.loads(response.text)

    #extract the scores
    emotion_scores = formatted_res['emotionPredictions'][0]['emotion']
    #get the highest scoring emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    #return the response text
    return {'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion}