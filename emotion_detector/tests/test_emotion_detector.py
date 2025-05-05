import json
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.emotion_detector import emotion_predictor

def test_emotion_detection():
    # Sample text for testingS
    test_text = "I am happy to be learning about Python packaging!"
    
    # Call your emotion predictor function
    result = emotion_predictor(test_text)
    
    # Print formatted output
    print("Emotion Analysis Results:")
    print("------------------------")
    print(f"Input text: {test_text}")
    print("Emotions detected:")
    
    # Format and display emotion scores
    emotions = result.get('emotion', {}).get('document', {}).get('emotion', {})
    for emotion, score in emotions.items():
        print(f"  - {emotion.capitalize()}: {score:.4f}")

if __name__ == "__main__":
    test_emotion_detection()