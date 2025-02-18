```python
# Importing necessary libraries
import csv
import pandas as pd
import numpy as np

# Load data from csv file
def load_data(filename):
    try:
        data = pd.read_csv(filename)
        print(f"Data loaded successfully from {filename}")
        return data
    except Exception as e:
        print("An error occurred:", e)

# Analyze data
def analyze_data(data):
    try:
        print('Data Analysis:')
        print('Shape of data:', data.shape)
        print('Columns in data:', data.columns.tolist())
        print('Data types of columns:', data.dtypes)
    except Exception as e:
        print("An error occurred:", e)

# Cleaning data
def clean_data(data):
    try:
        print('Starting data cleaning...')
        # Handling missing values
        data = data.replace('', np.nan)
        if data.isnull().sum().sum() > 0:
            print('Missing values in data:', data.isnull().sum())
            # Fill missing values with mean
            data = data.fillna(data.mean())
            print('Missing values handled')
        else:
            print('No missing values in data')
        # Removing duplicates
        initial_size = data.shape[0]
        data = data.drop_duplicates()
        print(f'Dropped {initial_size - data.shape[0]} duplicates')
        print('Data cleaning done')
        return data
    except Exception as e:
        print("An error occurred:", e)

# Descriptive statistics of data
def describe_data(data):
    try:
        print('Descriptive Statistics:')
        print(data.describe())
    except Exception as e:
        print("An error occurred:", e)

# Write data to csv
def write_data(data, filename):
    try:
        data.to_csv(filename, index=False)
        print(f"Data written successfully to {filename}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    filename = 'data.csv'
    # Load data
    data = load_data(filename)
    # Analyze data
    analyze_data(data)
    # Clean data
    data = clean_data(data)
    # Describe data
    describe_data(data)
    # Write data to new csv file
    write_data(data, 'clean_data.csv')
```
Цей код виконує деякі основні операції обробки даних: завантаження даних з файлу CSV, аналіз розміру та форми даних, очищення даних (включаючи обробку відсутніх значень та видалення дублікатів), отримання описових статистичних даних та запису даних у новий файл CSV.