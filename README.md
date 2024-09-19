# COVID Detection from Chest X-Ray Images

This project implements a deep learning model to detect COVID-19 from chest X-ray images. It includes a data preprocessing pipeline, model training scripts, and a Flask web application for easy deployment and usage.

## Project Structure

- `model.py`: Contains functions for image preprocessing and prediction
- `app.py`: Flask web application for serving predictions
- `templates/index.html`: HTML template for the web interface

## Features

- Data preprocessing for chest X-ray images
- CNN model architecture for COVID-19 detection
- Flask web application for easy deployment and usage
- User-friendly interface for image upload and analysis

## Prerequisites

- Python 3.7+
- TensorFlow 2.x
- Flask
- OpenCV
- NumPy
- Pillow

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/covid-detection.git
   cd covid-detection
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

1. Ensure you have Flask installed:
   ```
   pip install flask
   ```

2. Run the Flask app:
   ```
   python app.py
   ```

3. Open a web browser and go to `http://localhost:5000` to use the prediction interface.

### Using the Interface

1. Click on "Choose File" to select a chest X-ray image (PNG format only).
2. Click "Upload and Analyze" to process the image.
3. The result will be displayed, indicating whether COVID-19 is detected or not.

## Model Architecture

The project uses a Convolutional Neural Network (CNN) for COVID-19 detection. The exact architecture details can be found in the `model.py` file.

## Performance

The model's performance metrics, such as accuracy, precision, recall, and F1-score, should be added here once they are available from your training and evaluation process.

## Docker Support

This project includes Docker support for easy deployment. To use the Docker container:

1. Build the Docker image:
   ```
   docker build -t covid-detection-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 5000:5000 -v /path/to/models:/models covid-detection-app
   ```

Replace `/path/to/models` with the actual path to your model files on the host machine.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset source should be acknowledged here
- Inspired by various COVID-19 detection projects in the medical imaging domain

