"""
Project: Product Portfolio Performance & Revenue Optimization Analytics
Author: Your Name
Description:
Sales performance analytics solution to identify peak purchasing hours
and revenue optimization opportunities using Python.
"""

# ===============================
# Import Required Libraries
# ===============================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Configuration
# ===============================

DATA_PATH = "sales_data.csv"
OUTPUT_DIR = "../visualizations"
OUTPUT_FILE = "hourly_sales.png"

# ===============================
# Data Loading Function
# ===============================

def load_data(file_path):
    """
    Loads transactional sales dataset.
    """
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return df
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        exit()

# ===============================
# Data Preprocessing Function
# ===============================

def preprocess_data(df):
    """
    Cleans data and performs DateTime feature engineering.
    """
    # Remove missing values
    df = df.dropna()

    # Convert Order Date to DateTime
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Extract Hour Feature
    df['Hour'] = df['Order Date'].dt.hour

    print("Data preprocessing completed.")
    return df

# ===============================
# Sales Analysis Function
# ===============================

def analyze_hourly_sales(df):
    """
    Aggregates sales by hour to identify peak revenue periods.
    """
    hourly_sales = df.groupby('Hour')['Sales'].sum().sort_index()
    print("Hourly sales analysis completed.")
    return hourly_sales

# ===============================
# Visualization Function
# ===============================

def visualize_sales(hourly_sales):
    """
    Generates and saves hourly sales distribution chart.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    plt.figure()
    hourly_sales.plot(kind='bar')
    plt.xlabel("Hour of Day")
    plt.ylabel("Total Sales")
    plt.title("Hourly Sales Distribution")
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, OUTPUT_FILE))
    plt.close()

    print("Visualization saved successfully.")

# ===============================
# Main Execution
# ===============================

def main():
    df = load_data(DATA_PATH)
    df = preprocess_data(df)
    hourly_sales = analyze_hourly_sales(df)
    visualize_sales(hourly_sales)

    print("Analysis Complete! Project executed successfully.")

if __name__ == "__main__":
    main()