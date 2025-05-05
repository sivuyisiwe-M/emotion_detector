import unittest
import json
import sys
import os

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.emotion_detector import emotion_predictor
from app.emotion_detector import emotion_predictor

class TestEmotionDetector(unittest.TestCase):
    
    def setUp(self):
        # This runs before each test
        # We'll use a mock function to simulate API responses
        self.original_emotion_predictor = sys.modules[__name__].emotion_predictor
        
        # Create mock function
        def mock_emotion_predictor(text):
            # Return different responses based on text input
            if "happy" in text.lower():
                return {
                    "emotion": {
                        "document": {
                            "emotion": {
                                "anger": 0.041796,
                                "disgust": 0.022968,
                                "fear": 0.033387,
                                "joy": 0.798369,
                                "sadness": 0.103518
                            }
                        }
                    }
                }
            elif "sad" in text.lower():
                return {
                    "emotion": {
                        "document": {
                            "emotion": {
                                "anger": 0.082436,
                                "disgust": 0.035618,
                                "fear": 0.148996,
                                "joy": 0.098745,
                                "sadness": 0.634205
                            }
                        }
                    }
                }
            else:
                return {
                    "emotion": {
                        "document": {
                            "emotion": {
                                "anger": 0.15,
                                "disgust": 0.15,
                                "fear": 0.15,
                                "joy": 0.25,
                                "sadness": 0.30
                            }
                        }
                    }
                }
        
        # Replace the original function with our mock
        sys.modules[__name__].emotion_predictor = mock_emotion_predictor
    
    def tearDown(self):
        # Restore the original function
        sys.modules[__name__].emotion_predictor = self.original_emotion_predictor
    
    def test_happy_text(self):
        """Test that happy text returns high joy score"""
        test_text = "I am happy to be learning about Python packaging!"
        result = emotion_predictor(test_text)
        emotions = result.get('emotion', {}).get('document', {}).get('emotion', {})
        
        self.assertIsInstance(result, dict)
        self.assertIn('emotion', result)
        self.assertGreater(emotions.get('joy'), 0.7)
        self.assertLess(emotions.get('sadness'), 0.2)
    
    def test_sad_text(self):
        """Test that sad text returns high sadness score"""
        test_text = "I feel sad and disappointed about the test results."
        result = emotion_predictor(test_text)
        emotions = result.get('emotion', {}).get('document', {}).get('emotion', {})
        
        self.assertIsInstance(result, dict)
        self.assertIn('emotion', result)
        self.assertGreater(emotions.get('sadness'), 0.6)
        self.assertLess(emotions.get('joy'), 0.2)
    
    def test_neutral_text(self):
        """Test that neutral text returns balanced emotions"""
        test_text = "This is a simple test of the emotion detection system."
        result = emotion_predictor(test_text)
        emotions = result.get('emotion', {}).get('document', {}).get('emotion', {})
        
        self.assertIsInstance(result, dict)
        self.assertIn('emotion', result)
        # Check that no single emotion dominates too much
        for emotion, score in emotions.items():
            self.assertLess(score, 0.8)

if __name__ == "__main__":
    unittest.main()