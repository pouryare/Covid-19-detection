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
- Docker support for containerized deployment

## Prerequisites

- Docker

## Installation and Usage

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

## Development

For those interested in contributing or further developing the project:

1. Clone the repository:
   ```
   git clone https://github.com/pouryare/covid-detection.git
   ```

2. Install the required dependencies (consider using a virtual environment):
   ```
   pip install -r requirements.txt
   ```

3. Make your changes and test locally:
   ```
   python app.py
   ```

4. Build a new Docker image if necessary:
   ```
   docker build -t your-username/covid-detection-app:latest .
   ```

## Contributing

Contributions to this project are welcome! Please fork the repository from [https://github.com/pouryare/covid-detection](https://github.com/pouryare/covid-detection) and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset source: [Add the source of your dataset here]
- Inspired by various COVID-19 detection projects in the medical imaging domain

## Troubleshooting

If you encounter any issues while running the Docker container or using the web application, please check the following:

1. Ensure Docker is properly installed and running on your system.
2. Check if port 5000 is available on your machine. If not, you can map to a different port:
   ```
   docker run -d -p 8080:5000 --name covid-app pouryare/covid-detection-app:latest
   ```
   Then access the application at `http://localhost:8080`.

3. If you're having trouble with image uploads, ensure you're using PNG format images.

For any other issues, please open an issue on the GitHub repository.
