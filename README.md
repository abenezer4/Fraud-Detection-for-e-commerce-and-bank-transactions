Fraud Detection for E-commerce and Bank Transactions
Project Overview
This project, conducted for Adey Innovations Inc., aims to improve the detection of fraudulent cases in e-commerce and bank credit card transactions. By leveraging geolocation data, behavioral feature engineering, and advanced machine learning models, the project builds a robust system capable of identifying suspicious activities while balancing the trade-off between security and user experience.
Key Features
Geolocation Integration: Mapping IP addresses to countries for regional fraud analysis.
Behavioral Sensors: Feature engineering focused on transaction velocity and latency (e.g., time since signup).
Class Imbalance Management: Utilizing SMOTE to handle extreme class disparities in training data.
Explainable AI (XAI): Utilizing SHAP to provide transparency for model predictions (Upcoming in Task 3).
Project Structure
The repository is organized as follows:
code
Text
fraud-detection/
├── .vscode/                 # VSCode settings
├── .github/                 # GitHub actions for automated testing
├── data/
│   ├── raw/                 # Original datasets (git-ignored)
│   └── processed/           # Cleaned and feature-engineered data
├── notebooks/
│   ├── eda-fraud-data.ipynb # Analysis of E-commerce data
│   ├── eda-creditcard.ipynb  # Analysis of Bank data
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   └── shap-explainability.ipynb
├── src/                     # Modular python scripts
│   └── data_loader.py       # Centeralized data loading logic
├── tests/                   # Unit tests
├── models/                  # Saved model artifacts (.pkl files)
├── scripts/                 # Utility scripts
├── requirements.txt         # Project dependencies
└── README.md
Installation and Setup
1. Clone the Repository
code
Bash
git clone https://github.com/abenezer4/Fraud-Detection-for-e-commerce-and-bank-transactions.git
cd Fraud-Detection-for-e-commerce-and-bank-transactions
2. Environment Setup
It is recommended to use a virtual environment:
code
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
code
Bash
pip install -r requirements.txt
Task 1 Milestones (Completed for Interim-1)
Data Cleaning & EDA
Duplicate Removal: Identified and removed 1,081 duplicates in the bank dataset.
Class Analysis: Documented extreme imbalance (0.17% fraud in banking; 9.3% in e-commerce).
Visualization: Analyzed fraud distribution by browser, marketing source, and purchase value.
Geolocation Integration
Implemented a high-performance pd.merge_asof lookup to map numerical IP addresses to countries.
Handled mapping gaps by categorizing 14.5% of records as "Unknown" countries.
Feature Engineering
Time to Purchase: Created duration features between signup and purchase to identify automated bots.
Device Frequency: Engineered velocity features tracking the number of users per device.
Handling Imbalance
Applied SMOTE (Synthetic Minority Over-sampling Technique) to the training data.
Balanced the e-commerce training set from 11,321 fraud cases to 109,568 cases.
Data Sources
Fraud_Data.csv: E-commerce transactions.
IpAddress_to_Country.csv: IP mapping table.
creditcard.csv: Anonymized bank transactions.