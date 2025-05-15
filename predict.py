# predict.py
import joblib

# Load model dan encoder target
model = joblib.load("model/model_rf.joblib")
target_encoder = joblib.load("model/encoder_target.joblib")


def make_prediction(data):
    prediction = model.predict(data)
    return target_encoder.inverse_transform(prediction)[0]
