# Hybrid Football Analytics & Market Value Predictor ⚽📊

##  Overview
This project is a sophisticated hybrid system designed to demonstrate the integration of **Low-level programming (C++)** and **High-level Data Science (Python)**. It analyzes football player performance metrics and predicts their transfer market values using Machine Learning.

##  System Architecture

### 1. Performance Engine (C++)
- **Located in:** `/performance_engine`
- **Purpose:** Handles intensive calculations for individual player efficiency.
- **Why C++?** To demonstrate proficiency in memory management and high-speed execution for core algorithmic logic.

### 2. Data Intelligence Module (Python)
- **Located in:** `/data_science_model`
- **Purpose:** Performs Exploratory Data Analysis (EDA) and predictive modeling.
- **Tech Stack:** Pandas, Scikit-Learn, Matplotlib, Seaborn.
- **Algorithm:** Linear Regression model trained on key attributes like Age, Potential, and Overall Rating.



##  Project Structure
```text
.
├── performance_engine/
│   └── calculator.cpp       # C++ Source Code
├── data_science_model/
│   ├── predict_value.py     # Python ML Script
│   └── players.csv          # Sample Dataset
└── README.md                # Project Documentation
