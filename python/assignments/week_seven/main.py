import pandas as pd 
import matplotlib.pylot as plt 
import seaborn as sns 
from sklearn.datasets import load_iris 

# this will load and explore the dataset 

try: 
    # this will load the iris dataset from sklearn 
    iris_data = load_iris(as_frame=True) 
    df = iris_data.frame 
    df['species'] = df['target'].map(dict(enumerate(iris_data.target_names)))

    # this will print the message successfully 
    print("=>Dataset loaded successfully.\n")
except Exception as e: 
    print(f"Error loading dataset: {e}")

# this will display the first few rows 
print("First 5 rows of the dataset: ") 
print(df.head())

# Data structure and missing values 
print("\nDataset info:")
