
# from flask import Flask, request, jsonify
# from emotion_detector import emotion_predictor

# app = Flask(__name__)

# @app.route('/emotion', methods=['POST'])
# def detect_emotion():
#     data = request.get_json()
#     if 'text' not in data:
#         return jsonify({"error": "Missing text parameter"}), 400
#     text = data['text']
#     response = emotion_predictor(text)
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)










from flask import Flask, request, jsonify
from app.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "Missing text parameter"}), 400
    text = data['text']
    if not text:
        return jsonify({"error": "Invalid text"}), 400
    response = emotion_predictor(text)
    if "error" in response:
        return jsonify(response), 400
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)










