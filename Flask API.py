import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
from predict import make_prediction

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    return """
    <html>
    <body style='padding: 10px;'>
    <h1>Welcome to my Flask API</h1>
    </body>
    </html>
    """

@app.route("/predict", methods=["POST"])
def predict():
    # Check if request contains an image file
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    # Get the image file from the request
    file = request.files['file']

    # Read the image file
    image = Image.open(io.BytesIO(file.read()))

    # Convert image to numpy array
    image_array = np.array(image)

    # Make prediction using the image array
    predictions = make_prediction(image_array)

    # Render the image and predictions in HTML
    return render_template('result.html', image_file=file, predictions=predictions.tolist())

if __name__ == "__main__":
    app.run()
