# Building Network Security System - MLOps Project

An end-to-end machine learning operations (MLOps) project for building a network security system with comprehensive ETL pipelines. This project implements a complete machine learning workflow to detect phishing and network security threats using advanced data processing, validation, transformation, and model training techniques.

## Project Overview

This MLOps project demonstrates best practices in:
- **Data Ingestion**: Automated data collection and storage in MongoDB
- **Data Validation**: Comprehensive data quality checks and schema validation
- **Data Transformation**: Feature engineering and preprocessing pipelines
- **Model Training**: Machine learning model development and evaluation
- **API Deployment**: FastAPI-based REST endpoints for predictions

## Architecture

The project follows a modular architecture with clear separation of concerns:

```
├── networksecurity/
│   ├── components/          # Core pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/            # Training pipeline orchestration
│   ├── exception/           # Custom exception handling
│   ├── logging/             # Logging utilities
│   ├── utils/               # Utility functions and model estimator
│   ├── entity/              # Configuration entities
│   └── constant/            # Project constants
├── app.py                   # FastAPI application
├── main.py                  # Training pipeline entry point
├── NetworkData/             # Dataset directory
└── final_model/             # Trained model artifacts
```

## Key Features

### 1. **Data Pipeline Components**
- **Data Ingestion**: Loads network security data (phishing dataset) into MongoDB
- **Data Validation**: Validates data schema and quality
- **Data Transformation**: Applies preprocessing and feature engineering
- **Model Training**: Trains machine learning models on transformed data

### 2. **API Endpoints**
- `GET /`: Redirects to FastAPI documentation
- `GET /train`: Initiates the training pipeline
- `POST /predict`: Accepts CSV files and returns predictions with confidence scores

### 3. **Model Persistence**
- Preprocessor artifact (`final_model/preprocessor.pkl`)
- Trained model artifact (`final_model/model.pkl`)

### 4. **Database Integration**
- MongoDB integration for data storage
- Configurable collections and databases
- SSL/TLS support for secure connections

## Installation

### Prerequisites
- Python 3.8+
- MongoDB
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/KirankumarDhanireddy/BuildingNetworkSecuritySystem.git
cd BuildingNetworkSecuritySystem
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in the project root:
```
MONGO_DB_URL=your_mongodb_connection_string
```

## Usage

### Training the Model

Run the complete training pipeline:
```bash
python main.py
```

This will execute:
1. Data Ingestion from `NetworkData/phisingData.csv`
2. Data Validation
3. Data Transformation
4. Model Training

### Starting the API Server

```bash
python app.py
```

The server will start on `http://0.0.0.0:8000`

### Making Predictions

1. **Via API Documentation**: Visit `http://localhost:8000/docs` (Swagger UI)
2. **Via cURL**:
```bash
curl -X POST "http://localhost:8000/predict" \
  -F "file=@your_data.csv"
```

### Triggering Training via API

```bash
curl -X GET "http://localhost:8000/train"
```

## Dataset

The project uses a phishing detection dataset with 31 features:

**Features include:**
- `having_IP_Address`
- `URL_Length`
- `Shortining_Service`
- `having_At_Symbol`
- `double_slash_redirecting`
- `Prefix_Suffix`
- `having_Sub_Domain`
- `SSLfinal_State`
- `Domain_registeration_length`
- `Favicon`
- `port`
- ... and 20 additional security features

**Target Values:**
- `-1`: Phishing/Suspicious
- `0`: Legitimate
- `1`: Suspicious

## Configuration

All configuration is managed through:
- `DataIngestionConfig`: MongoDB and data source settings
- `DataValidationConfig`: Schema validation rules
- `DataTransformationConfig`: Feature engineering parameters
- `ModelTrainerConfig`: Model training hyperparameters
- `TrainingPipelineConfig`: Overall pipeline orchestration

## Project Structure

```
NetworkData/
├── phisingData.csv          # Training dataset with 31 features

final_model/
├── preprocessor.pkl         # Fitted preprocessor for data transformation
├── model.pkl                # Trained machine learning model

prediction_output/
├── output.csv               # Prediction results
```

## Technology Stack

- **Framework**: FastAPI, Uvicorn
- **Data Processing**: Pandas, NumPy, Scikit-learn
- **Database**: MongoDB with PyMongo
- **Security**: SSL/TLS support, environment variable management
- **Template Engine**: Jinja2
- **CORS**: Cross-Origin Resource Sharing enabled

## API Response

Prediction endpoint returns:
- HTML table with input features
- Predicted class for each sample
- CSV output saved to `prediction_output/output.csv`

## Error Handling

The project includes custom exception handling with:
- `NetworkSecurityException`: Custom exception class for pipeline errors
- Comprehensive logging at each pipeline stage
- Traceback information for debugging

## CORS Configuration

The FastAPI application is configured with CORS enabled for:
- All origins (`*`)
- All HTTP methods
- All headers
- Credential support

## Future Enhancements

- Model versioning and registry
- Hyperparameter tuning
- Cross-validation
- Performance metrics dashboard
- Automated retraining schedule
- Model explainability (SHAP values)
- Unit and integration tests
- CI/CD pipeline

## License

This project is open source and available under the MIT License.

## Contact

For questions or contributions, please contact: KirankumarDhanireddy

---

**Last Updated**: 2026
