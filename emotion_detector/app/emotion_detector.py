

# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# import json

# def emotion_predictor(text):
#     # Set up authenticator with your API key
#     authenticator = IAMAuthenticator('ufDnkI-MpSqQLwmpanscXNdvG-hO6sNbCwzMYhfskex8')
    
#     # Create service object
#     natural_language_understanding = NaturalLanguageUnderstandingV1(
#         version='2022-04-07',
#         authenticator=authenticator
#     )
    
#     # Set the service URL
#     natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/d495df77-7eca-4b93-9a75-ef170f1ac1db')
    
#     # Call the analyze method
#     response = natural_language_understanding.analyze(
#         text=text,
#         features=Features(emotion=EmotionOptions())).get_result()
    
#     return response


# if __name__ == "__main__":
#     sample_text = "I am so happy about this wonderful day!"
#     result = emotion_predictor(sample_text)
#     print(json.dumps(result, indent=2))





# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
# import json
# from ibm_cloud_sdk_core import ApiException

# def emotion_predictor(text):
#     try:
#         natural_language_understanding = NaturalLanguageUnderstandingV1(
#             version='2022-04-07',
#             iam_apikey='ufDnkI-MpSqQLwmpanscXNdvG-hO6sNbCwzMYhfskex8',
#             url='https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/d495df77-7eca-4b93-9a75-ef170f1ac1db'
#         )
#         response = natural_language_understanding.analyze(
#             text=text,
#             features=Features(emotion=EmotionOptions(targets=None))).get_result()
#         emotion_scores = response['emotion']['document']['emotion']
#         return emotion_scores
#     except ApiException as e:
#         if e.code == 400:
#             return {"error": "Invalid request. Please check your input."}
#         else:
#             return {"error": str(e)}
#     except Exception as e:
#         return {"error": str(e)}





from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from ibm_cloud_sdk_core import ApiException

def emotion_predictor(text):
    try:
        authenticator = IAMAuthenticator('ufDnkI-MpSqQLwmpanscXNdvG-hO6sNbCwzMYhfskex8')
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2022-04-07',
            authenticator=authenticator
        )
        natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/d495df77-7eca-4b93-9a75-ef170f1ac1db')
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(emotion=EmotionOptions(targets=None))).get_result()
        emotion_scores = response['emotion']['document']['emotion']
        return emotion_scores
    except ApiException as e:
        if e.code == 400:
            return {"error": "Invalid request. Please check your input."}
        else:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}