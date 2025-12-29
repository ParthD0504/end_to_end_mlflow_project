# End-to-End Machine Learning Project with MLflow

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A production-ready end-to-end machine learning pipeline demonstrating best practices for ML project structure, experiment tracking with MLflow, and deployment using Flask and Docker.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [ML Pipeline Workflow](#ml-pipeline-workflow)
- [MLflow Tracking](#mlflow-tracking)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements a complete machine learning pipeline from data ingestion to model deployment. It demonstrates industry-standard practices including:

- Modular code architecture with reusable components
- Configuration-driven development using YAML files
- Experiment tracking and model versioning with MLflow
- Web interface for model predictions using Flask
- Containerization with Docker for consistent deployments
- CI/CD automation with GitHub Actions

## Project Structure

```
end_to_end_mlflow_project/
├── .github/
│   └── workflows/          # CI/CD pipeline configurations
├── artifacts/              # Generated artifacts (data, models, etc.)
├── config/
│   └── config.yaml         # Main configuration file
├── mlruns/                 # MLflow experiment tracking data
├── research/               # Jupyter notebooks for experimentation
├── src/
│   └── ml_project/         # Main source code package
│       ├── __init__.py
│       ├── components/     # ML pipeline components
│       ├── config/         # Configuration management
│       ├── constants/      # Project constants
│       ├── entity/         # Data classes and entities
│       ├── pipeline/       # Training and prediction pipelines
│       └── utils/          # Utility functions
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates for Flask app
├── app.py                  # Flask web application
├── main.py                 # Pipeline orchestration script
├── params.yaml             # Model hyperparameters
├── schema.yaml             # Data schema definitions
├── requirements.txt        # Python dependencies
├── setup.py                # Package installation script
├── template.py             # Project template generator
├── Dockerfile              # Docker configuration
└── README.md
```

## Features

- **Data Ingestion**: Automated data download and extraction
- **Data Validation**: Schema-based data quality checks
- **Data Transformation**: Feature engineering and preprocessing
- **Model Training**: Configurable model training with hyperparameter support
- **Model Evaluation**: Comprehensive metrics logging with MLflow
- **Prediction Service**: REST API for real-time predictions
- **Web Interface**: User-friendly UI for making predictions
- **Experiment Tracking**: Full MLflow integration for reproducibility
