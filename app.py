import joblib
import numpy as np
from preprocess import preprocess
from flask import Flask, request, jsonify


app = Flask(__name__)

model = joblib.load('model.joblib')   # Loading the saved model
vectorizer = joblib.load('tf_idf.joblib')  # Loading the saved TF-IDF vectorizer 

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()  # Reading the incoming json data 

    reviews = data['reviews']  # Extract the feature values from the  message 

    process_review = preprocess(reviews) # Preprocess the review posted 

    process_review = vectorizer.transform([process_review])  # Exract features from the review 

    prediction = model.predict(process_review) # Predict the sentiment

    return jsonify({"prediction": prediction[0]})  # output the sentiment. jsonify is used to convert python dict to JSON object



@app.route("/health", methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0",  port=5000) # Host: 0.0.0.0 means any computer can  connect to this host 