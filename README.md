# Ops Random Forest Breast Cancer Classifier

A machine learning project for breast cancer classification using the Random Forest algorithm. This project demonstrates data preprocessing, model training, evaluation, and deployment best practices for a binary classification problem in healthcare.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data](#data)
- [Model](#model)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This repository contains code and documentation for building a breast cancer classifier using the Random Forest algorithm. The goal is to predict whether a tumor is malignant or benign based on clinical features. The project follows best practices in data science and DevOps for reproducibility and maintainability.

## Features

- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Random Forest model training and hyperparameter tuning
- Model evaluation with metrics (accuracy, precision, recall, F1-score, ROC-AUC)
- Model persistence (saving/loading)
- Example API for model inference
- Automated tests and CI/CD integration

## Installation

1. **Clone the repository:**

```
git clone https://github.com/yourusername/ops-random-forest-breast.git
cd ops-random-forest-breast
```

2. **Create and activate a virtual environment (optional but recommended):**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```
pip install -r requirements.txt
```

## Usage

1. **Prepare the data:**

- Place your dataset (e.g., `data.csv`) in the `data/` directory.

2. **Train the model:**

```
python src/train.py --data data/data.csv
```

3. **Evaluate the model:**

```
python src/evaluate.py --model models/random_forest.pkl --data data/test.csv
```

4. **Run the API (optional):**

```
uvicorn src.api:app --reload
```

## Contact

- **LinkedIn:** [https://www.linkedin.com/in/mohammad-rammal](https://www.linkedin.com/in/mohammad-rammal)
- **Email:** mohammad.rammal@hotmail.com
