from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
import json

def emotion_predictor(text):
    try:
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2022-04-07',
            iam_apikey='ufDnkI-MpSqQLwmpanscXNdvG-hO6sNbCwzMYhfskex8',
            url='https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/d495df77-7eca-4b93-9a75-ef170f1ac1db'
        )
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(emotion=EmotionOptions(targets=None))).get_result()
        emotion_scores = response['emotion']['document']['emotion']
        return emotion_scores
    except Exception as e:
        return {"error": str(e)}

text = "I am happy today"
print(emotion_predictor(text))