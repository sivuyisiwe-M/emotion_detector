
# from flask import Flask, request, jsonify
# from emotion_detector import emotion_predictor
# # from .emotion_detector import emotion_predictor

# app = Flask(__name__)

# @app.route('/emotion', methods=['POST'])
# def detect_emotion():
#     try:
#         data = request.get_json()
#         if 'text' not in data:
#             return jsonify({"error": "Missing text parameter"}), 400
#         text = data['text']
#         if not text:
#             return jsonify({"error": "Invalid text"}), 400
#         response = emotion_predictor(text)
#         if "error" in response:
#             return jsonify(response), 400
#         return jsonify(response)
#     except Exception as e:
#         app.logger.error(f"Error processing request: {str(e)}")
#         return jsonify({"error": "Internal server error"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)



"""
Emotion detection server.

This module provides a Flask API for detecting emotions in text.
"""
from flask import Flask, request, jsonify
from emotion_detector import emotion_predictor

app = Flask(__name__)

# Define constants for error messages
ERROR_MISSING_TEXT = "Missing text parameter"
ERROR_INVALID_TEXT = "Invalid text"
ERROR_INTERNAL_SERVER = "Internal server error"

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    """
    Detect emotion in text.

    Expects a JSON payload with a 'text' parameter.
    Returns a JSON response with the detected emotion scores.
    """
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({"error": ERROR_MISSING_TEXT}), 400
        text = data['text']
        if not text:
            return jsonify({"error": ERROR_INVALID_TEXT}), 400
        response = emotion_predictor(text)
        if "error" in response:
            return jsonify(response), 400
        return jsonify(response)
    except TypeError as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": ERROR_INTERNAL_SERVER}), 500
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": ERROR_INTERNAL_SERVER}), 500

if __name__ == '__main__':
    app.run(debug=True)