import pickle
from flask import Flask, request, jsonify

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Parse input JSON
    input_data = request.get_json()
    features = input_data["features"]  # Assume a list of features is provided

    # Make a prediction
    prediction = model.predict([features])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)