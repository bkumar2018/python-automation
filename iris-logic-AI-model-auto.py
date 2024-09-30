import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('iris_logistic_regression_model.pkl')

# Example new data (let's say we're predicting for an Iris flower)
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Features: sepal length, sepal width, petal length, petal width

# Make a prediction
prediction = model.predict(new_data)
print(f"Predicted class: {prediction}")
