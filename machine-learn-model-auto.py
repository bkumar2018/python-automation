from flask import Flask, request, jsonify
import joblib

# Load your pre-trained model
model = joblib.load('iris_logistic_regression_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting JSON input
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

