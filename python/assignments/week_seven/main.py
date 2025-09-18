import pandas as pd 
import matplotlib.pyplot as plt
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
print(df.info()) 

print("\nMissing values:")
print(df.isnull().sum())


# this is the basic statistics 
print("\n Descriptive statics")
print(df.describe())

# group by species and compute mean 
grouped = df.groupby('species').mean(numeric_only=True)
print("\nMean values grouped by species:")
print(grouped) 


# pattern observation (print a note) 
print("\nObservation: ")



# Data visualization 

# Set a seaborn style
sns.set(style="whitegrid")

# 1. Line chart (dummy time trend using index)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title('Line Chart: Sepal vs Petal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6, 4))
sns.barplot(x=grouped.index, y=grouped['petal length (cm)'])
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(6, 4))
sns.histplot(df['sepal width (cm)'], bins=10, kde=True)
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(6, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Scatter Plot: Sepal Length vs Petal Length')

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()


df.to_csv('cleaned_iris.csv', index=False)

