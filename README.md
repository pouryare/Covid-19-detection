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

- Docker

## Usage

### Running the Web Application using Docker

1. Pull the Docker image:
   ```
   docker pull pouryare/covid-detection-app:latest
   ```

2. Run the Docker container:
   ```
   docker run -d -p 5000:5000 --name covid-app pouryare/covid-detection-app:latest
   ```

3. Open a web browser and go to `http://localhost:5000` to use the prediction interface.

### Using the Interface

1. Click on "Choose File" to select a chest X-ray image (PNG format only).
2. Click "Upload and Analyze" to process the image.
3. The result will be displayed, indicating whether COVID-19 is detected or not.

## Model Architecture

The project uses a Convolutional Neural Network (CNN) for COVID-19 detection. The exact architecture details are encapsulated within the Docker image.

## Performance

The model's performance metrics, such as accuracy, precision, recall, and F1-score, are specific to the trained model included in the Docker image.

## Contributing

Contributions to this project are welcome! Please fork the repository from [https://github.com/pouryare/covid-detection](https://github.com/pouryare/covid-detection) and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset source should be acknowledged here
- Inspired by various COVID-19 detection projects in the medical imaging domain

